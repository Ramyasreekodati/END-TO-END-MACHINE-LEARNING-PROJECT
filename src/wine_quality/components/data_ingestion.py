import os
import urllib.request as request
import zipfile
from wine_quality import logger
from wine_quality.utils.common import get_size
from pathlib import Path
from wine_quality.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config  # Store the DataIngestionConfig object for file paths and URLs

    def download_file(self):
        """
        Downloads the data file from the source URL if it does not already exist locally.
        Logs file information upon download or skips if the file is already present.
        """
        if not os.path.exists(self.config.local_data_file):  # Check if file already exists
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,  # URL to download the file from
                filename=self.config.local_data_file  # Local path to save the file
            )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")  # Log successful download
        else:
            # Log that the file already exists and display its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the downloaded zip file into the specified directory.
        Creates the extraction directory if it does not exist.
        """
        unzip_path = self.config.unzip_dir  # Directory where the files will be extracted
        os.makedirs(unzip_path, exist_ok=True)  # Ensure the extraction directory exists
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # Extract all files into the unzip directory

  