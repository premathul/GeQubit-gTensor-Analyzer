import numpy as np
from gequbit_gtensor.core import principal_system, effective_g, tensor_frobenius_distance
from gequbit_gtensor.analysis import principal_axis_misalignment_deg

def test_diagonal_principal_values():
    vals,_=principal_system(np.diag([1.,2.,3.]))
    assert np.allclose(vals,[3,2,1])

def test_effective_axis():
    assert np.isclose(effective_g(np.diag([1.,2.,3.]),[0,0,1]),3)

def test_zero_distance():
    g=np.diag([1.,2.,3.])
    assert tensor_frobenius_distance(g,g)==0

def test_zero_misalignment():
    g=np.diag([1.,2.,3.])
    assert np.allclose(principal_axis_misalignment_deg(g,g),0)
