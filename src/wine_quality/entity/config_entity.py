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



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str