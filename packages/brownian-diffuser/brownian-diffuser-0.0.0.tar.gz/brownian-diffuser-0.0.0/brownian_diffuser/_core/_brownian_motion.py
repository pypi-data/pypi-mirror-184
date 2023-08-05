
# -- import packages: --------------------------------------------------------------------
import torch


# -- main module class: ------------------------------------------------------------------
class BrownianMotion:
    def __parse__(self, kwargs, ignore=["self"]):

        for key, val in kwargs.items():
            if not key in ignore:
                setattr(self, key, val)

    def __init__(self, X_state: torch.Tensor, stdev: float, n_steps: int) -> None:

        """
        Brownian Motion class

        Parameters:
        -----------
        X_state
            Representative cell state of shape: (n_cells, n_dim)
            type: torch.Tensor
        stdev
            parameter specifying the magnitude of brownian motion
        n_steps
            Number of brownian "steps" to be generated

        Returns:
        --------
        z
            Brownian motion tensor of size: (n_steps, n_cells, n_dim)
            type: torch.Tensor
        """

        self.__parse__(locals())

    @property
    def state_shape(self) -> list:
        return list(self.X_state.shape)

    @property
    def temporal_state_shape(self) -> list:
        return [self.n_steps] + self.state_shape

    def __call__(self):
        """Create brownian motion Tensor."""
        return torch.randn(self.temporal_state_shape, requires_grad=True) * self.stdev

    def __repr__(self):
        return "Brownian Motion Generator"