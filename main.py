#from src.wine_quality.logging import logger
#logger.info("this is my logger")

from src.wine_quality import logger
from src.wine_quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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