# LBSNSTRUCTURE

A python compiled version of the [common lbsn data structure concept](https://gitlab.vgiscience.de/lbsn/concept) (ProtoBuf) to handle cross network Social Media data in Python.

## Quick Start

Install with:  
```shell
pip install --upgrade lbsnstructure
```

Import to python projecty with:  
```python
import lbsnstructure
```

.. or, for non-developers, compile newest version from [Protofiles](https://gitlab.vgiscience.de/lbsn/concept)

1. Clone git Repository `git clone git@gitlab.vgiscience.de/lbsn/concept`
2. Install [Protocoll Buffers](https://github.com/google/protobuf/releases)
3. Compile structure to python package `protoc --python_out=examples/python lbsnstructure/structure.proto`  
4. Install with `pip install .` in examples/python

## License

This project is licensed under the  MIT License.