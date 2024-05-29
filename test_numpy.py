import numpy as np

# Donn´ees de temps (en secondes)
t = np.array([0, 12, 29, 31, 42, 54])
# Donn´ees de vitesse (en m/s)
v = np.array([105, 154, 223, 188, 251, 229])

delta_v = np.diff(v)
delta_t = np.diff(t)
a = delta_v/delta_t
temps_v_max = t[np.argmax(v)]
distance_totale = np.trapz(v, t)
print(distance_totale)
