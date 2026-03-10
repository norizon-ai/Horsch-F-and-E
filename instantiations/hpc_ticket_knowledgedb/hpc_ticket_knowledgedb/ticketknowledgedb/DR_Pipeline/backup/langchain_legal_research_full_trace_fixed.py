#!/usr/bin/env python3
"""
LangChain-basiertes deutsches Rechtssystem mit vollständigem Phoenix Tracing
Trackt sowohl Suchen als auch LLM-Generierungen (ohne OpenAI Instrumentation)
"""

import asyncio
import os
import sys
import json
import requests
import re
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid

# Phoenix tracing imports
from phoenix.otel import register
from opentelemetry import trace

# LangChain imports - minimal
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler

# Pydantic for data models
from pydantic import BaseModel, Field

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration
OPENAI_COMPATIBLE_BASE_URL = "http://lme49.cs.fau.de:30000/v1"
OPENAI_COMPATIBLE_API_KEY = "dummy"
OPENAI_COMPATIBLE_MODEL = "openai/gpt-oss-120b"

ELASTIC_URL = os.getenv("ELASTIC_URL", "http://localhost:9200")
ELASTIC_INDEX = "inform"

# Configure Phoenix tracing
try:
    tracer_provider = register(
        project_name="full-trace-legal-research-fixed",
        endpoint="http://localhost:6006/v1/traces",
        auto_instrument=True
    )
    
    print("✅ Phoenix tracing enabled at http://localhost:6006")
    print("✅ Manual LLM generation tracing enabled")
except Exception as e:
    print(f"⚠️ Phoenix tracing not available: {e}")
    tracer_provider = None

# Enhanced callback handler for detailed LLM tracing
class ComprehensiveLLMCallbackHandler(BaseCallbackHandler):
    """Comprehensive callback handler for detailed LLM tracing in Phoenix"""
    
    def __init__(self):
        super().__init__()
        self.tracer = trace.get_tracer(__name__)
        self.current_span = None
    
    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs) -> None:
        """Called when LLM starts generating"""
        self.current_span = self.tracer.start_span("LLM Generation")
        self.current_span.set_attribute("llm.model", OPENAI_COMPATIBLE_MODEL)
        self.current_span.set_attribute("llm.prompts_count", len(prompts))
        self.current_span.set_attribute("llm.total_prompt_length", sum(len(p) for p in prompts))
        
        # Add first prompt preview
        if prompts:
            preview = prompts[0][:200] + "..." if len(prompts[0]) > 200 else prompts[0]
            self.current_span.set_attribute("llm.prompt_preview", preview)
        
        print(f"🤖 Phoenix: LLM generation starting (Model: {OPENAI_COMPATIBLE_MODEL})")
    
    def on_llm_end(self, response, **kwargs) -> None:
        """Called when LLM finishes generating"""
        if self.current_span:
            if hasattr(response, 'generations') and response.generations:
                total_length = 0
                for gen_list in response.generations:
                    for gen in gen_list:
                        if hasattr(gen, 'text'):
                            total_length += len(gen.text)
                        elif hasattr(gen, 'message') and hasattr(gen.message, 'content'):
                            total_length += len(gen.message.content)
                
                self.current_span.set_attribute("llm.response_length", total_length)
                self.current_span.set_attribute("llm.generations_count", len(response.generations))
                
                # Add response preview
                if response.generations and response.generations[0]:
                    first_gen = response.generations[0][0]
                    if hasattr(first_gen, 'text'):
                        preview = first_gen.text[:200] + "..." if len(first_gen.text) > 200 else first_gen.text
                    elif hasattr(first_gen, 'message') and hasattr(first_gen.message, 'content'):
                        preview = first_gen.message.content[:200] + "..." if len(first_gen.message.content) > 200 else first_gen.message.content
                    else:
                        preview = "No content available"
                    self.current_span.set_attribute("llm.response_preview", preview)
            
            self.current_span.end()
            self.current_span = None
        
        print(f"✅ Phoenix: LLM generation completed")
    
    def on_llm_error(self, error: Exception, **kwargs) -> None:
        """Called when LLM encounters an error"""
        if self.current_span:
            self.current_span.set_attribute("llm.error", str(error))
            self.current_span.set_attribute("llm.error_type", type(error).__name__)
            self.current_span.end()
            self.current_span = None
        
        print(f"❌ Phoenix: LLM generation error: {error}")

