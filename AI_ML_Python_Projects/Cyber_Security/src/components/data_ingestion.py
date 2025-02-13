import os
import sys
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# import psycopg2 as psy
# raw psycopg2 connection (conn) is not officially supported.
# Instead of using psycopg2 directly, create a SQLAlchemy engine and use that for read_sql().
from sqlalchemy import create_engine  


from src.my_logger import logging
from src.my_exception import  CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts',"train_set.csv")
    test_data_path: str = os.path.join('artifacts',"test_set.csv")
    raw_data_path: str = os.path.join('artifacts',"raw_set.csv")

class DataIngestion:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Data initialization starts")
            
            from sqlalchemy import create_engine


            host= 'localhost'
            database = 'CyberSecurity_dataset'
            user = 'postgres'
            password = 'amma'
            port = 5432 

            conn = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

            sql = "select * from cyber_security limit 10"
            df = pd.read_sql(sql,conn)

            logging.info("Reading the dataset as dataframe is done") 

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path,index=False, header=True)

            train_data, test_data = train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.data_ingestion_config.train_data_path,index = False,header = True)
            test_data.to_csv(self.data_ingestion_config.test_data_path,index = False,header = True)

            logging.info("train and test data are splitted and stored in a directory")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
                   )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()




