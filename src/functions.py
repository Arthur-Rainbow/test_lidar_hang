import numpy as np


def estimer_z_toit(xy, tree, Z, k=20):
    # Cette fonction sert à estimer la hauteur d'un point (x, y) donné quelconque.

    k_eff = min(k, len(Z))
    _, indices = tree.query(xy, k=k_eff)

    z = Z[np.array(indices)]
    return float(np.median(z))

def triangle_max_edge_length(coords_2d):
    a = np.linalg.norm(coords_2d[0] - coords_2d[1])
    b = np.linalg.norm(coords_2d[1] - coords_2d[2])
    c = np.linalg.norm(coords_2d[2] - coords_2d[0])
    return max(a, b, c)