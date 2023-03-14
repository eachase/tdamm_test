import numpy as np
from astropy import units

class TDAMMModel:

    def __init__(self):
        pass

    def fluxDensity(self, t, nu, *args, **kwargs):
        pass

    def __call__(self, t, nu, *args, **kwargs):
        return self.fluxDensity(t, nu, *args, **kwargs)


class Dummy(TDAMMModel):

    def __init__(self):
        pass

    def fluxDensity(self, t, nu, F0, alpha, beta):
        t1d = 1.0 * units.day
        nu0 = 1.0e14 * units.Hz

        return F0 * np.power(t/t1d, alpha) * np.power(nu/nu0, beta)