import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelTrainerConfig,
    TrainingPipelineConfig,
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__ == '__main__':
    try:
        # Initialize the global training pipeline configuration
        trainingpipelineconfig = TrainingPipelineConfig()

        # -------------------------------------------------------------
        # 1. Data Ingestion Phase
        # -------------------------------------------------------------
        logging.info("Initiate the data ingestion")
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        # -------------------------------------------------------------
        # 2. Data Validation Phase
        # -------------------------------------------------------------
        logging.info("Initiate the data Validation")
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(
            dataingestionartifact, data_validation_config
        )
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        # -------------------------------------------------------------
        # 3. Data Transformation Phase
        # -------------------------------------------------------------
        logging.info("Data Transformation started")
        data_transformation_config = DataTransformationConfig(
            trainingpipelineconfig
        )
        data_transformation = DataTransformation(
            data_validation_artifact, data_transformation_config
        )
        data_transformation_artifact = (
            data_transformation.initiate_data_transformation()
        )
        logging.info("Data Transformation completed")
        print(data_transformation_artifact)

        # -------------------------------------------------------------
        # 4. Model Training Phase
        # -------------------------------------------------------------
        logging.info("Model Training started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact,
        )
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training completed and artifact created")
        print(model_trainer_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)