#from src.wine_quality.logging import logger
#logger.info("this is my logger")

from src.wine_quality import logger
from src.wine_quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wine_quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.wine_quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.wine_quality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.wine_quality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME="Data Ingestion stage"

if __name__ == "__main__":
    try:
        logger.info(f"<<<<< stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f" >>>>>> stage {STAGE_NAME} completed<<<<<<\n\n X===================X")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Data Validation stage"

if __name__ == "__main__":
    try:
        logger.info(f"<<<<< stage { STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f" >>>>>> stage {STAGE_NAME} completed<<<<<<\n\n X===================X")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Data Transformation stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_ingestion = DataTransformationTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
