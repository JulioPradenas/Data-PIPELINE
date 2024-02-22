import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def data_preprocessing_pipeline(data):
    #identificar caracteristicas  numericas y categoricas 
    numeric_features = data.select_dtypes(include=['float', 'int']).columns
    categorical_features = data.select_dtypes(include=['object']).columns

    #manipular valores faltantes en caracteristicas en numericas
    data[numeric_features] = data[numeric_features].fillna(data[numeric_features].mean())

    #deteccion y manpulacion de outliers en caracteristicas numericas utilizando iqr
    for feature in numeric_features:
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        data[feature] = np.where((data[feature] < lower_bound) | (data[feature] > upper_bound),
                                 data[feature].mean(), data[feature])

    #normalizacion caracteristicas numericas 
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numeric_features])
    data[numeric_features] = scaler.transform(data[numeric_features])

    #manipulacion de valores faltantes en caracteristacas categoricas
    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])

    return data