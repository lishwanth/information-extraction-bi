import streamlit as st
from src.model.pipeline import DataPipeline

pipeline = DataPipeline()

st.title("Document Information Extraction for BI")

uploaded_file = st.file_uploader("Choose a document file...", type=["pdf", "png", "jpg"])
if uploaded_file is not None:
    file_path = f'./data/{uploaded_file.name}'
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    predictions = pipeline.run_pipeline(file_path)
    st.write(predictions)
