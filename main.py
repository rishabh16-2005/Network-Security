from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TraingPipelineConfig
from networksecurity.entity.config_entity import DataIngestionConfig , DataValidationConfig
import sys
if __name__ == "__main__":
    try:
        trainingpipelineconfig = TraingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestionartifacts=data_ingestion.initiate_data_ingestion()
        logging.info("data initiation completed")
        data_validation_config = DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifacts,data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)