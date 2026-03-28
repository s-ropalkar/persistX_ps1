# services/rag_engine.py

import pandas as pd


class RAGEngine:
    def __init__(self, csv_path="data/certified_brands.csv"):
        try:
            self.df = pd.read_csv(csv_path)
        except:
            self.df = pd.DataFrame(columns=["brand", "certification"])

    def find_certification(self, text):

        text_lower = text.lower()
        matches = []

        for _, row in self.df.iterrows():
            brand = str(row["brand"]).lower()

            if brand in text_lower:
                matches.append({
                    "brand": row["brand"],
                    "certification": row["certification"]
                })

        return matches