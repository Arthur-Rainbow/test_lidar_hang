import numpy as np


def estimer_z_toit(xy, tree, Z, k=20):
    # Cette fonction sert à estimer la hauteur d'un point (x, y) donné quelconque.

    k_eff = min(k, len(Z))
    _, indices = tree.query(xy, k=k_eff)

    z = Z[np.array(indices)]
    return float(np.median(z))
