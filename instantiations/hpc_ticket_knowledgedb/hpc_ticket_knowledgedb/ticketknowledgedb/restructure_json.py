import json
import sys
from datetime import datetime

# Map communication channel IDs to their string names
CHANNEL_MAP = {
    1: "Email",
    2: "Phone",
    3: "Internal",
    4: "Chat",
    5: "SMS",
}

def convert_ticket(ticket_data):
    """Convert a ticket from the unarchived format to the target format."""
    ticket = ticket_data["Ticket"][0]
    
    # Extract base ticket information
    restructured = {
        "TicketNumber": ticket["TicketNumber"],
        "TicketID": str(ticket["TicketID"]),
        "Title": ticket["Title"],
        "Created": ticket["Created"],
        "Queue": ticket["Queue"],
        "State": ticket["State"],
        "Priority": ticket["Priority"],
        "Lock": ticket["Lock"],
        "CustomerID": ticket["CustomerID"],
        "CustomerUserID": ticket["CustomerUserID"],
        "conversations": []
    }
    
    # Convert articles to conversations
    for article in ticket["Article"]:
        # Map the channel ID to its string name
        channel_id = article.get("CommunicationChannelID")
        channel = CHANNEL_MAP.get(channel_id, "Email") if channel_id else "Email"
        
        conversation = {
            "ArticleID": str(article["ArticleID"]),
            "CreateTime": article["CreateTime"],
            "SenderType": article["SenderType"],
            "Channel": channel,
            "From": article["From"],
            "To": article.get("To", ""),
            "Sender": article["From"],
            "Subject": article["Subject"],
            "content": article.get("Body", ""),
            "role": "user" if article["SenderType"] == "customer" else "system"
        }
        
        # Add Cc if present
        if article.get("Cc"):
            conversation["Cc"] = article["Cc"]
            
        restructured["conversations"].append(conversation)
        
    return restructured

def main():
    input_file = "tickets_unarchived.jsonl"
    output_file = "tickets_restructured.jsonl"
    
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            try:
                ticket_data = json.loads(line.strip())
                restructured_ticket = convert_ticket(ticket_data)
                json.dump(restructured_ticket, f_out, ensure_ascii=False)
                f_out.write('\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}", file=sys.stderr)
            except Exception as e:
                print(f"Error processing ticket: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
