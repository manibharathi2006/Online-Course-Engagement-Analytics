import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('/mnt/data/mini_project.csv')
# 1. Check for Missing Values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)
# 2. Data Analysis: Correlation between 'Video_Watched_Time' and 'Quiz_Scores'
correlation = data['Video_Watched_Time'].corr(data['Quiz_Scores'])
print(f"\nCorrelation between Video Watched Time and Quiz Scores: {correlation:.2f}")
# 3. Compare Completion Status based on 'Major'
completion_by_major=data.groupby('Major')['Completion_Status'].value_counts(normalize=True).
unstack()
print("\nCompletion Status by Major:\n", completion_by_major)
# 4. Visualizations
# Plot 1: Correlation Heatmap (Optional)
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
# Plot 2: Video Watched Time vs Quiz Scores (Scatter plot)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Video_Watched_Time', y='Quiz_Scores', data=data, hue='Completion_Status')
plt.title('Video Watched Time vs Quiz Scores')
plt.xlabel('Video Watched Time (minutes)')
plt.ylabel('Quiz Scores')
plt.show()


# Plot 3: Completion Status by Major (Bar plot)
completion_by_major.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title('Completion Status by Major')
plt.ylabel('Proportion')
plt.show()
# Plot 4: Distribution of Final Exam Scores
plt.figure(figsize=(8, 6))
sns.histplot(data['Final_Exam_Scores'], kde=True, color='purple')
plt.title('Distribution of Final Exam Scores')
plt.xlabel('Final Exam Scores')
plt.ylabel('Frequency')
plt.show()
# Plot 5: Time to Complete vs Completion Status (Box plot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Completion_Status', y='Time_to_Complete', data=data)
plt.title('Time to Complete by Completion Status')
plt.ylabel('Time to Complete (days)')
plt.show()
