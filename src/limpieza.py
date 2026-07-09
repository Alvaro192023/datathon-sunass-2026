"""Limpieza y estandarizacion de las bases operativas de la EPS (Reto 1-2).

Cubre: normalizacion de sectores, deteccion/correccion de coordenadas invertidas
y construccion de timestamps completos para el calculo de tiempos de reparacion.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd


def normalizar_sector(s: object) -> str | None:
    """Colapsa cualquier variante (' S-09 ', 's09', 'S 09', 'S009') a la forma canonica 'S9'."""
    if pd.isna(s):
        return None
    s = str(s).strip().upper().replace(" ", "").replace("-", "").replace("_", "")
    m = re.match(r"^S0*(\d+)$", s)
    return f"S{int(m.group(1))}" if m else None


def detectar_invertidas(df: pd.DataFrame) -> pd.Series:
    """Marca registros con latitud/longitud evidentemente intercambiadas (Lima)."""
    return (df["latitud"] < -50) & (df["longitud"] > -50)


def corregir_invertidas(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Intercambia lat<->lon en los registros marcados; devuelve el df y el numero de correcciones."""
    m = detectar_invertidas(df)
    df.loc[m, ["latitud", "longitud"]] = df.loc[m, ["longitud", "latitud"]].values
    return df, int(m.sum())


def datetime_completo(fecha_serie: pd.Series, hora_serie: pd.Series) -> pd.Series:
    """Combina una fecha real con una hora (datetime de anio dummy) en un datetime completo."""
    f = pd.to_datetime(fecha_serie, errors="coerce")
    h = pd.to_datetime(hora_serie, errors="coerce")
    delta = (pd.to_timedelta(h.dt.hour, unit="h") +
             pd.to_timedelta(h.dt.minute, unit="m") +
             pd.to_timedelta(h.dt.second, unit="s"))
    return f + delta
