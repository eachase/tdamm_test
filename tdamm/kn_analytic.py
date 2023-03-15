from .tdamm_core import TDAMMModel, ModelParameter

class AnalyticModel(TDAMMModel):
    """
    Analytic kilonova model based on Metzger Kilonova Review

    This class is heavily taken from NMMA (Michael Coughlin, et al.)
    """

    def __init__(self):
        pass

    def getParameters(self):
        return []

    def fluxDensity(self, t, nu, **kwargs):
        return 0
    


