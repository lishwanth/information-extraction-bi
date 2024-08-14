import pandas as pd

class BIProcessor:
    def normalize_data(self, extracted_data):
        # Normalize extracted data (e.g., unify date formats, currencies)
        return pd.DataFrame(extracted_data)

    def generate_reports(self, normalized_data):
        # Generate business reports
        report = normalized_data.describe()  # Example report
        return report
