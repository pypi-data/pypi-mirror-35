from abc import ABC, abstractmethod
import torch.nn as nn


class BaseArch(nn.Module, ABC):
    def __init__(self, state_info, action_info, output_layer):
        super().__init__()
        self.state_info = state_info
        self.action_info = action_info
        self.output_layer = output_layer

        self.body = self.create_body()
        self.head = self.create_head()

    @abstractmethod
    def create_body(self):
        pass

    @abstractmethod
    def create_head(self):
        pass

    @property
    def input_shape(self):
        return self.state_info.shape

    @property
    def action_shape(self):
        return self.action_info.shape

    def forward(self, x):
        return self.head(self.body(x))

    @classmethod
    def from_env(cls, env, output_layer, **kwargs):
        return cls(
            state_info=env.state_info,
            action_info=env.action_info,
            output_layer=output_layer,
            **kwargs
        )
