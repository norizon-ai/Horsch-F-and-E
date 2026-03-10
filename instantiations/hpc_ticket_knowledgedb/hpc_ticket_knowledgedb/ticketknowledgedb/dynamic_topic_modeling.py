import json
import pandas as pd
import numpy as np
from datetime import datetime
from bertopic import BERTopic
import plotly.graph_objects as go
from tqdm import tqdm
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
import re

def clean_text(text):
    """Clean text by removing unwanted patterns"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    
    # Remove numbers and number-word combinations (like ticket numbers)
    text = re.sub(r'\b\d+\w*\b|\b\w*\d+\b', '', text)
    
    # Remove special characters and extra whitespace
    text = re.sub(r'[^\w\s]', ' ', text)
    text = ' '.join(text.split())
    
    return text

# Load and prepare data
def load_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return data

# Load the data
print("Loading data...")
tickets = load_jsonl('total_tickets.jsonl')

# Extract first messages and timestamps
texts = []
timestamps = []

for ticket in tickets:
    if 'conversations' in ticket and ticket['conversations'] and len(ticket['conversations']) > 0:
        first_message = ticket['conversations'][0]
        if 'content' in first_message and 'CreateTime' in first_message:
            # Skip empty content
            content = first_message['content']
            if not content or not isinstance(content, str):
                continue
            
            # Clean and add title to content if available
            if 'Title' in ticket and ticket['Title']:
                title = clean_text(ticket['Title'])
                content = clean_text(content)
                # Add cleaned title with more weight by repeating it
                content = f"Title: {title}\n{title}\n{title}\n\nContent: {content}"
                
            texts.append(content)
            # Convert timestamp to datetime
            try:
                timestamp = datetime.strptime(first_message['CreateTime'], '%Y-%m-%d %H:%M:%S')
                timestamps.append(timestamp)
            except (ValueError, TypeError):
                continue

# Filter data from 2014 onwards
data_2014 = [(text, ts) for text, ts in zip(texts, timestamps) if ts.year >= 2014]
if data_2014:
    texts = [item[0] for item in data_2014]
    timestamps = [item[1] for item in data_2014]
else:
    print("No data found from 2014 onwards!")
    exit(1)

print(f"Total number of tickets from 2014 onwards: {len(texts)}")

# Define custom stop words (common words that don't add meaning)
custom_stop_words = [
    # Email/formal words
    'dear', 'hello', 'hi', 'thanks', 'thank', 'you', 'regards', 'best', 'greetings',
    'please', 'would', 'could', 'sincerely', 'cheers', 'kind', 'best', 'wishes',
    'phone', 'tel', 'email', 'mail', 'address', 'fax', 'www', 'http', 'https',
    
    # Institution words
    'university', 'department', 'institute', 'faculty', 'lehrstuhl', 'fau',
    'erlangen', 'nürnberg', 'juelich', 'uni', 'office',
    
    # Common German words
    'ich', 'sie', 'und', 'mit', 'der', 'die', 'das', 'ist', 'für', 'auf',
    'zusammengeführt', 'ticket', 'wurde', 'bitte', 'können', 'möchte',
    
    # Common names and locations
    'schulze', 'eicker', 'bunlong', 'stefan', 'turowski', 'eckstein',
    'audiolabs', 'physics', 'materials',
    
    # Technical common words
    'host', 'message', 'attached', 'file', 'files', 'error', 'warning',
    'running', 'output', 'input', 'version', 'using', 'used', 'use',
    'number', 'time', 'date', 'day', 'week', 'month', 'year'
]

# Configure CountVectorizer with custom stop words and token pattern
vectorizer_model = CountVectorizer(
    stop_words=custom_stop_words,
    token_pattern=r'(?u)\b[a-zA-Z]{3,}\b',  # Only words with 3+ characters
    max_df=0.9,  # Remove terms that appear in more than 90% of documents
    min_df=5,    # Remove terms that appear in fewer than 5 documents
)

# Configure UMAP for more detailed topic separation
umap_model = UMAP(
    n_neighbors=15,         # Fewer neighbors for more local structure
    n_components=20,        # More components for finer separation
    min_dist=0.05,         # Smaller min_dist for tighter clusters
    metric='cosine',        # Cosine similarity works well with text
    random_state=42
)

# Configure HDBSCAN for finer clustering
hdbscan_model = HDBSCAN(
    min_cluster_size=20,    # Smaller minimum cluster size
    min_samples=5,          # Less conservative clustering
    cluster_selection_method='eom',  # Better for varying density clusters
    metric='euclidean',
    prediction_data=True
)

# Configure CountVectorizer for better topic representation
vectorizer_model = CountVectorizer(
    stop_words=custom_stop_words,
    token_pattern=r'(?u)\b[a-zA-Z]{3,}\b',  # Only words with 3+ characters
    min_df=5,     # Remove terms that appear in fewer than 5 documents
    max_df=0.7    # Remove terms that appear in more than 70% of documents
)

# Create and train BERTopic model with parameters for more detailed topics
print("Training BERTopic model...")
topic_model = BERTopic(
    # Embedding model parameters
    embedding_model='all-MiniLM-L6-v2',
    
    # Dimensionality reduction
    umap_model=umap_model,
    min_topic_size=20,      # Smaller minimum topic size
    
    # Clustering
    hdbscan_model=hdbscan_model,
    
    # Vectorizer with custom stop words
    vectorizer_model=vectorizer_model,
    
    # Topic representation
    top_n_words=15,         # Show more words per topic
    
    # Calculate probabilities
    calculate_probabilities=True,
    
    # Verbose output
    verbose=True
)

# Fit the model and transform documents
topics, probs = topic_model.fit_transform(texts)

# Reduce topics by merging similar ones and removing outliers
print("\nReducing and merging similar topics...")
topic_model.reduce_topics(texts, nr_topics=50)  # Increased number of topics

# Update topic labels with more descriptive names
topic_model.update_topics(texts, top_n_words=20)

# Generate topics over time
print("Generating topics over time...")
topics_over_time = topic_model.topics_over_time(
    texts, 
    timestamps,
    global_tuning=True,
    evolution_tuning=True,
    nr_bins=20
)

# Visualize topics over time
print("Creating visualization...")
# Get actual number of topics (excluding -1 for outliers)
num_topics = len(topic_model.get_topic_info()[topic_model.get_topic_info()['Topic'] != -1])

# Create visualization with enhanced settings
fig = topic_model.visualize_topics_over_time(
    topics_over_time,
    top_n_topics=num_topics,
    width=1200,          # Wider plot
    height=800,          # Taller plot
    title="Topic Evolution Over Time (2014-Present)"
)

# Update layout for better readability
fig.update_layout(
    showlegend=True,
    legend=dict(
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.02,  # Position legend outside the plot
        bgcolor="rgba(255, 255, 255, 0.9)",  # Semi-transparent background
        bordercolor="rgba(0, 0, 0, 0.2)",
        borderwidth=1
    ),
    margin=dict(t=50, l=50, r=150, b=50)  # Increased right margin to accommodate legend
)

# Save the enhanced visualization
fig.write_html("dynamic_topics_visualization.html")

# Get detailed topic info
print("Generating detailed topic analysis...")

# Create HTML report content
report_html = """
<div style='max-width: 1200px; margin: 40px auto; padding: 20px; font-family: Arial, sans-serif;'>
    <h1 style='color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px;'>Topic Analysis Report</h1>
    <p style='color: #34495e; font-size: 1.1em;'>Analysis of ticket conversations from 2014 onwards. Total tickets analyzed: {total_tickets}</p>
    
    <h2 style='color: #2c3e50; margin-top: 30px;'>Topic Overview</h2>
    <p style='color: #34495e;'>Found {num_topics} main topics in the conversations. Each topic is characterized by its most representative terms and example tickets.</p>
    
    <div id='topic-details'>
