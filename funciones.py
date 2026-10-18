
import numpy as np
from scipy import stats
from joblib import Parallel, delayed


def calcular_metricas(df, columna):
    """Calcula métricas básicas de una columna numérica."""

    datos = df[columna].dropna().to_numpy()

    return {
        "promedio": np.mean(datos),
        "mediana": np.median(datos),
        "desviacion_estandar": np.std(datos)
    }


def analizar_distribucion(df, columna):
    """Describe estadísticamente los datos de una columna."""

    datos = df[columna].dropna().to_numpy()

    resultado = stats.describe(datos)

    return {
        "cantidad": resultado.nobs,
        "minimo": resultado.minmax[0],
        "maximo": resultado.minmax[1],
        "promedio": np.mean(datos)
    }


def _promedio_grupo(nombre, grupo, columna):
    """Calcula el promedio para un grupo."""

    return {
        "region": nombre,
        "promedio": grupo[columna].mean()
    }


def promedio_por_region(df, columna="latencia_ms"):
    """Calcula el promedio por región usando Joblib."""

    grupos = list(df.groupby("region"))

    resultados = Parallel(n_jobs=-1)(
        delayed(_promedio_grupo)(nombre, grupo, columna)
        for nombre, grupo in grupos
    )

    return resultados