# Initialize OpenAI-compatible LLM with enhanced tracing
llm_callback = ComprehensiveLLMCallbackHandler()

llm = ChatOpenAI(
    base_url=OPENAI_COMPATIBLE_BASE_URL,
    api_key=OPENAI_COMPATIBLE_API_KEY,
    model=OPENAI_COMPATIBLE_MODEL,
    temperature=0.2,
    max_tokens=2000,
    model_kwargs={},
    callbacks=[llm_callback]
)

# Data models
class SearchResult(BaseModel):
    """Suchergebnis aus der LEXinform-Datenbank"""
    recordid: str = Field(description="Eindeutige Datensatz-ID")
    text: str = Field(description="Volltext des Rechtsdokuments")
    score: float = Field(description="Relevanz-Score")
    highlight: Optional[str] = Field(description="Hervorgehobene Textpassagen")

class LegalSearchResults(BaseModel):
    """Sammlung von Rechtsdokument-Suchergebnissen"""
    query: str = Field(description="Ursprüngliche Suchanfrage")
    results: List[SearchResult] = Field(description="Liste der gefundenen Dokumente")
    total_found: int = Field(description="Gesamtanzahl gefundener Dokumente")
    error: Optional[str] = Field(description="Fehlermeldung falls Suche fehlschlug")

