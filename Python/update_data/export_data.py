from pathlib import Path


class DataFrameExporter:
    def __init__(self, df, path):
        self.df = df
        self.path = path

    def to_json(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.df.to_json(self.path, orient='records', force_ascii=False, indent=4)

    def to_csv(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.path, index=False, sep='|')

    def to_excel(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.df.to_excel(self.path, index=False)
