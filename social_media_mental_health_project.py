import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
df = pd.read_csv('smmh.csv')


print(df["10. How often do you get distracted by Social media when you are busy doing something?"].value_counts())
print(df["18. How often do you feel depressed or down?"].value_counts())
df["10. How often do you get distracted by Social media when you are busy doing something?"].value_counts().sort_index().plot(kind='bar')
plt.title("Social Media Distraction")
plt.xlabel("Distraction Rating")
plt.ylabel("Number of Participants")
plt.show()

correlation, p_value = spearmanr(df["10. How often do you get distracted by Social media when you are busy doing something?"], df["18. How often do you feel depressed or down?"])
print("Correlation:", correlation)
print("P-Value:", p_value)
plt.figure(figsize=(6,4))
plt.scatter(df["10. How often do you get distracted by Social media when you are busy doing something?"], df["18. How often do you feel depressed or down?"])
plt.title("Distraction vs Depression")
plt.xlabel("Social Media Distraction")
plt.ylabel("Depression Rating")
plt.show()

plt.figure(figsize=(6,4))
df["18. How often do you feel depressed or down?"].hist(bins=5)
plt.title("Distribution of Depression Ratings")
plt.xlabel("Depression Rating")
plt.ylabel("Number of Participants")
plt.show()

columns = [
    "10. How often do you get distracted by Social media when you are busy doing something?",
    "18. How often do you feel depressed or down?",
    "20. On a scale of 1 to 5, how often do you face issues regarding sleep?",
    "13. On a scale of 1 to 5, how much are you bothered by worries?",
    "14. Do you find it difficult to concentrate on things?"
]
corr_matrix = df[columns].corr(method='spearman')
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', fmt=".2f")
plt.title("Correlation Between Social Media and Mental Health Factors")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
