#    Copyright 2023 Stanford University Convex Optimization Group
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""JSON encoder for NumPy data types.

This module provides a custom JSON encoder that can handle NumPy data types
by converting them to standard Python types that can be serialized to JSON.
"""

import json

import numpy as np


class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy data types."""

    def default(self, obj):
        """Handle numpy types by converting them to Python standard types.

        Args:
            obj: The object to encode

        Returns:
            A JSON serializable version of the object
        """
        # Integer types
        if isinstance(
            obj,
            np.int_
            | np.intc
            | np.intp
            | np.int8
            | np.int16
            | np.int32
            | np.int64
            | np.uint8
            | np.uint16
            | np.uint32
            | np.uint64,
        ):
            return int(obj)

        # Float types
        elif isinstance(obj, np.float16 | np.float32 | np.float64):
            return float(obj)

        # Complex types
        elif isinstance(obj, np.complex64 | np.complex128):
            return {"real": obj.real, "imag": obj.imag}

        # Array types
        elif isinstance(obj, np.ndarray):
            return obj.tolist()

        # Boolean types
        elif isinstance(obj, np.bool_):
            return bool(obj)

        # Void type
        elif isinstance(obj, np.void):
            return None

        # Fall back to the default encoder
        return json.JSONEncoder.default(self, obj)
