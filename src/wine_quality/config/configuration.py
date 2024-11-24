from wine_quality.constants import *
from wine_quality.utils.common import read_yaml, create_directories
from wine_quality.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # Path to the main config file
        params_filepath = PARAMS_FILE_PATH,  # Path to the parameters file
        schema_filepath = SCHEMA_FILE_PATH  # Path to the schema file
    ):
        self.config = read_yaml(config_filepath)  # Load configuration settings
        self.params = read_yaml(params_filepath)  # Load parameter settings
        self.schema = read_yaml(schema_filepath)  # Load schema details

        create_directories([self.config.artifacts_root])  # Ensure artifact root directory exists

        # Artifacts setup starts here for data ingestion

    def get_data_ingestion_config(self) -> DataIngestionConfig:  # Returns data ingestion configuration
        config = self.config.data_ingestion  # Access data ingestion settings

        create_directories([config.root_dir])  # Ensure the root directory for data ingestion exists

        # Populate and return the DataIngestionConfig object with relevant paths and URLs
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
