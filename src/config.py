import os

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///bi_extraction.db')
    MODEL_PATH = os.getenv('MODEL_PATH', './models/sentiment_model')
    DATA_DIR = os.getenv('DATA_DIR', './data/processed')
    RAW_DATA_DIR = os.getenv('RAW_DATA_DIR', './data/raw')
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')
