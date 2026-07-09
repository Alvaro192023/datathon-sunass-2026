"""Tests de asignacion de cuadrillas y ruteo TSP (src/ruteo.py)."""
import pandas as pd

from src.ruteo import asignar_cuadrilla_mas_cercana, dist_eu, nearest_neighbor, ruta_total, two_opt


def test_dist_eu():
    assert dist_eu((0, 0), (3, 4)) == 5.0


def test_asignar_cuadrilla_mas_cercana():
    cuadrillas = pd.DataFrame({"codigo": ["C1", "C2"], "latitud": [0.0, 10.0], "longitud": [0.0, 10.0]})
    cod, d = asignar_cuadrilla_mas_cercana(0.5, 0.5, cuadrillas)
    assert cod == "C1"
    assert d < 1.0


def test_nearest_neighbor_visita_todos():
    puntos = [(0, 1), (1, 1), (1, 0), (2, 2)]
    orden = nearest_neighbor(puntos, origen=(0, 0))
    assert sorted(orden) == list(range(len(puntos)))


def test_two_opt_no_empeora_la_ruta():
    puntos = [(0, 1), (2, 2), (0, 0.1), (2, 0)]  # orden inicial con cruce
    origen = (0, 0)
    nn = nearest_neighbor(puntos, origen)
    _, d_two = two_opt(nn, puntos, origen)
    assert d_two <= ruta_total(nn, puntos, origen) + 1e-9
