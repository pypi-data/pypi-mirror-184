
import numpy as np
import torch

def timespan(t: (torch.Tensor or np.ndarray)):
    return (t.max() - t.min()).item()

    
class TimeConfiguration:
    def __parse__(self, kwargs, ignore=["self"]):

        for key, val in kwargs.items():
            if not key in ignore:
                setattr(self, key, val)

    def __init__(self, t: torch.Tensor, n_steps: int = 40):
        self.__parse__(locals())

    @property
    def timespan(self):
        return timespan(self.t)

    @property
    def dt(self):
        return self.timespan / self.n_steps

    @property
    def t0(self):
        return self.t[0].item()

    @property
    def tf(self):
        return self.t[-1].item()