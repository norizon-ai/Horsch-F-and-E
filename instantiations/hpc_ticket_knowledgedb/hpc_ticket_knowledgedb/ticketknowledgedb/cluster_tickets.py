import os
import glob
import re
from bertopic import BERTopic
import pandas as pd
from pathlib import Path
import shutil

def read_markdown_files(directory):
    """Read all markdown files from the knowledgebase directory."""
    markdown_files = glob.glob(os.path.join(directory, "*.md"))
    documents = []
    filenames = []
    
    for file_path in markdown_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            documents.append(content)
            filenames.append(os.path.basename(file_path))
    
    return documents, filenames

def create_topic_directory(base_dir, clean=True):
    """Create or clean the topic directory."""
    topic_dir = os.path.join(base_dir, "topic_clusters")
    if clean and os.path.exists(topic_dir):
        shutil.rmtree(topic_dir)
    os.makedirs(topic_dir, exist_ok=True)
    return topic_dir

def sanitize_topic_name(name):
    """Convert topic name to a valid filename."""
    # Remove invalid filename characters and trim
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip()
    # Ensure the filename isn't too long
    return name[:100] if len(name) > 100 else name

def main():
    # Read all markdown files
    print("Reading markdown files...")
    docs, filenames = read_markdown_files("knowledgebase")
    total_input_files = len(filenames)
    print(f"Found {total_input_files} input files")
    
    # Create and train the topic model
    print("Training BERTopic model...")
    topic_model = BERTopic(nr_topics=50, min_topic_size=5, verbose=True)
    topics, probs = topic_model.fit_transform(docs)
    
    # Verify all documents were assigned topics
    total_assigned = len(topics)
    if total_assigned != total_input_files:
        print(f"WARNING: Number of assigned topics ({total_assigned}) doesn't match number of input files ({total_input_files})")
    
    # Get topic information
    topic_info = topic_model.get_topic_info()
    print("\nTop topics found:")
    print(topic_info.head(10))
    
    # Create topic clusters directory
    topic_dir = create_topic_directory(".")
    
    # Create a mapping of documents to topics
    doc_topic_mapping = pd.DataFrame({
        'Filename': filenames,
        'Topic': topics,
        'Content': docs
    })
    
    # Save documents by topic
    print("\nSaving documents by topic...")
    total_saved = 0
    for topic_id in topic_info['Topic']:
        if topic_id == -1:  # Include outlier topic - we want to keep all documents
            topic_words = "outliers_miscellaneous"
        else:
            topic_words = "_".join([word for word, _ in topic_model.get_topic(topic_id)][:5])
            
        # Get topic name and documents
        topic_docs = doc_topic_mapping[doc_topic_mapping['Topic'] == topic_id]
        topic_name = f"topic_{topic_id}_{topic_words}"
        topic_name = sanitize_topic_name(topic_name)
        total_saved += len(topic_docs)
        
        # Create topic file
        output_file = os.path.join(topic_dir, f"{topic_name}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write topic header
            f.write(f"# Topic {topic_id}: {topic_words}\n\n")
            f.write(f"Number of tickets: {len(topic_docs)}\n\n")
            f.write("## Tickets in this topic:\n\n")
            
            # Write each document
            for _, row in topic_docs.iterrows():
                f.write(f"### {row['Filename']}\n")
                f.write(row['Content'])
                f.write("\n---\n\n")
        
        print(f"Created {topic_name}.md with {len(topic_docs)} tickets")
    
    # Save topic model information
    topic_info.to_csv(os.path.join(topic_dir, "topic_info.csv"), index=False)
    
    # Final verification
    print(f"\nVerification Summary:")
    print(f"Total input files: {total_input_files}")
    print(f"Total files assigned to topics: {total_assigned}")
    print(f"Total files saved: {total_saved}")
    
    if total_saved != total_input_files:
        print(f"WARNING: Some files may have been lost! {total_input_files - total_saved} files are missing!")
    else:
        print("\nSuccess! All files were properly clustered and saved.")
    print("\nTopic clusters have been saved to the topic_clusters directory.")

if __name__ == "__main__":
    main()
