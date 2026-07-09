"""Asignacion de cuadrillas y ruteo de reparaciones (Reto 3-4).

Asigna cada fuga a la cuadrilla mas cercana y optimiza la senda diaria de cada cuadrilla
con una heuristica TSP: vecino mas cercano + mejora local 2-opt.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

Punto = tuple[float, float]


def dist_eu(p1: Punto, p2: Punto) -> float:
    """Distancia euclidiana entre dos puntos (lat, lon)."""
    return float(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def asignar_cuadrilla_mas_cercana(lat: float, lon: float, cuadrillas: pd.DataFrame) -> tuple[str, float]:
    """Devuelve (codigo, distancia) de la cuadrilla mas cercana a un punto dado."""
    d = np.sqrt((cuadrillas["latitud"] - lat) ** 2 + (cuadrillas["longitud"] - lon) ** 2)
    idx = d.idxmin()
    return cuadrillas.loc[idx, "codigo"], float(d.loc[idx])


def ruta_total(orden: list[int], puntos: list[Punto], origen: Punto) -> float:
    """Longitud total de la ruta cerrada origen -> puntos[orden] -> origen."""
    pts = [origen] + [puntos[i] for i in orden] + [origen]
    return sum(dist_eu(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def nearest_neighbor(puntos: list[Punto], origen: Punto) -> list[int]:
    """Construye una ruta inicial por vecino mas cercano desde el origen."""
    pendientes = list(range(len(puntos)))
    orden: list[int] = []
    actual = origen
    while pendientes:
        i_best = min(pendientes, key=lambda i: dist_eu(actual, puntos[i]))
        orden.append(i_best)
        pendientes.remove(i_best)
        actual = puntos[i_best]
    return orden


def two_opt(orden: list[int], puntos: list[Punto], origen: Punto, max_iter: int = 300) -> tuple[list[int], float]:
    """Mejora la ruta por 2-opt swaps hasta un optimo local (o max_iter)."""
    mejor = orden[:]
    mejor_dist = ruta_total(mejor, puntos, origen)
    n = len(mejor)
    mejorado, it = True, 0
    while mejorado and it < max_iter:
        mejorado = False
        it += 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                nuevo = mejor[:i] + mejor[i:j + 1][::-1] + mejor[j + 1:]
                nd = ruta_total(nuevo, puntos, origen)
                if nd < mejor_dist - 1e-9:
                    mejor, mejor_dist = nuevo, nd
                    mejorado = True
    return mejor, mejor_dist
