#  Copyright (c) modalic 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

"""Shared object types."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np

Weights = List[np.ndarray]


@dataclass
class Parameters:
    r"""Model parameters."""

    tensor: bytes
    data_type: str
    model_version: int


@dataclass
class ProcessMeta:
    r"""Meta data about the process."""

    round_id: int
    loss: float
