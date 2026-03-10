#!/usr/bin/env python3
"""
Generate fictional Confluence pages based on a structure file using OpenAI.
Creates realistic German technical documentation for TechMech Solutions GmbH.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
import argparse
from openai import OpenAI


class ConfluencePage:
    """Represents a single Confluence page."""

    def __init__(self, title: str, space: str, parent: Optional[str] = None, level: int = 0):
        self.title = title
        self.space = space
        self.parent = parent
        self.level = level
        self.content = ""
        self.filename = self._sanitize_filename(title)

    @staticmethod
    def _sanitize_filename(title: str) -> str:
        """Convert page title to valid filename."""
        # Remove version numbers and special chars, keep German umlauts
        filename = re.sub(r'[<>:"/\\|?*]', '', title)
        filename = filename.replace(' ', '_')
        # Limit length
        if len(filename) > 100:
            filename = filename[:100]
        return filename + '.md'


class ConfluenceStructureParser:
    """Parses the confluence structure markdown file."""

    def __init__(self, structure_file: Path):
        self.structure_file = structure_file
        self.pages: List[ConfluencePage] = []
        self.current_space = ""
        self.current_space_code = ""

    def parse(self) -> List[ConfluencePage]:
        """Parse the structure file and extract all pages."""
        with open(self.structure_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        parent_stack = []

        for line in lines:
            line = line.rstrip()

            # Skip empty lines and separators
            if not line or line.strip().startswith('---'):
                continue

            # Check for space definition (## Space X: NAME (CODE))
            space_match = re.match(r'^## Space \d+: (.+?) \(([A-Z]+)\)', line)
            if space_match:
                self.current_space = space_match.group(1)
                self.current_space_code = space_match.group(2)
                parent_stack = []
                # Add space home page
                page = ConfluencePage(
                    title=f"{self.current_space} - Home",
                    space=self.current_space_code,
                    parent=None,
                    level=0
                )
                self.pages.append(page)
                continue

            # Skip metadata lines
            if line.startswith('**Space-Beschreibung**'):
                continue

            # Parse section headers (###, ####, etc.)
            header_match = re.match(r'^(#{3,})\s+(.+)', line)
            if header_match:
                level = len(header_match.group(1)) - 2  # Convert ### to level 1
                title = header_match.group(2).strip()

                # Remove markdown bold
                title = re.sub(r'\*\*(.+?)\*\*', r'\1', title)

                # Update parent stack
                while len(parent_stack) >= level:
                    parent_stack.pop()

                parent = parent_stack[-1] if parent_stack else f"{self.current_space} - Home"

                page = ConfluencePage(
                    title=title,
                    space=self.current_space_code,
                    parent=parent,
                    level=level
                )
                self.pages.append(page)
                parent_stack.append(title)
                continue

            # Parse bullet point pages
            bullet_match = re.match(r'^(\s*)[-*]\s+(.+)', line)
            if bullet_match:
                indent = len(bullet_match.group(1))
                title = bullet_match.group(2).strip()

                # Remove markdown bold
                title = re.sub(r'\*\*(.+?)\*\*', r'\1', title)

                # Calculate level based on indentation
                level = (indent // 2) + len(parent_stack)

                parent = parent_stack[-1] if parent_stack else f"{self.current_space} - Home"

                page = ConfluencePage(
                    title=title,
                    space=self.current_space_code,
                    parent=parent,
                    level=level
                )
                self.pages.append(page)

        return self.pages


class ContentGenerator:
    """Generates realistic content for Confluence pages using OpenAI."""

    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.company_context = """
TechMech Solutions GmbH ist ein mittelständisches deutsches Unternehmen im Bereich
Automatisierungstechnik und Sondermaschineninbau. Das Unternehmen entwickelt und baut
Roboterzellen, Fördertechnik und Qualitätsprüfsysteme für verschiedene Branchen
(Automotive, Lebensmittel, Pharma, etc.).
"""

    def generate_content(self, page: ConfluencePage) -> str:
        """Generate realistic German content for a Confluence page."""

        prompt = f"""Du bist ein technischer Redakteur für {self.company_context}

