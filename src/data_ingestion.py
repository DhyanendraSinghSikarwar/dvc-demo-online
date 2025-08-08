import pandas as pd
import numpy as np
import os
import loguru

# Set up logging
loguru.logger.add("logs/error.log", level="ERROR", rotation="1 MB", compression="zip")
loguru.logger.info("Logging is set up.")


def load_data(url):
    try:
        df = pd.read_csv(url)
        loguru.logger.info("Data loaded successfully.")
        return df
    except Exception as e:
        loguru.logger.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error


def preprocess_data(df):
    
    df = df.iloc[:, 3:]
    
    df = df[df['Length of Membership'] > 3]

    df.drop(columns=['Avg. Session Length'], inplace=True)
    return df


def save_preprocessed_data(df, output_path):
    df.to_csv(output_path, index=False)
    loguru.logger.info(f"Data saved to {output_path}")


def main():
    try:
        df = load_data('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
        if not df.empty:
            loguru.logger.info("Data loaded successfully.")
        else:
            loguru.logger.warning("Loaded data is empty.")
        df = preprocess_data(df)
        path = os.path.join('data', 'customer.csv')
        save_preprocessed_data(df, path)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Data ingestion process completed.")

if __name__ == "__main__":
    main()