# Elasticsearch search function
async def search_elasticsearch(query: str) -> LegalSearchResults:
    """Durchsucht die LEXinform-Elasticsearch-Datenbank"""
    try:
        search_data = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["text"],
                    "type": "best_fields",
                    "fuzziness": "AUTO"
                }
            },
            "size": 10,
            "_source": ["recordid", "text", "indexed_at", "text_length"],
            "highlight": {
                "fields": {
                    "text": {
                        "fragment_size": 200,
                        "number_of_fragments": 3
                    }
                }
            },
            "sort": [
                {"_score": {"order": "desc"}},
                {"text_length": {"order": "desc"}}
            ]
        }

        search_url = f"{ELASTIC_URL}/{ELASTIC_INDEX}/_search"
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(search_url, json=search_data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            raw_results = response.json()
            hits = raw_results.get("hits", {}).get("hits", [])
            total = raw_results.get("hits", {}).get("total", {}).get("value", 0)
            
            results = []
            for hit in hits:
                source = hit.get("_source", {})
                highlight = hit.get("highlight", {}).get("text", [])
                highlight_text = " ... ".join(highlight) if highlight else None
                
                result = SearchResult(
                    recordid=source.get("recordid", ""),
                    text=source.get("text", ""),
                    score=hit.get("_score", 0.0),
                    highlight=highlight_text
                )
                results.append(result)
            
            return LegalSearchResults(
                query=query,
                results=results,
                total_found=total,
                error=None
            )
        else:
            return LegalSearchResults(
                query=query,
                results=[],
                total_found=0,
                error=f"Elasticsearch-Fehler: {response.status_code} - {response.text}"
            )
            
    except Exception as e:
        return LegalSearchResults(
            query=query,
            results=[],
            total_found=0,
            error=f"Suchfehler: {str(e)}"
        )

def parse_channel_tags_for_searches(text: str) -> List[Dict[str, str]]:
    """Parst Channel Tags und extrahiert Suchanfragen"""
    searches = []
    
    # Pattern für rechtsdatenbank_suche
    pattern1 = r'<\|channel\|>commentary to=functions\.rechtsdatenbank_suche.*?"suchanfrage":\s*"([^"]+)"'
    matches1 = re.findall(pattern1, text, re.DOTALL)
    for match in matches1:
        searches.append({"type": "general", "query": match})
    
    # Pattern für spezifische_rechtsnorm_suche
    pattern2 = r'<\|channel\|>commentary to=functions\.spezifische_rechtsnorm_suche.*?"gesetz":\s*"([^"]+)".*?"paragraph":\s*"([^"]+)"'
    matches2 = re.findall(pattern2, text, re.DOTALL)
    for match in matches2:
        searches.append({"type": "specific", "gesetz": match[0], "paragraph": match[1]})
    
    # Alternative Pattern
    pattern3 = r'"suchanfrage":\s*"([^"]+)"'
    matches3 = re.findall(pattern3, text)
    for match in matches3:
        if not any(s["query"] == match for s in searches if s.get("query")):
            searches.append({"type": "general", "query": match})
    
    return searches

async def execute_search(search_info: Dict[str, str]) -> str:
    """Führt eine Suche basierend auf den extrahierten Informationen aus"""
    tracer = trace.get_tracer(__name__)
    
    if search_info["type"] == "general":
        query = search_info["query"]
        print(f"🔍 Durchsuche Rechtsdatenbank nach: {query}")
        
        with tracer.start_as_current_span("Enhanced Elasticsearch Search") as span:
            span.set_attribute("search.query", query)
            span.set_attribute("search.type", "general")
            span.set_attribute("search.index", ELASTIC_INDEX)
            span.set_attribute("search.timestamp", datetime.now().isoformat())
            
            results = await search_elasticsearch(query)
            
            # Add comprehensive search results to span
            span.set_attribute("search.results_count", len(results.results))
            span.set_attribute("search.total_found", results.total_found)
            span.set_attribute("search.success", not bool(results.error))
            
            # Add top result details
            if results.results:
                top_result = results.results[0]
                span.set_attribute("search.top_result.recordid", top_result.recordid)
                span.set_attribute("search.top_result.score", top_result.score)
                span.set_attribute("search.top_result.text_length", len(top_result.text))
                
                # Add all record IDs and scores
                record_data = [{"id": r.recordid, "score": r.score} for r in results.results]
                span.set_attribute("search.all_results", json.dumps(record_data))
                
                # Add text preview of top result
                text_preview = top_result.text[:300] + "..." if len(top_result.text) > 300 else top_result.text
                span.set_attribute("search.top_result.text_preview", text_preview)
            
            if results.error:
                span.set_attribute("search.error", results.error)
                return f"❌ Suchfehler: {results.error}"
            
            if not results.results:
                return f"❌ Keine Ergebnisse für '{query}' gefunden."
            
            formatted_results = f"✅ {len(results.results)} Rechtsdokumente gefunden für '{query}':\n\n"
            
            for i, result in enumerate(results.results, 1):
                text_preview = result.text[:400] + "..." if len(result.text) > 400 else result.text
                
                formatted_results += f"**Dokument {i}** (ID: {result.recordid}, Score: {result.score:.2f})\n"
                formatted_results += f"Text: {text_preview}\n"
                
                if result.highlight:
                    formatted_results += f"Highlights: {result.highlight}\n"
                
                formatted_results += "\n---\n\n"
            
            print(f"✅ {len(results.results)} Rechtsdokumente gefunden")
            return formatted_results
    
    elif search_info["type"] == "specific":
        gesetz = search_info["gesetz"]
        paragraph = search_info["paragraph"]
        query = f"{gesetz} {paragraph}"
        print(f"🔍 Suche spezifische Rechtsnorm: {query}")
        
        with tracer.start_as_current_span("Enhanced Specific Legal Norm Search") as span:
            span.set_attribute("search.gesetz", gesetz)
            span.set_attribute("search.paragraph", paragraph)
            span.set_attribute("search.query", query)
            span.set_attribute("search.type", "specific")
            span.set_attribute("search.timestamp", datetime.now().isoformat())
            
            results = await search_elasticsearch(query)
            span.set_attribute("search.results_count", len(results.results))
            span.set_attribute("search.success", not bool(results.error))
            
            if results.error:
                span.set_attribute("search.error", results.error)
                return f"❌ Fehler bei Rechtsnorm-Suche: {results.error}"
            
            if not results.results:
                return f"❌ Keine Rechtsnorm '{query}' gefunden."
            
            best_result = results.results[0]
            span.set_attribute("result.recordid", best_result.recordid)
            span.set_attribute("result.score", best_result.score)
            span.set_attribute("result.text_length", len(best_result.text))
            
            formatted_result = f"✅ Rechtsnorm {query} gefunden:\n\n"
            formatted_result += f"**Datensatz-ID:** {best_result.recordid}\n"
            formatted_result += f"**Relevanz-Score:** {best_result.score:.2f}\n\n"
            formatted_result += f"**Volltext:**\n{best_result.text}\n\n"
            
            if best_result.highlight:
                formatted_result += f"**Wichtige Passagen:**\n{best_result.highlight}\n"
            
            print(f"✅ Rechtsnorm {query} gefunden (ID: {best_result.recordid})")
            return formatted_result
    
    return "❌ Unbekannter Suchtyp"

async def comprehensive_legal_research(user_query: str) -> str:
    """Führt umfassende Rechtsrecherche mit vollständigem Tracing durch"""
    tracer = trace.get_tracer(__name__)
    
    with tracer.start_as_current_span("Comprehensive Legal Research Process") as span:
        span.set_attribute("user_query", user_query)
        span.set_attribute("user_query_length", len(user_query))
        span.set_attribute("research_start_time", datetime.now().isoformat())
        
        # Schritt 1: Erste Analyse durch das Reasoning Model
        print("🧠 Analysiere Rechtsfrage mit Reasoning Model...")
        
        with tracer.start_as_current_span("Initial Legal Analysis & Query Planning") as span:
            system_prompt = """Du bist ein erfahrener deutscher Rechtsanwalt, spezialisiert auf Steuerrecht.

Analysiere die folgende Rechtsfrage und identifiziere die wichtigsten Suchbegriffe für die Rechtsdatenbank.

Erstelle eine Liste von Suchanfragen, die du benötigst, um eine umfassende rechtliche Analyse zu erstellen.

Konzentriere dich auf deutsche Steuerrecht-Begriffe wie:
- EStG (Einkommensteuergesetz) Paragraphen
- Werbungskosten, Sonderausgaben, außergewöhnliche Belastungen
- Kindesunterhalt, Ausbildungsunterhalt
- Kindergeld, Kinderfreibetrag
- BAföG steuerliche Behandlung

Gib deine Antwort in folgendem Format:
SUCHANFRAGEN:
1. [Suchbegriff 1]
2. [Suchbegriff 2]
3. [Suchbegriff 3]
etc."""

            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_query)
            ]
            
            span.set_attribute("llm.system_prompt_length", len(system_prompt))
            span.set_attribute("llm.user_query_length", len(user_query))
            span.set_attribute("llm.messages_count", len(messages))
            
            initial_response = await llm.ainvoke(messages)
            
            span.set_attribute("llm.response_length", len(initial_response.content))
            span.set_attribute("llm.response_preview", initial_response.content[:300] + "...")
            print(f"📋 Reasoning Model Antwort erhalten: {len(initial_response.content)} Zeichen")
        
        # Schritt 2: Extrahiere Suchanfragen aus der Antwort
        with tracer.start_as_current_span("Extract and Prepare Search Queries") as span:
            search_queries = []
            
            # Parse strukturierte Suchanfragen
            lines = initial_response.content.split('\n')
            for line in lines:
                if line.strip() and (line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '-', '*'))):
                    query = re.sub(r'^\d+\.\s*', '', line.strip())
                    query = re.sub(r'^[-*]\s*', '', query.strip())
                    if query and len(query) > 3:
                        search_queries.append(query)
            
            # Fallback: Parse Channel Tags falls vorhanden
            channel_searches = parse_channel_tags_for_searches(initial_response.content)
            for search in channel_searches:
                if search["type"] == "general":
                    search_queries.append(search["query"])
                elif search["type"] == "specific":
                    search_queries.append(f"{search['gesetz']} {search['paragraph']}")
            
            # Standard-Suchen falls keine gefunden
            if not search_queries:
                search_queries = [
                    "EStG Unterhalt volljährige Kinder Ausbildung",
                    "Kindergeld Kinderfreibetrag Ausbildung",
                    "BAföG steuerlich Unterhalt",
                    "Werbungskosten Studium Eltern",
                    "EStG §33a außergewöhnliche Belastungen"
                ]
            
            span.set_attribute("search_queries_count", len(search_queries))
            span.set_attribute("search_queries_planned", json.dumps(search_queries[:5]))
            span.set_attribute("fallback_queries_used", len(search_queries) == 5 and search_queries[0] == "EStG Unterhalt volljährige Kinder Ausbildung")
            print(f"🔍 Führe {len(search_queries)} Suchen durch...")
        
        # Schritt 3: Führe alle Suchen durch
        with tracer.start_as_current_span("Execute All Legal Database Searches") as span:
            all_search_results = []
            searches_to_execute = min(len(search_queries), 5)
            span.set_attribute("total_searches_planned", searches_to_execute)
            
            for i, query in enumerate(search_queries[:5], 1):  # Maximal 5 Suchen
                print(f"\n--- Suche {i}/{searches_to_execute}: {query} ---")
                
                search_info = {"type": "general", "query": query}
                result = await execute_search(search_info)
                all_search_results.append(f"**Suche {i}: {query}**\n{result}")
            
            span.set_attribute("searches_completed", len(all_search_results))
            span.set_attribute("total_search_results_length", sum(len(r) for r in all_search_results))
        
        # Schritt 4: Finale Analyse mit allen Suchergebnissen
        print("\n🧠 Erstelle finale rechtliche Analyse...")
        
        with tracer.start_as_current_span("Final Comprehensive Legal Analysis") as span:
            final_system_prompt = """Du bist ein erfahrener deutscher Rechtsanwalt, spezialisiert auf Steuerrecht.

Basierend auf den folgenden Suchergebnissen aus der LEXinform-Datenbank, erstelle eine umfassende rechtliche Analyse der ursprünglichen Frage.

Struktur deiner Antwort:
1. **Zusammenfassung der Rechtslage**
2. **Steuerliche Behandlung für den Vater**
3. **Steuerliche Behandlung für das Kind**
4. **Praktische Empfehlungen**
5. **Erforderliche Nachweise**
6. **Quellenangaben** (mit Datensatz-IDs)

Verwende die spezifischen Datensatz-IDs aus den Suchergebnissen für deine Zitate."""

            final_content = f"Ursprüngliche Frage: {user_query}\n\nSuchergebnisse:\n\n" + "\n\n".join(all_search_results)
            
            final_messages = [
                SystemMessage(content=final_system_prompt),
                HumanMessage(content=final_content)
            ]
            
            span.set_attribute("final_system_prompt_length", len(final_system_prompt))
            span.set_attribute("final_content_length", len(final_content))
            span.set_attribute("final_messages_count", len(final_messages))
            
            final_response = await llm.ainvoke(final_messages)
            
            span.set_attribute("final_response_length", len(final_response.content))
            span.set_attribute("searches_performed", len(search_queries))
            span.set_attribute("research_end_time", datetime.now().isoformat())
        
        return final_response.content

