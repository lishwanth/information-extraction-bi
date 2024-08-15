
# Information Extraction for Business Intelligence

## Overview

This project is an end-to-end solution for extracting and analyzing information from business documents such as invoices, contracts, and reports. The goal is to provide insights and generate reports for Business Intelligence (BI). The system leverages OCR, NLP, and machine learning techniques to process documents, extract relevant entities, and provide structured data for further analysis.

## Tools and Technologies

- **Programming Language:** Python 3.9
- **NLP Framework:** Hugging Face Transformers (LayoutLM)
- **OCR:** Tesseract
- **Data Processing:** Pandas, NumPy
- **Web Framework:** Flask (API), Streamlit (Frontend)
- **Database:** SQLite
- **Containerization:** Docker, Docker Compose
- **MLOps:** MLflow (for experiment tracking)
- **Version Control:** GitHub

## Project Structure

```plaintext
information-extraction-bi/
│
├── data/
│   ├── raw/                     # Raw data files
│   └── processed/               # Processed data files
│
├── models/                      # Trained models and checkpoints
│
├── notebooks/                   # Jupyter notebooks for experimentation and analysis
│   ├── exploratory_analysis.ipynb   # Initial data exploration
│   ├── sentiment_analysis.ipynb     # Model training and evaluation
│   └── trend_analysis.ipynb         # Trend analysis of extracted data
│
├── src/
│   ├── data/
│   │   ├── document_loader.py       # Document loading and OCR processing
│   │   └── preprocessor.py          # Text preprocessing and entity extraction
│   │
│   ├── model/
│   │   ├── information_extractor.py # Model definition and training
│   │   └── pipeline.py              # Data pipeline for end-to-end processing
│   │
│   ├── logic/
│   │   ├── bi_processor.py          # Business logic and reporting
│   │
│   ├── web/
│   │   ├── api_server.py            # Flask API server
│   │   └── frontend.py              # Streamlit frontend interface
│   │
│   ├── db/
│   │   └── database_manager.py      # Database management for storing and querying extracted data
│   │
│   ├── utils.py                     # Utility functions used across the project
│   └── config.py                    # Configuration settings for the project
│
├── tests/                           # Unit and integration tests
│   └── test_pipeline.py             # Tests for the data pipeline
│
├── Dockerfile                       # Docker configuration for containerization
├── docker-compose.yml               # Docker Compose setup for multi-container applications
├── requirements.txt                 # Python dependencies required for the project
├── README.md                        # Project overview, tools, structure, and setup instructions
└── .gitignore                       # Files and directories to ignore in version control
```

## Getting Started

### Prerequisites

- Python 3.9
- Docker and Docker Compose
- Tesseract OCR

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/information-extraction-bi.git
   cd information-extraction-bi
   ```

2. **Install Python dependencies:**

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

- **API Endpoint:** The Flask API will be available at `http://localhost:5000/predict`. You can POST documents to this endpoint to get predictions and extracted entities.
- **Frontend:** The Streamlit frontend will be accessible at `http://localhost:8501`. You can upload documents through the interface and view the results.

## Detailed Explanation

### Data Pipeline

The data pipeline processes documents through various stages:
1. **Document Loading:** Using the `DocumentLoader` class, documents are loaded from PDFs or images, and text is extracted using Tesseract OCR.
2. **Text Preprocessing:** The `Preprocessor` class cleans and tokenizes the extracted text, making it ready for entity extraction.
3. **Model Inference:** The `InformationExtractor` class uses a pre-trained LayoutLM model to identify and extract entities from the processed text.
4. **Business Logic:** The extracted entities are further processed using the `BIProcessor` class to generate structured data and reports.
5. **Storage and Querying:** Extracted data can be stored in an SQLite database for further querying and analysis.

### Models

- **LayoutLM:** This model is specifically designed for documents with complex layouts (such as invoices and forms). It uses both textual and layout information to extract entities more accurately than traditional NLP models.

### Business Logic

- **Normalization:** The extracted entities are normalized to ensure consistency in the data.
- **Reporting:** Business intelligence reports are generated based on the extracted and normalized data, providing insights into key metrics.

## Deployment

The project is containerized using Docker to ensure consistency across different environments. The Docker setup includes:
- A container for the Flask API
- A container for the Streamlit frontend
- SQLite database setup

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.
