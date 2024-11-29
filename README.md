# Ramyasreekodati-END-TO-END-MACHINE-LEARNING-PROJECT
End-to-End Machine Learning Project
Welcome to the End-to-End Machine Learning Project repository! This project demonstrates the complete lifecycle of a machine learning workflow, from data preparation to deployment, ensuring a scalable and maintainable solution.

""" 
End to end ml Project Implementation
1. Introduction
2. GitHub Repo setup
3. Project Template creation
4. project setup
5. Logging , Exception and Utility
6. Project Workflows
7. Notepad Experiment's
8. Components Implementation
	Data Ingestion
	Data Validation
	Data Transformation
	Data Training
	Data Evaluation
9.  Training pipeline
10. Prediction Pipeline
11. User APP Implementation's
12. Decentralization
13. Deployment on AWS --> CI/CD

"""

#Clone the repository
''''
bash

https://github.com/Ramyasreekodati/END-TO-END-MACHINE-LEARNING-PROJECT.git

'''

### Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```
'''bash
now open up your local host 0.0.0.0 : 2021
'''


get config --global user.name "Ramyasreekodati"
get config --global user.email "ramyasreekodati@gmail.com"

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# Directory Structure

├── research  
│   ├── 01_data_ingestion.py  
│   ├── 02_data_validation.py   
│   ├── 03_data_transformation.py   
│   ├── 04_model_trainer.py        # Prototyping and experimentation scripts.  
│   ├── 05_model_evaluation.py   
├── config  
│   └── config.yaml                # Configuration settings for the project.  
├── src  
│   ├── utils  
│   │   └── common.py              # Utility functions for YAML parsing, directory creation, etc.  
│   ├── entity  
│   │   └── config_entity.py       # Data classes for configuration management.  
│   ├── components  
│   │   ├── data_ingestion.py 
│   │   ├── data_validation.py      # Logic for fetching and structuring raw data.  
│   │   ├── data_transformation.py 
│   │   ├── data_trainer.py 
│   │   ├── data_evaluation.py 
│   ├── pipeline  
│   │   ├── stage_01_data_ingestion.py 
│   │   ├── stage_02_data_validation.py  # Data ingestion pipeline stage.  
│   │   ├── stage_03_data_transformation.py 
│   │   ├── stage_04_model_trainer.py 
│   │   ├── stage_05_model_evaluation.py 
│   └── constants  
│       └── constants.py           # Centralized constants for the project.  
├── params.yaml                    # Parameters for model training and evaluation.  
├── schema.yaml                    # Schema for validating input data.  
├── app.py                         # Flask application for user interaction.  
├── artifacts                      # Directory for storing pipeline outputs.  
├── logs                           # Directory for execution logs.  
├── main.py                        # Entry point for orchestrating the pipeline.  
├── requirements.txt               # Python dependencies.  
├── setup.py                       # Script for installing the project as a package.  
└── README.md                      # Overview and documentation for the project.  
├── app.py                           # Main application file
├── project_folder\
│   ├── static\
│   │    ├── css\
│   │         └── style.css            # CSS styles
│   │     ├── js\                      # (Optional) Add if JavaScript files are needed
│   │     └── images\
│   │         └── image.jpg            # Place for images
│   ├── templates\                   # HTML templates
│   │     ├── index.html
│   │     ├── result.html
│   │     ├── signin.html
│   │     ├── signup.html
│   └── __init__.py  
















