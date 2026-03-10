import os
import glob
import numpy as np
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import re

def read_markdown_files(directory):
    """Read all markdown files from the knowledgebase directory."""
    markdown_files = glob.glob(os.path.join(directory, "*.md"))
    documents = []
    filenames = []
    timestamps = []
    
    for file_path in markdown_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            documents.append(content)
            filenames.append(os.path.basename(file_path))
            
            # Try to extract timestamp from filename (assuming YYYYMMDD format)
            timestamp_match = re.search(r'(\d{8})', os.path.basename(file_path))
            if timestamp_match:
                # Convert to datetime object
                try:
                    date_str = timestamp_match.group(1)
                    timestamps.append(pd.to_datetime(date_str, format='%Y%m%d'))
                except ValueError:
                    timestamps.append(pd.NaT)
            else:
                timestamps.append(pd.NaT)
    
    return documents, filenames, timestamps

def create_output_directory():
    """Create directory for analysis outputs."""
    output_dir = "ticket_analysis"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def save_topic_analysis(topic_model, docs, timestamps, output_dir):
    """Generate and save various topic analysis visualizations."""
    # 1. Topic Word Scores Visualization
    try:
        topic_word_scores = topic_model.visualize_topics()
        topic_word_scores.write_html(f"{output_dir}/topic_word_scores.html")
    except Exception as e:
        print(f"Warning: Could not generate topic word scores visualization: {e}")
    
    # 2. Topic Evolution Visualization
    try:
        # Get valid timestamps and corresponding documents
        valid_indices = [i for i, ts in enumerate(timestamps) if pd.notna(ts)]
        
        if valid_indices:
            valid_docs = [docs[i] for i in valid_indices]
            valid_timestamps = [timestamps[i] for i in valid_indices]
            
            # Get topics over time using BERTopic's built-in method
            topics_over_time = topic_model.topics_over_time(
                valid_docs,
                valid_timestamps,
                nr_bins=20,  # Adjust number of time bins
                evolution_tuning=0.6  # Adjust smoothing
            )
            
            # Create the visualization
            topic_evolution = topic_model.visualize_topics_over_time(
                topics_over_time,
                top_n_topics=10  # Show top 10 topics for clarity
            )
            topic_evolution.write_html(f"{output_dir}/topic_evolution.html")
        else:
            print("Warning: No valid timestamps found for topic evolution visualization")
    except Exception as e:
        print(f"Warning: Could not generate topic evolution visualization: {e}")
    
    # 3. Hierarchical Topic Tree
    try:
        topic_hierarchy = topic_model.visualize_hierarchy()
        topic_hierarchy.write_html(f"{output_dir}/topic_hierarchy.html")
    except Exception as e:
        print(f"Warning: Could not generate topic hierarchy visualization: {e}")
    
    # 4. Topic Similarity Heatmap
    try:
        topic_similarity = topic_model.visualize_heatmap()
        topic_similarity.write_html(f"{output_dir}/topic_similarity.html")
    except Exception as e:
        print(f"Warning: Could not generate topic similarity visualization: {e}")
    
    # 5. Topic Distribution
    try:
        topic_distr = topic_model.visualize_barchart()
        topic_distr.write_html(f"{output_dir}/topic_distribution.html")
    except Exception as e:
        print(f"Warning: Could not generate topic distribution visualization: {e}")

def analyze_topic_quality(topic_model, docs):
    """Analyze topic quality metrics."""
    # Calculate topic diversity (unique words across topics)
    all_words = set()
    total_words = 0
    word_freq = {}
    
    topics = topic_model.get_topics()
    for topic_id in topics:
        topic_words = topics[topic_id]
        if topic_words:  # Check if topic has words
            words = [word for word, _ in topic_words]
            all_words.update(words)
            total_words += len(words)
            
            # Count word frequencies across topics
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # Calculate metrics
    diversity = len(all_words) / total_words if total_words > 0 else 0
    
    # Calculate average word frequency (lower is better - means words are more unique to topics)
    avg_word_freq = sum(word_freq.values()) / len(word_freq) if word_freq else 0
    
    # Calculate topic sizes
    topic_sizes = topic_model.get_topic_info()['Count']
    avg_size = topic_sizes.mean()
    size_std = topic_sizes.std()
    
    return {
        'diversity': diversity,
        'avg_word_freq': avg_word_freq,
        'avg_topic_size': avg_size,
        'topic_size_std': size_std,
        'total_topics': len(topic_model.get_topics())
    }

