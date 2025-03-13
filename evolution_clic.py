import matplotlib.pyplot as plt
import pandas as pd

# Assurez-vous de charger vos données nettoyées
data = pd.read_csv('cleaned_dataset_marketing.csv')
data['Date'] = pd.to_datetime(data['Date'])  # Convertir la colonne 'Date' en datetime si ce n'est pas déjà fait

# Grouping data by week and campaign, then calculating the mean of clicks
weekly_clicks = data.groupby([data['Date'].dt.to_period('W'), 'Campagne'])['Clics'].mean().unstack()

# Resetting the index to convert periods to timestamps for plotting
weekly_clicks.index = weekly_clicks.index.to_timestamp()

# Creating a bar chart for weekly average clicks per campaign
plt.figure(figsize=(20, 12))
width = 0.15  # width of the bars

# Plotting bars for each campaign with a slight offset for each to avoid overlap
for i, campaign in enumerate(weekly_clicks.columns):
    plt.bar(weekly_clicks.index + pd.to_timedelta(i * width, unit='W'), weekly_clicks[campaign], width=width, label=campaign)

plt.title('Moyenne Hebdomadaire des Clics par Campagne (Diagramme en Barres)')
plt.xlabel('Semaine')
plt.ylabel('Moyenne des Clics')
plt.legend(title='Campagne')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(weekly_clicks.index, labels=[date.strftime('%Y-%m-%d') for date in weekly_clicks.index], rotation=45)
plt.tight_layout()
plt.show()
