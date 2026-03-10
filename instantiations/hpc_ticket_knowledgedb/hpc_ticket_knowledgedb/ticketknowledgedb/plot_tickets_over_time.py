import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Read JSONL file
tickets = []
with open('total_tickets.jsonl', 'r') as file:
    for line in file:
        tickets.append(json.loads(line))

# Convert to DataFrame
df = pd.DataFrame(tickets)

# Convert creation dates to datetime
df['Created'] = pd.to_datetime(df['Created'])

# Filter data from 2014 onwards
df = df[df['Created'].dt.year >= 2014]

# Group by date and count tickets
daily_counts = df.groupby(df['Created'].dt.date).size().reset_index()
daily_counts.columns = ['date', 'count']
daily_counts['date'] = pd.to_datetime(daily_counts['date'])

# Create the plot
plt.figure(figsize=(15, 8))

# Plot ticket frequency
plt.plot(daily_counts['date'], daily_counts['count'], color='blue', label='Tickets per day')

# Get the date range
min_date = pd.to_datetime('2014-01-01')
max_date = daily_counts['date'].max()
years = range(2014, max_date.year + 1)

# Highlight semester holidays
for year in years:
    # Winter holidays (February - April)
    plt.axvspan(pd.to_datetime(f'{year}-02-01'), pd.to_datetime(f'{year}-04-01'), 
                alpha=0.2, color='yellow', label='Semester holidays' if year == years[0] else None)
    
    # Summer holidays (July - October)
    plt.axvspan(pd.to_datetime(f'{year}-07-01'), pd.to_datetime(f'{year}-10-01'), 
                alpha=0.2, color='yellow')

# Customize the plot
plt.title('Ticket Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Tickets')
plt.grid(True, alpha=0.3)
plt.legend()

# Format x-axis
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Rotate and align the tick labels so they look better
plt.gcf().autofmt_xdate()

# Add a bit of padding to the x-axis
plt.margins(x=0.02)

# Save the plot
plt.savefig('ticket_frequency.png')
plt.close()
