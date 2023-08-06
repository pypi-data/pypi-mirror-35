# Pylint Topology

Validate your package dependencies as a topological graph.


## Installation

```
pip install pylint-topology
```


## Configure

Add `module-topology` settings to your `.pylintrc`:

```
# List of module names for which are in a certain topology. Module imports should be forwards.
module-topology=
    utils,
    core,
    user,
    business,
    order,
```


## Usage

```
pylint --load-plugins pylint_topology
```


## License

GPLv2
