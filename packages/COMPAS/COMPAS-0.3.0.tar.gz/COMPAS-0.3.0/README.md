# The COMPAS framework

[![Build Status](https://travis-ci.com/compas-dev/compas.svg?branch=develop)](https://travis-ci.com/compas-dev/compas)


The **COMPAS** framework is an open-source, Python-based framework for computational research and collaboration in architecture, engineering and digital fabrication.

The main library consists of a core package (**compas**) and several additional
packages for integration of the core functionality in CAD software (**compas_blender**, **compas_rhino**, **compas_ghpython**).

The core package defines all *real* functionality.
The CAD packages simply provide a unified framework for processing, visualising, and interacting with geometry and datastructures, and for building user interfaces in different CAD software.

The complete documentation of the compas framework is available at https://compas-dev.github.io/.


## Getting Started

The recommended way to install **COMPAS** is to use [Anaconda/conda](https://conda.io/docs/):

    $ conda config --add channels conda-forge
    $ conda install COMPAS

But it can also be installed using `pip`:

    $ pip install COMPAS

Once installed, you can verify your setup. Start Python from the command line and run the following:

```python

>>> import compas
>>> import compas_rhino
>>> import compas_blender
>>> import compas_ghpython

```

Optionally, you can also install from source. Check the [documentation for more details](https://compas-dev.github.io/gettingstarted.html).


## First Steps

Some useful resources for first explorations:

* https://compas-dev.github.io/main/examples.html
* https://compas-dev.github.io/main/tutorial.html
* https://compas-dev.github.io/main/reference.html


## Questions and feedback

The **COMPAS** framework has a forum: http://forum.compas-framework.org/
for questions and discussions.


## Issue tracker

If you find a bug, please help us solve it by [filing a report](https://github.com/compas-dev/compas/issues).


## Contributing

If you want to contribute, check out our [developer guidelines](https://compas-dev.github.io/devguide.html).


## License

The main library of **COMPAS** is [released under the MIT license](https://compas-dev.github.io/license.html).


## Contact

The **COMPAS** framework is developed by the Block Research Group at ETH Zurich,
with the support of the NCCR (National Centre for Competence in Research) in *Digital fabrication*.
Main contributors are Tom Van Mele, Andrew Liew, Tomás Méndez and Matthias Rippmann.

For questions, comments, requests, ..., please [contact the main developers directly](mailto:van.mele@arch.ethz.ch,liew@arch.ethz.ch,mendez@arch.ethz.ch,rippmann@arch.ethz.ch).
