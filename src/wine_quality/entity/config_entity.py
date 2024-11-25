# congif.yaml

"""Here the process is happening in artifile """

from dataclasses import dataclass  # the dataclass decorator for simplifying class creation
from pathlib import Path  # Path for handling file system paths 

@dataclass(frozen=True)  #  simplifies the class structure; frozen makes it immutable
class DataIngestionConfig:
    root_dir: Path  # Root directory for managing all data ingestion-related files and outputs
    source_URL: str  # URL of the data source to be downloaded
    local_data_file: Path  # Path where the downloaded data file will be stored locally
    unzip_dir: Path  # Directory where the data will be extracted after downloading



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path



