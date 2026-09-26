import numpy as np

def g_metric(g_tensor):
    g=np.asarray(g_tensor,float)
    if g.shape!=(3,3):
        raise ValueError("g_tensor must be 3x3")
    return g.T@g

def principal_system(g_tensor):
    G=g_metric(g_tensor)
    vals,vecs=np.linalg.eigh(G)
    order=np.argsort(vals)[::-1]
    vals=vals[order]; vecs=vecs[:,order]
    return np.sqrt(np.clip(vals,0,None)),vecs

def effective_g(g_tensor, direction):
    n=np.asarray(direction,float)
    if n.shape!=(3,) or np.linalg.norm(n)==0:
        raise ValueError("direction must be a nonzero 3-vector")
    n=n/np.linalg.norm(n)
    return float(np.sqrt(n@g_metric(g_tensor)@n))

def is_psd_gmetric(g_tensor, tol=1e-12):
    return bool(np.min(np.linalg.eigvalsh(g_metric(g_tensor))) >= -tol)

def tensor_frobenius_distance(g1, g2):
    return float(np.linalg.norm(g_metric(g1)-g_metric(g2),"fro"))