# Main application
async def main():
    """Hauptanwendung für umfassende Rechtsrecherche mit vollständigem Phoenix Tracing"""
    
    print("=" * 80)
    print("🏛️  LEXinform Rechtsrecherche-System (Vollständiges Tracing - Fixed)")
    print("=" * 80)
    print(f"🤖 KI-Modell: {OPENAI_COMPATIBLE_MODEL}")
    print(f"🔗 Endpoint: {OPENAI_COMPATIBLE_BASE_URL}")
    print(f"🔍 Elasticsearch: {ELASTIC_URL}/{ELASTIC_INDEX}")
    print("📊 Phoenix Tracing: http://localhost:6006")
    print("🔧 Umfassendes LLM + Search Tracing aktiviert")
    print()
    print("Verfügbare Befehle:")
    print("  - Rechtsfrage eingeben für umfassende Analyse")
    print("  - 'exit' zum Beenden")
    print("=" * 80)
    print()
    
    while True:
        try:
            user_input = input("Rechtsfrage> ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye", "beenden"]:
                print("Auf Wiedersehen! 👋")
                break
            
            if not user_input:
                continue
            
            print(f"\n🧠 Analysiere Rechtsfrage: {user_input[:100]}...")
            print("🔍 Starte umfassende Rechtsrecherche mit vollständigem Tracing...\n")
            
            # Führe umfassende Rechtsrecherche durch
            result = await comprehensive_legal_research(user_input)
            
            print("\n" + "=" * 80)
            print("📋 RECHTLICHE ANALYSE:")
            print("=" * 80)
            print(result)
            print("=" * 80)
            
            print(f"\n📊 Vollständige Phoenix Traces: http://localhost:6006")
            print("   🤖 LLM Generierungen (Start/End mit Details)")
            print("   🔍 Elasticsearch Suchen (mit Record IDs)")
            print("   🏛️ Kompletter Research-Workflow")
            print("   📈 Performance-Metriken")
            print()
            
        except KeyboardInterrupt:
            print("\n\nAuf Wiedersehen! 👋")
            break
        except Exception as e:
            print(f"\n❌ Fehler bei der Rechtsrecherche: {str(e)}")
            print("Bitte versuchen Sie es mit einer anderen Rechtsfrage.\n")

