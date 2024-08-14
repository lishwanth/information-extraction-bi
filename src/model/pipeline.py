from src.data.document_loader import DocumentLoader
from src.data.preprocessor import Preprocessor
from src.model.information_extractor import InformationExtractor

class DataPipeline:
    def __init__(self):
        self.loader = DocumentLoader()
        self.preprocessor = Preprocessor()
        self.extractor = InformationExtractor()

    def run_pipeline(self, file_path):
        raw_text = self.loader.load_pdf(file_path)
        clean_text = self.preprocessor.clean_text(raw_text)
        tokens = self.preprocessor.tokenize(clean_text)
        predictions = self.extractor.predict(tokens)
        return predictions
