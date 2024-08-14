import re
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

class Preprocessor:
    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
        text = re.sub(r'\d+', '<NUM>', text)  # Replace numbers
        return text.strip()

    def tokenize(self, text):
        return word_tokenize(text)

    def extract_entities(self, text):
        # Placeholder for advanced entity extraction (e.g., using spaCy)
        return re.findall(r'\b[A-Z][a-z]*\b', text)  # Example regex for entity extraction
