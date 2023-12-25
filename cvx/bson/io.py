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
import json
from io import BytesIO
from typing import Any, Union

import numpy as np
import pandas as pd
import polars as pl
import pyarrow as pa


def encode(data: Union[np.ndarray, pd.DataFrame, pl.DataFrame]) -> Any:
    """
    Encode a numpy array or a pandas DataFrame

    Args:
        data: The numpy array or pandas DataFrame

    Returns: object converted into bytes
    """
    if isinstance(data, np.ndarray):
        tensor = pa.Tensor.from_numpy(obj=data)
        buffer = pa.BufferOutputStream()
        pa.ipc.write_tensor(tensor, buffer)
        return bytes(buffer.getvalue().to_pybytes())

    if isinstance(data, pd.DataFrame):
        return data.to_parquet()

    if isinstance(data, pl.DataFrame):
        result = data.write_ipc(file=None)
        result.seek(0)
        return result.read()

    converted = json.dumps(data).encode(encoding="utf-8")
    arr = bytes("cvx", "utf-8")
    return arr + converted

    # return bytes.
    # print(encoded_tuple)
    # decoded_color = encoded_color.decode()
    # orginal_form = json.load(decoded_color)
    # return

    # raise TypeError(f"Invalid Datatype {type(data)}")


def decode(data: bytes) -> Union[np.ndarray, pd.DataFrame, pl.DataFrame]:
    """
    Decode the bytes back into numpy array or pandas DataFrame

    Args:
        data: bytes

    Returns:
        The array or the frame
    """
    # reader the first few bytes
    header = data[:3]

    # ARR indicates a pl.DataFrame
    if header == b"ARR":
        return pl.read_ipc(data)

    # PAR indicates a pd.DataFrame
    if header == b"PAR":
        return pd.read_parquet(BytesIO(data))

    if header == b"cvx":
        return json.loads(data[3:].decode())

    # if still here we try numpy
    return pa.ipc.read_tensor(data).to_numpy()