def generate_report(topic_model, quality_metrics, output_dir):
    """Generate a comprehensive analysis report."""
    report = []
    report.append("# HPC Support Ticket Analysis Report")
    report.append(f"\nAnalysis generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Topic Model Overview
    report.append("\n## Topic Model Overview")
    topic_info = topic_model.get_topic_info()
    report.append(f"\nTotal number of topics: {quality_metrics['total_topics']}")
    report.append(f"Documents per topic (avg): {quality_metrics['avg_topic_size']:.1f}")
    report.append(f"Documents per topic (std): {quality_metrics['topic_size_std']:.1f}")
    
    # Quality Metrics
    report.append("\n## Model Quality Metrics")
    report.append(f"\nTopic diversity: {quality_metrics['diversity']:.3f} (higher is better)")
    report.append(f"Average word frequency: {quality_metrics['avg_word_freq']:.2f} (lower is better)")
    report.append("\nThese metrics indicate how well-separated and distinct the topics are.")
    
    # Complete Topic Analysis
    report.append("\n## Complete Topic Analysis")
    report.append("\nTopics are sorted by size (number of documents). For each topic, showing:")
    report.append("1. Number of documents in the topic")
    report.append("2. Top keywords with their importance scores")
    report.append("3. Representative document examples")
    
    # Get all topics sorted by size
    topics = topic_model.get_topics()
    topic_info = topic_info.sort_values('Count', ascending=False)
    
    # First, handle the outlier topic if it exists
    outlier_row = topic_info[topic_info['Topic'] == -1]
    if not outlier_row.empty:
        report.append(f"\n### Outlier Documents: {outlier_row.iloc[0]['Count']} documents")
        report.append("These documents didn't fit well into any specific topic.")
    
    # Then handle all other topics
    for _, row in topic_info[topic_info['Topic'] != -1].iterrows():
        topic_id = row['Topic']
        topic_words = topics[topic_id]
        if topic_words:
            # Get word scores and format them
            word_scores = [(word, score) for word, score in topic_words[:15]]  # Top 15 words
            words_str = "\n".join([f"- {word} (importance: {score:.3f})" for word, score in word_scores])
            
            # Get representative documents
            try:
                docs = topic_model.get_representative_docs(topic_id)
                doc_examples = "\n".join([f"- {doc[:100]}..." for doc in docs[:3]])
            except:
                doc_examples = "No representative documents available"
            
            report.append(f"\n### Topic {topic_id}: {row['Count']} documents")
            report.append("\nTop keywords and their importance scores:")
            report.append(words_str)
            report.append("\nExample documents:")
            report.append(doc_examples)
    
    # Topic Size Distribution
    report.append("\n## Topic Size Distribution")
    report.append("\nNumber of documents per topic range:")
    bins = [0, 10, 50, 100, 500, float('inf')]
    labels = ['1-10', '11-50', '51-100', '101-500', '500+']
    topic_sizes = pd.cut(topic_info['Count'], bins=bins, labels=labels)
    size_dist = topic_sizes.value_counts().sort_index()
    for label, count in size_dist.items():
        report.append(f"- {label} documents: {count} topics")
    
    # Write report
    with open(f"{output_dir}/analysis_report.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

def main():
    # Read documents
    print("Reading markdown files...")
    docs, filenames, timestamps = read_markdown_files("knowledgebase")
    output_dir = create_output_directory()
    
    print("Creating topic model...")
    # Custom vectorizer with extended n-gram range
    vectorizer = CountVectorizer(stop_words="english", 
                               ngram_range=(1, 2),  # Include bigrams
                               max_features=10000)
    
    # Initialize topic model with optimized parameters
    topic_model = BERTopic(
        # Embedding model parameters
        embedding_model="all-MiniLM-L6-v2",  # Lightweight but effective model
        
        # Topic representation
        vectorizer_model=vectorizer,
        min_topic_size=5,
        nr_topics="auto",  # Let the model determine optimal number
        
        # Dimensionality reduction
        umap_model=UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric='cosine'),
        
        # Verbose output
        verbose=True
    )
    
    # Fit the model
    topics, probs = topic_model.fit_transform(docs)
    
    print("\nGenerating visualizations...")
    save_topic_analysis(topic_model, docs, timestamps, output_dir)
    
    print("Calculating quality metrics...")
    quality_metrics = analyze_topic_quality(topic_model, docs)
    
    print("Generating report...")
    generate_report(topic_model, quality_metrics, output_dir)
    
    print(f"\nAnalysis complete! Results have been saved to the '{output_dir}' directory.")
    print("\nGenerated files:")
    print("1. topic_word_scores.html - Interactive visualization of word scores per topic")
    print("2. topic_evolution.html - Topic evolution over time")
    print("3. topic_hierarchy.html - Hierarchical clustering of topics")
    print("4. topic_similarity.html - Topic similarity heatmap")
    print("5. topic_distribution.html - Distribution of documents across topics")
    print("6. analysis_report.md - Comprehensive analysis report")
    
    print("\nSuggested next steps:")
    print("1. Review the visualizations and report")
    print("2. Adjust parameters based on the following aspects:")
    print("   - If topics are too broad: decrease nr_topics or increase min_topic_size")
    print("   - If topics are too specific: increase nr_topics or decrease min_topic_size")
    print("   - If topics have low coherence: adjust vectorizer parameters or try different embedding models")
    print("3. Iterate with different parameters to find the optimal configuration")

if __name__ == "__main__":
    main()
