
# Information Extraction for Business Intelligence

## Overview

This project is an end-to-end solution for extracting information from business documents (e.g., invoices, contracts) and generating reports for Business Intelligence (BI). The system uses a combination of OCR, NLP, and machine learning techniques to process documents, extract relevant entities, and provide insights.

## Project Structure

```plaintext
information-extraction-bi/
│
├── data/
│   ├── raw/                     # Raw data files
│   └── processed/               # Processed data files
│
├── models/                      # Trained models
│
├── src/
│   ├── data/
│   │   ├── document_loader.py   # Document loading and OCR
│   │   └── preprocessor.py      # Data preprocessing
│   │
│   ├── model/
│   │   ├── information_extractor.py  # Model training and inference
│   │   └── pipeline.py          # Data pipeline management
│   │
│   ├── logic/
│   │   ├── bi_processor.py      # Business logic for processing and reporting
│   │
│   ├── web/
│   │   ├── api_server.py        # Flask or FastAPI server
│   │   └── frontend.py          # Streamlit front-end
│   │
│   ├── db/
│   │   └── database_manager.py  # Database interactions
│   │
│   ├── utils.py                 # Utility functions
│   └── config.py                # Configuration settings
│
├── tests/                       # Unit and integration tests
│   └── test_pipeline.py         # Test for the data pipeline
│
├── Dockerfile                   # Docker setup
├── docker-compose.yml           # Docker Compose setup
├── requirements.txt             # Python package dependencies
├── README.md                    # Project overview and setup instructions
└── .gitignore                   # Git ignore file
```

## Getting Started

### Prerequisites

- Python 3.9
- Docker

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/information-extraction-bi.git
   cd information-extraction-bi
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   - **Using Docker:**

     ```bash
     docker-compose up --build
     ```

   - **Without Docker:**

     ```bash
     python src/web/api_server.py
     ```

### Usage

- **API:** The Flask API will be available at `http://localhost:5000/predict`. You can POST documents to this endpoint to get predictions.
- **Frontend:** The Streamlit frontend will be available at `http://localhost:8501` (if running separately).

## Project Details

### Data Pipeline

- The data pipeline loads documents, preprocesses them, and then passes them through the NLP model for entity extraction.

### Models

- **LayoutLM**: Used for extracting entities from documents with complex layouts like invoices and contracts.

### Business Logic

- The extracted entities are processed and normalized to generate useful reports for business intelligence.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
