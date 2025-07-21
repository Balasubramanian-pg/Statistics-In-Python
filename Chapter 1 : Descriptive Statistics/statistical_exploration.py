import kagglehub
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_prepare_data():
    """Loads data from KaggleHub and performs initial validation."""
    print("\n--- Phase 1: Data Validation and Familiarization ---")
    print("Downloading dataset from Kaggle Hub...")
    dataset_path = kagglehub.dataset_download('rudraprasadbhuyan/spotify-dataset-for-ml-practice')
    file_path = os.path.join(dataset_path, "modified-spotify-dataset.csv")
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")

    cols_of_interest = [
        'popularity', 'danceability', 'energy', 'valence', 'loudness',
        'explicit', 'mood_cluster'
    ]

    print(f"\nData Shape: {df.shape}")
    print("\nData Types of Relevant Columns:")
    print(df[cols_of_interest].dtypes)
    print("\nMissing Values in Relevant Columns:")
    print(df[cols_of_interest].isnull().sum())
    print("\nDescriptive Statistics for Continuous Variables:")
    print(df[cols_of_interest].describe())
    return df

def perform_t_test(df, alpha=0.05):
    """Performs and prints the results of an independent t-test."""
    print("\n--- Test 1: Popularity of Explicit vs. Non-Explicit Songs (T-Test) ---")
    popularity_explicit = df[df['explicit'] == 1]['popularity']
    popularity_non_explicit = df[df['explicit'] == 0]['popularity']

    t_stat, p_value = stats.ttest_ind(popularity_explicit, popularity_non_explicit, equal_var=False)

    print(f"H0 (Null Hypothesis): Mean popularity is equal for explicit and non-explicit songs.")
    print(f"H1 (Alternative Hypothesis): Mean popularity is different for explicit and non-explicit songs.")
    print(f"\nMean Popularity (Explicit): {popularity_explicit.mean():.2f}")
    print(f"Mean Popularity (Non-Explicit): {popularity_non_explicit.mean():.2f}")
    print(f"T-statistic: {t_stat:.2f}")
    print(f"P-value: {p_value}")
    if p_value < alpha:
        print("Result: Reject the null hypothesis. The difference is statistically significant.")
    else:
        print("Result: Fail to reject the null hypothesis.")
    return t_stat, p_value

def perform_anova(df, alpha=0.05):
    """Performs and prints the results of an ANOVA test."""
    print("\n--- Test 2: Energy across different Mood Clusters (ANOVA) ---")
    mood_clusters = df['mood_cluster'].unique()
    energy_by_mood = [df[df['mood_cluster'] == cluster]['energy'] for cluster in mood_clusters]

    f_stat, p_value = stats.f_oneway(*energy_by_mood)

    print(f"H0 (Null Hypothesis): Mean energy is the same across all mood clusters.")
    print(f"H1 (Alternative Hypothesis): At least one mood cluster has a different mean energy.")
    print("\nMean Energy by Mood Cluster:")
    print(df.groupby('mood_cluster')['energy'].mean())
    print(f"\nF-statistic: {f_stat:.2f}")
    print(f"P-value: {p_value}")
    if p_value < alpha:
        print("Result: Reject the null hypothesis. A significant difference exists.")
    else:
        print("Result: Fail to reject the null hypothesis.")
    return f_stat, p_value

def perform_correlation_test(df, alpha=0.05, output_dir="analysis_outputs"):
    """Performs a Pearson correlation, saves a plot, and prints results."""
    print("\n--- Test 3: Relationship between Danceability and Valence (Pearson Correlation) ---")

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Visualization
    print("Generating scatter plot for Valence vs. Danceability...")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='valence', y='danceability', alpha=0.1, s=10)
    plt.title('Valence vs. Danceability in Spotify Songs')
    plt.xlabel('Valence (Musical Positiveness)')
    plt.ylabel('Danceability')
    plt.grid(True)
    plot_path = os.path.join(output_dir, 'valence_vs_danceability.png')
    plt.savefig(plot_path)
    plt.close() # Close the plot to free up memory
    print(f"Plot saved to {plot_path}")

    r_value, p_value = stats.pearsonr(df['danceability'], df['valence'])

    print(f"\nH0 (Null Hypothesis): There is no linear correlation between danceability and valence.")
    print(f"H1 (Alternative Hypothesis): There is a linear correlation between danceability and valence.")
    print(f"\nPearson Correlation Coefficient (r): {r_value:.2f}")
    print(f"P-value: {p_value}")
    if p_value < alpha:
        print("Result: Reject the null hypothesis. The correlation is statistically significant.")
    else:
        print("Result: Fail to reject the null hypothesis.")
    return r_value, p_value

def main():
    """Main function to run the full analysis pipeline."""
    print("Starting statistical exploration of the Spotify dataset...")

    df = load_and_prepare_data()

    print("\n--- Phase 2 & 3: Hypothesis Testing and Interpretation ---")
    alpha = 0.05

    perform_t_test(df, alpha)
    perform_anova(df, alpha)
    perform_correlation_test(df, alpha, output_dir="analysis_outputs")

if __name__ == "__main__":
    main()