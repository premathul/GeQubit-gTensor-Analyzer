import numpy as np
from .core import effective_g, principal_system

def direction_from_angles(theta_deg, phi_deg):
    t,p=np.deg2rad([theta_deg,phi_deg])
    return np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])

def angular_map(g_tensor, theta_deg, phi_deg):
    out=np.empty((len(theta_deg),len(phi_deg)))
    for i,t in enumerate(theta_deg):
        for j,p in enumerate(phi_deg):
            out[i,j]=effective_g(g_tensor,direction_from_angles(t,p))
    return out

def principal_axis_misalignment_deg(g1, g2):
    _,a=principal_system(g1); _,b=principal_system(g2)
    angles=[]
    for i in range(3):
        c=np.clip(abs(np.dot(a[:,i],b[:,i])),0,1)
        angles.append(np.degrees(np.arccos(c)))
    return np.array(angles)

def ensemble_effective_g(tensors, direction):
    return np.array([effective_g(g,direction) for g in tensors],float)
