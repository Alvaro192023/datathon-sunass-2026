"""Tests de la limpieza de datos operativos (src/limpieza.py)."""
import numpy as np
import pandas as pd
import pytest

from src.limpieza import corregir_invertidas, detectar_invertidas, normalizar_sector


@pytest.mark.parametrize("entrada,esperado", [
    (" S-09 ", "S9"), ("s09", "S9"), ("S 09", "S9"), ("S009", "S9"), ("S12", "S12"),
])
def test_normalizar_sector_variantes(entrada, esperado):
    assert normalizar_sector(entrada) == esperado


def test_normalizar_sector_invalidos():
    assert normalizar_sector(np.nan) is None
    assert normalizar_sector("basura") is None


def test_detectar_y_corregir_invertidas():
    df = pd.DataFrame({"latitud": [-77.0, -12.0], "longitud": [-12.0, -77.0]})
    mask = detectar_invertidas(df)
    assert mask.tolist() == [True, False]
    df2, n = corregir_invertidas(df.copy())
    assert n == 1
    assert detectar_invertidas(df2).sum() == 0
    assert df2.loc[0, "latitud"] == -12.0 and df2.loc[0, "longitud"] == -77.0
