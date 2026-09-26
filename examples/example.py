import numpy as np
from gequbit_gtensor.core import principal_system
from gequbit_gtensor.analysis import angular_map

g=np.diag([0.2,0.4,7.5])
values,axes=principal_system(g)
print("principal g values:",values)
m=angular_map(g,np.linspace(0,180,19),np.linspace(0,360,37))
print("range:",m.min(),m.max())
