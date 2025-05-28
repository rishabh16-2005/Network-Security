from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TraiingPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig
import sys
if __name__ == "__main__":
    try:
        training_ingestion_pipeline = TraiingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_ingestion_pipeline)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestionartifacts=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityException(e,sys)