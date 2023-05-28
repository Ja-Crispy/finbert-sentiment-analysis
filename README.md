# Sentiment Analysis for Financial Headlines

This code performs sentiment analysis on financial headlines using the `ProsusAI/finbert` model. It leverages the `transformers` library for natural language processing and `wandb` for logging the results. The code takes advantage of multiprocessing to speed up the prediction process.

## Dataset
The dataset used here is "Daily Financial News for 6000+ stocks", which is available on Kaggle. It contains ~4m financial headlines for 6000+ stocks from 2009-2020. 
Here's the link to the [dataset](https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests?select=raw_analyst_ratings.csv)

## Model
The sentiment analysis is conducted using the `ProsusAI/finbert` model. This model is specifically trained for financial sentiment analysis tasks and provides accurate predictions for positive, negative, and neutral sentiments.

## Libraries Used
- `pandas`: Used for loading and manipulating data from a CSV file.
- `numpy`: Used for array operations and data handling.
- `torch`: Used for performing predictions with the `finbert` model.
- `transformers`: Used for loading the `ProsusAI/finbert` model and tokenizing input data.
- `wandb`: Used for logging and visualizing the results.
- `multiprocessing`: Used for parallel processing and improving performance.

## Benefits of Multiprocessing
To enhance performance, the code utilizes the multiprocessing approach. Here are the benefits of using multiprocessing in this scenario:
- **Faster Predictions**: By dividing the input data into smaller chunks and processing them in parallel, the sentiment analysis can be performed more efficiently, reducing the overall execution time.
- **Utilizing Multiple CPU Cores**: The code automatically detects the number of available CPU cores and assigns a worker process to each core. This allows for optimal utilization of computational resources, resulting in improved throughput.
- **Shared Result List**: The multiprocessing manager provides a shared result list that allows each worker process to store its predictions independently. This approach eliminates the need for complex synchronization mechanisms and ensures that the results are collected accurately.

By employing multiprocessing, the code optimizes the sentiment analysis pipeline, making it well-suited for handling large amounts of financial headlines efficiently.

**Note:** Ensure that the input data is properly formatted and stored in a CSV file before running the code. As WandB has a 200,000 entry limit for free accounts, the num_entries variable in preprocessing.py should be set to 200,000 or less. This will ensure that the code runs without any errors.

For any further details or inquiries, please refer to the code and its comments.
