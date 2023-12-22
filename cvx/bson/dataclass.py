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
from dataclasses import dataclass
from typing import Any

from cvx.bson.file import FILE, read_bson, write_bson


@dataclass(frozen=True)
class Data:
    def to_bson(self, file: FILE) -> int:
        return write_bson(file, self.__dict__)

    @classmethod
    def from_bson(cls, file: FILE) -> Any:
        x = read_bson(file)
        return cls(**x)

    @classmethod
    def keys(cls):
        yield from cls.__dict__["__annotations__"].keys()

    def items(self):
        yield from self.__dict__.items()
