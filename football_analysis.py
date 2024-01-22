import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('fifa_players.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Display general information about the DataFrame
print(df.info())

# Display descriptive statistics of the DataFrame
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Analyzing Player Characteristics:

# Age distribution of players
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Players\' Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Overall rating distribution of players
sns.histplot(data=df, x='overall_rating', bins=20, kde=True)
plt.title('Distribution of Players\' Overall')
plt.xlabel('Overall')
plt.ylabel('Frequency')
plt.show()

# Analyzing Nationalities:

# Top 10 nationalities in the dataset
top_nationalities = df['nationality'].value_counts().head(10)
sns.barplot(x=top_nationalities.index, y=top_nationalities.values)
plt.title('Top 10 Nationalities of Players')
plt.xlabel('Nationality')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.show()

# Analyzing Player Potential:

# Distribution of player potential
plt.figure(figsize=(14, 6))
position_count = df['potential'].value_counts()
sns.barplot(x=position_count.index, y=position_count.values, palette='Set2')
plt.title('Distribution of Player Potential')
plt.xlabel('Potential')
plt.ylabel('Number of Players')
plt.xticks(rotation=45, ha='right', fontsize=10)  # Adding rotation and dimension to text
plt.tight_layout()  # Avoid overlap
plt.show()

# Choosing only some variables to define corelation chart 
selected_variables = ['age', 'overall_rating', 'potential', 'value_euro']
selected_correlation_matrix = df[selected_variables].corr()

# Correlation matrix for selected variables
plt.figure(figsize=(8, 6))
sns.heatmap(selected_correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, square=True)
plt.title('Correlation Matrix (Selected Variables)')
plt.show()