Erstelle einen realistischen Confluence-Seiteninhalt für folgende Seite:

Titel: {page.title}
Space: {page.space}
Übergeordnete Seite: {page.parent}

Die Seite sollte:
- In professionellem Deutsch geschrieben sein
- Technisch detailliert und realistisch sein
- Typische Confluence-Formatierung verwenden (Überschriften, Listen, Tabellen)
- Zwischen 200-500 Wörter lang sein
- Relevante technische Details, Spezifikationen oder Prozessbeschreibungen enthalten
- Bei Bedarf realistische Beispieldaten, Messwerte oder Konfigurationen enthalten

Schreibe NUR den Seiteninhalt, keine Metadaten oder Erklärungen.
"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Du bist ein technischer Redakteur für technische Dokumentation."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            content = response.choices[0].message.content
            return content.strip()

        except Exception as e:
            print(f"Error generating content for '{page.title}': {e}")
            return f"# {page.title}\n\n*Inhalt wird noch erstellt...*"


class ConfluenceExporter:
    """Exports generated pages to a folder structure."""

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        # Create output directory immediately
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._created_spaces = set()

    def write_page(self, page: ConfluencePage):
        """Write a single page to disk immediately."""
        # Ensure space directory exists
        space_dir = self.output_dir / page.space
        if page.space not in self._created_spaces:
            space_dir.mkdir(exist_ok=True)
            self._created_spaces.add(page.space)

        # Create page file with metadata
        page_content = self._format_page(page)
        page_file = space_dir / page.filename

        with open(page_file, 'w', encoding='utf-8') as f:
            f.write(page_content)

        return f"{page.space}/{page.filename}"

    @staticmethod
    def _format_page(page: ConfluencePage) -> str:
        """Format page with metadata and content."""
        metadata = f"""---
title: {page.title}
space: {page.space}
parent: {page.parent or 'None'}
level: {page.level}
---

"""
        return metadata + page.content


def main():
    parser = argparse.ArgumentParser(
        description='Generate fictional Confluence pages for demo purposes'
    )
    parser.add_argument(
        '--structure',
        type=Path,
        default=Path(__file__).parent / 'confluence_structure.md',
        help='Path to confluence structure file'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path(__file__).parent / 'generated_confluence',
        help='Output directory for generated pages'
    )
    parser.add_argument(
        '--api-key',
        required=True,
        help='OpenAI API key'
    )
    parser.add_argument(
        '--model',
        default='gpt-4o-mini',
        help='OpenAI model to use (default: gpt-4o-mini)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of pages to generate (for testing)'
    )

    args = parser.parse_args()

    print("🚀 Confluence Demo Generator")
    print("=" * 50)
    print(f"Structure file: {args.structure}")
    print(f"Output directory: {args.output}")
    print(f"OpenAI model: {args.model}")
    print()

    # Parse structure
    print("📖 Parsing confluence structure...")
    parser_obj = ConfluenceStructureParser(args.structure)
    pages = parser_obj.parse()

    if args.limit:
        pages = pages[:args.limit]

    print(f"✓ Found {len(pages)} pages to generate")
    print()

    # Initialize exporter (creates output directory)
    exporter = ConfluenceExporter(args.output)

    # Generate content and write immediately
    print("🤖 Generating and writing content...")
    generator = ContentGenerator(args.api_key, args.model)

    for i, page in enumerate(pages, 1):
        print(f"[{i}/{len(pages)}] Generating: {page.title}")

        # Generate content
        page.content = generator.generate_content(page)

        # Write immediately to disk
        file_path = exporter.write_page(page)
        print(f"           ✓ Saved: {file_path}")

    print()
    print("=" * 50)
    print(f"✅ Success! Generated {len(pages)} pages")
    print(f"📁 Output directory: {args.output}")
    print()
    print("You can now use these files with your Confluence connector demo!")


if __name__ == '__main__':
    main()
