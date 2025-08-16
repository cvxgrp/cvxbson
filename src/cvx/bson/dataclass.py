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
"""Dataclass utilities for BSON serialization and deserialization."""

from dataclasses import dataclass
from typing import Any

from .file import FILE, read_bson, write_bson


@dataclass(frozen=True)
class Data:
    """Base class for dataclasses that can be serialized to and from BSON.

    This class provides methods for serializing to BSON files and deserializing from BSON files.
    """

    def to_bson(self, file: FILE) -> int:
        """Serialize this object to a BSON file.

        Args:
            file: Path to the file where the data will be written

        Returns:
            Number of bytes written
        """
        return write_bson(file, self.__dict__)

    @classmethod
    def from_bson(cls, file: FILE) -> Any:
        """Create an instance of this class from a BSON file.

        Args:
            file: Path to the BSON file to read

        Returns:
            An instance of this class
        """
        x = read_bson(file)
        return cls(**x)

    @classmethod
    def keys(cls):
        """Get the field names of this dataclass.

        Yields:
            Field names defined in the class annotations
        """
        yield from cls.__dict__["__annotations__"].keys()

    def items(self):
        """Get the field names and values of this dataclass instance.

        Yields:
            Pairs of (field_name, field_value)
        """
        yield from self.__dict__.items()
