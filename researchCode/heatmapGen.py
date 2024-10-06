import pandas as pd
import seaborn as sns

# Loading Data 
df = pd.read_csv("./data/sector_train_data.csv", usecols=['Social Engineering', 'Network', 'Bad Security Practices',
       'Exploitation', 'Other Malware', 'Ransomware', 'Web Application',
       'Wireless', 'Cloud', 'Mobile', 'IoT/OT', 'Insider(Yes/No)', 'Sector'])

# Preprocessing data
df_cleaned = df[['Social Engineering', 'Network', 'Bad Security Practices',
       'Exploitation', 'Other Malware', 'Ransomware', 'Web Application',
       'Wireless', 'Cloud', 'Mobile', 'IoT/OT', 'Insider(Yes/No)']].replace({"NO": 0, "YES": 1, "no": 0, "yes": 1})

# Plotting heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(df_cleaned.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
