import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BigQueryConnector:
    """
    Handles secure connectivity and data ingestion from GCP BigQuery.
    Following the Medallion architecture, it pulls data from Gold datasets.
    """
    
    def __init__(self):
        self.project_id = os.getenv('GCP_PROJECT_ID')
        self.dataset_id = os.getenv('GCP_DATASET_ID')
        self.table_id = os.getenv('GCP_TABLE_ID', 'crypto_historical_trends')
        
        if not self.project_id or not self.dataset_id:
            raise ValueError(
                "Missing environment variables: GCP_PROJECT_ID or GCP_DATASET_ID. "
                "Please ensure they are set in your .env file."
            )
        creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        if creds_path and not os.path.exists(creds_path):
            # Try one level up if not found (common for notebooks)
            alt_path = os.path.join('..', creds_path)
            if os.path.exists(alt_path):
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = alt_path
                print(f"[INFO] Adjusted credentials path for notebook context: {alt_path}")

        self.client = bigquery.Client(project=self.project_id)

    def fetch_historical_trends(self) -> pd.DataFrame:
        """
        Retrieves historical crypto trends from the Gold dataset.
        """
        query = f"""
            SELECT *
            FROM `{self.project_id}.{self.dataset_id}.{self.table_id}`
            ORDER BY ds ASC
        """
        print(f"Executing query on: {self.project_id}.{self.dataset_id}.{self.table_id}")
        return self.client.query(query).to_dataframe()

    def fetch_custom_query(self, query: str) -> pd.DataFrame:
        """
        Executes a custom SQL query and returns a DataFrame.
        Useful for targeted analysis or pulling from multiple views.
        """
        return self.client.query(query).to_dataframe()

if __name__ == "__main__":
    # Smoke test for BigQuery connectivity
    try:
        connector = BigQueryConnector()
        print("[+] Connector initialized successfully.")
        
        # Attempt to fetch a small sample
        print("[+] Testing data extraction (limit 5)...")
        # Note: Added LIMIT 5 for the smoke test to be efficient
        query_test = f"SELECT * FROM `{connector.project_id}.{connector.dataset_id}.{connector.table_id}` LIMIT 5"
        sample_data = connector.fetch_custom_query(query_test)
        
        if not sample_data.empty:
            print("[SUCCESS] Data extraction verified. Sample head:")
            print(sample_data)
        else:
            print("[WARNING] Connection successful but table appears to be empty.")
            
    except Exception as e:
        print(f"[ERROR] Connection test FAILED: {e}")
        print("\nSenior Tip: Check if your Service Account has 'BigQuery Data Viewer' permissions.")
