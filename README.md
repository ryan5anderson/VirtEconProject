# Economist Chatbot Project

This project aims to develop an economist chatbot using pre-trained models from Hugging Face and economic data from public databases.

## Directory Structure

- `data/`: Contains all datasets.
  - `raw/`: Raw data directly obtained from APIs or other sources.
  - `processed/`: Cleaned and processed data ready for analysis or model training.
  - `external/`: Any external data files that are not raw but needed for the project.
- `models/`: Stores model files.
  - `pretrained/`: Pre-trained models downloaded from Hugging Face or other sources.
  - `fine_tuned/`: Fine-tuned models specific to your project.
- `notebooks/`: Jupyter notebooks for exploration and development.
- `scripts/`: Standalone scripts for various tasks.
- `src/`: Source code for the project.
  - `api/`: Code related to API interactions (e.g., fetching data from FRED).
  - `chatbot/`: Chatbot implementation including the interface and logic.
  - `data_processing/`: Functions and scripts for cleaning and processing data.
  - `training/`: Scripts and modules for training and fine-tuning models.
- `tests/`: Unit tests and other test scripts.
- `configs/`: Configuration files.
- `logs/`: Log files.
- `results/`: Output results.
