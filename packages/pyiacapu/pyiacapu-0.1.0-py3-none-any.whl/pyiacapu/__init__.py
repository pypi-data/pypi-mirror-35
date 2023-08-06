import pandas as pd


class Knn:

    def __init__(self, *args):
        self.args = args
        self.series = pd.Series([*args])

    def table(self):
        padrao_norm = {}

        media = self.series.mean()
        desvio_padrao = self.series.std()

        nums = []
        for idx, valor in enumerate(self.args):
            nums.append(valor)
            normalizado = (valor - media)/desvio_padrao
            padrao_norm.update({idx: normalizado})

        padrao_norm.update({'media': pd.Series([*nums]).mean()})
        padrao_norm.update({'desvio': pd.Series([*nums]).std()})

        return {
            'normalização': padrao_norm,
            'media': self.series.mean(),
            'desvio': self.series.mad()
        }
