import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Charger vos données nettoyées
data = pd.read_csv('cleaned_dataset_marketing.csv')

# Préparation des données
data_aggregated = data.groupby('Campagne')['Impressions'].sum().reset_index()

# Création de l'histogramme avec Seaborn
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(x='Campagne', y='Impressions', data=data_aggregated, palette='viridis')
plt.title('Nombre d\'impressions par campagne')
plt.xlabel('Campagne')
plt.ylabel('Nombre total d\'impressions')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# Améliorer la lisibilité
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right', fontweight='light', fontsize='x-large')
bar_plot.set_yticklabels([f'{int(x/1e3)}k' for x in bar_plot.get_yticks()], fontweight='light', fontsize='large')

plt.tight_layout()  # Ajuster la mise en page
plt.show()
