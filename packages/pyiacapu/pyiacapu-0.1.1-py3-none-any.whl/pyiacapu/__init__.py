import pandas as pd

from .conceitos import IAList # noqa


class Knn:

    def __init__(self, sample1, sample2):
        self.sample1 = sample1
        self.sample2 = sample2
        self.series1 = pd.Series([*sample1])
        self.series2 = pd.Series([*sample2])

    def __call__(self):
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
