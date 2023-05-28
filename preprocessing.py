import pandas as pd

def preprocess_dataset(file_path, num_entries):
    # Read the dataset from CSV file
    df = pd.read_csv(file_path)

    # Select relevant columns
    selected_columns = ['headline', 'stock ticker symbol']
    df = df[selected_columns]

    # Remove any rows with missing values
    df = df.dropna()

    # Select a specific number of entries
    df = df.head(num_entries)

    # Perform additional preprocessing steps as needed
    # For example, you can remove punctuation, convert text to lowercase, etc.

    # Return the preprocessed dataset
    return df

# Usage example
file_path = 'path/to/dataset.csv'
num_entries = 100000  # Number of entries to select from the dataset
preprocessed_df = preprocess_dataset(file_path, num_entries)
