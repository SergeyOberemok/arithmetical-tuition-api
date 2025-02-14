# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python [conda env:base] *
#     language: python
#     name: conda-base-py
# ---

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# ---

T = TypeVar('T')


# ## Generic

class Strategy(ABC, Generic[T]):
    @abstractmethod
    def doAlgorithm(self) -> T:
        pass
