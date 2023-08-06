# gcspy: Glasgow Constraint Solver Python Interface
A python interface for the Glasgow Constraint Solver, a CP solver implemented as part of research into pseudo-Boolean proof-logging and auditable constraint solving. This API is primarily intended for use by the [CPMpy](https://cpmpy.readthedocs.io/en/latest/index.html)
modelling library. Essentially it wraps all the relevant functionality in a single
class defined in api.hh/api.cc using only standard library types, and then generates
bindings for the methods using [pybind11](https://pybind11.readthedocs.io/en/latest/) (added using FetchContent in CMake).

## How to install
```
pip3 install gcspy
```
or clone this repository, make it current working directory and do

```
pip3 install .
```