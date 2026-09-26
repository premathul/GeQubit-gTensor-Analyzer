"""Reconstruct G=g.T@g from direction-dependent effective g measurements."""
import argparse
import csv
import numpy as np

def fit(directions, g_effective):
    u = np.asarray(directions, dtype=float)
    y = np.asarray(g_effective, dtype=float)
    if u.ndim != 2 or u.shape[1] != 3 or len(u) != len(y) or len(y) < 6:
        raise ValueError("Need >= 6 matched three-component directions and g values")
    if np.any(~np.isfinite(u)) or np.any(~np.isfinite(y)) or np.any(y < 0):
        raise ValueError("Inputs must be finite; g must be nonnegative")
    norms = np.linalg.norm(u, axis=1)
    if np.any(norms == 0):
        raise ValueError("Zero direction")
    u = u / norms[:,None]
    x,yz,z = u.T
    a = np.column_stack((x*x,yz*yz,z*z,2*x*yz,2*x*z,2*yz*z))
    if np.linalg.matrix_rank(a) != 6:
        raise ValueError("Directions cannot identify six independent tensor terms")
    p = np.linalg.lstsq(a, y*y, rcond=None)[0]
    G = np.array([[p[0],p[3],p[4]],[p[3],p[1],p[5]],[p[4],p[5],p[2]]])
    eigenvalues, axes = np.linalg.eigh(G)
    residual = np.linalg.norm(a@p - y*y) / np.sqrt(len(y))
    return G, eigenvalues, axes, residual

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv_file", help="Header: bx,by,bz,g_eff")
    args = p.parse_args()
    with open(args.csv_file, newline="") as f:
        rows = list(csv.DictReader(f))
    directions = [[float(row[k]) for k in ("bx","by","bz")] for row in rows]
    values = [float(row["g_eff"]) for row in rows]
    G, eig, axes, residual = fit(directions, values)
    print("G=\n",G,"\nprincipal_g=",np.sqrt(np.maximum(eig,0)),
          "\nprincipal_axes_columns=\n",axes,"\nRMS_squared_g_residual=",residual)
    if np.min(eig) < -1e-10:
        print("WARNING: fitted G is not positive semidefinite; input/model needs review.")
if __name__ == "__main__":
    main()
