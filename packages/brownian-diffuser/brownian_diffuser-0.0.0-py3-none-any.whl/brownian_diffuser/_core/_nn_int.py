
from ._time import timespan
from ._brownian_diffuser import BrownianDiffuser


def nn_int(net, X0, t, dt=0.1, stdev=0.5, max_steps=None, return_all=False):

    n_steps = int(timespan(t) / dt)
    diffuser = BrownianDiffuser()
    return diffuser(
        net,
        X0,
        t,
        n_steps=n_steps,
        stdev=stdev,
        max_steps=max_steps,
        return_all=return_all,
    )