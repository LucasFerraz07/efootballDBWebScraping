# -*- coding: utf-8 -*-
"""Tratamento do CSV gerado pelo scrapping.py."""

import pandas as pd

# CARREGAMENTO
df = pd.read_csv("jogadoresV1.csv")

# TRATAMENTO
df = df[df['Overall'] <= 110].copy()

replacement_map = {
    'RWF': 'PD',
    'CF': 'CA',
    'SS': 'SA',
    'CB': 'ZG',
    'LWF': 'PE',
    'GK': 'GO',
    'AMF': 'MAT',
    'RB': 'LD',
    'CMF': 'MLG',
    'DMF': 'VOL',
    'LB': 'LE',
    'RMF': 'MLD',
    'LMF': 'MLE'
}
df['Posição'] = df['Posição'].replace(replacement_map)


def get_category(overall):
    if 40 <= overall <= 59:
        return 'white'
    elif 60 <= overall <= 69:
        return 'bronze'
    elif 70 <= overall <= 79:
        return 'silver'
    elif 80 <= overall <= 89:
        return 'gold'
    elif 90 <= overall <= 110:
        return 'black'
    else:
        return None


df['categoria'] = df['Overall'].apply(get_category)

df.to_csv('jogadores_tratados.csv', index=False)
