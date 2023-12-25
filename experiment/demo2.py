import bson as bson
import numpy as np

from cvx.bson.io import encode

if __name__ == "__main__":
    file = "xxx2.bson"
    d = dict()

    array = np.random.rand(5, 3)
    d["aa"] = encode(array)

    array = np.random.rand(500, 300)
    d["bb"] = encode(array)

    with open(file=file, mode="wb") as bson_file:
        bson_file.write(bson.dumps(d))

    with open(file=file, mode="rb") as bson_file:
        # bbb = bson_file.read()
        xxx = bson.loads(bson_file.read())
        print(type(xxx))
        print(xxx.keys())