if __name__ == "__main__":
    # Set environment variables
    os.environ["ELASTIC_URL"] = ELASTIC_URL
    os.environ["ELASTIC_INDEX"] = ELASTIC_INDEX
    
    print("Überprüfe Systemverbindungen...")
    
    # Test Phoenix
    try:
        response = requests.get("http://localhost:6006/health", timeout=5)
        if response.status_code == 200:
            print("✅ Phoenix läuft auf http://localhost:6006")
        else:
            print("⚠️ Phoenix-Verbindung problematisch")
    except:
        print("❌ Phoenix nicht erreichbar")
    
    # Test Elasticsearch
    try:
        response = requests.get(f"{ELASTIC_URL}/_cluster/health", timeout=5)
        if response.status_code == 200:
            print("✅ Elasticsearch verbunden")
        else:
            print("⚠️ Elasticsearch-Verbindung problematisch")
    except:
        print("❌ Elasticsearch nicht erreichbar")
    
    # Test LLM endpoint
    try:
        test_response = requests.post(
            f"{OPENAI_COMPATIBLE_BASE_URL}/chat/completions",
            json={
                "model": OPENAI_COMPATIBLE_MODEL,
                "messages": [{"role": "user", "content": "Test"}],
                "max_tokens": 10
            },
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        if test_response.status_code == 200:
            print("✅ KI-Modell verbunden")
        else:
            print("⚠️ KI-Modell-Verbindung problematisch")
    except:
        print("❌ KI-Modell nicht erreichbar")
    
    print()
    
    # Run the application
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSystem beendet. Auf Wiedersehen!")
    except Exception as e:
        print(f"Systemfehler: {e}")