""".format(total_tickets=len(texts), num_topics=len(topic_model.get_topic_info()))

# Get topic information
topic_info = topic_model.get_topic_info()
top_topics = topic_info[topic_info['Topic'] != -1]  # Exclude outlier topic
representative_docs = topic_model.get_representative_docs()

for topic in top_topics['Topic']:
    # Get topic words and their weights
    words_weights = topic_model.get_topic(topic)
    if not words_weights:  # Skip if no words found
        continue
        
    sorted_words = words_weights[:15]  # Already sorted by weight
    
    # Get example documents
    examples = representative_docs.get(topic, [])[:3]  # Get up to 3 examples
    
    # Calculate topic size and percentage
    topic_size = topic_info[topic_info['Topic'] == topic]['Count'].values[0]
    topic_percentage = (topic_size / len(texts)) * 100
    
    # Add topic section to report
    report_html += f"""

        <div class='topic-section' style='margin: 30px 0; padding: 20px; background: #f8f9fa; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <h3 style='color: #2c3e50; margin-bottom: 15px;'>Topic {topic} ({topic_size} tickets, {topic_percentage:.1f}%)</h3>
            
            <h4 style='color: #34495e;'>Key Terms:</h4>
            <div style='display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;'>
    """
    
    # Add word weights
    for word, weight in sorted_words:  # Already limited to top 15
        weight_percent = float(weight) * 100
        report_html += f"""
                <div style='background: #3498db; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;'>
                    {word} ({weight_percent:.1f}%)
                </div>
        """
    
    report_html += """

            </div>
            
            <h4 style='color: #34495e;'>Example Tickets:</h4>
            <div class='examples' style='margin-top: 10px;'>
    """
    
    # Add example documents
    for i, example in enumerate(examples, 1):
        # Clean example text for display
        clean_example = example.replace('<', '&lt;').replace('>', '&gt;')
        
        # Extract title and content
        parts = clean_example.split('\n\nContent: ')
        if len(parts) == 2:
            title = parts[0].replace('Title: ', '').split('\n')[0]  # Get only first occurrence of title
            content = parts[1]
            if len(content) > 300:
                content = content[:300] + '...'
            
            clean_example = f"<strong>Title:</strong> {title}<br><strong>Content:</strong> {content}"
            
        report_html += f"""

                <div class='example' style='margin: 10px 0; padding: 15px; background: white; border-left: 4px solid #3498db; border-radius: 4px;'>
                    <strong>Example {i}:</strong><br>
                    <p style='margin: 10px 0; color: #34495e;'>{clean_example}</p>
                </div>
        """
    
    report_html += """

            </div>
        </div>
    """

report_html += """

    </div>
</div>
"""

# Read the existing visualization HTML
print("Merging report with visualization...")
with open('dynamic_topics_visualization.html', 'r', encoding='utf-8') as f:
    viz_html = f.read()

# Insert our report before the closing body tag
final_html = viz_html.replace('</body>', f'{report_html}</body>')

# Save the combined visualization and report
with open('dynamic_topics_visualization.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Done! Open dynamic_topics_visualization.html to view the results.")
