# ITK `itk-stubs` implementation

This repo contains manually constructed python interface (.pyi) files that can be
used by IDE's to provide type hinting and static analysis checking.

This folows the guidelines of the `PEP-0561` https://www.python.org/dev/peps/pep-0561/

# Installation
Place this repository adjacent to the `itk` python package (typically in the site-packages folder) or adjacent to the
WrapITK.pth file on the PYTHONPATH.

# How was this repository initialized

```bash
cd Dashboard/src/ITK-bld/Wrapping/Generators/Python
# Need to add empty __init__.py so that mypy stubgen
# recognizes the itk/support as a subpackage
touch itk/support/__init__.py

# Note: stubgen may need to be modified to increase timeout
# when LAZYLOADING takes too long
PYTHONPATH=~/src/mypy ITK_PYTHON_LAZYLOADING=False ~/src/mypy/mypy/stubgen.py -p itk -o stubgen_output

# Create itk-stubs link as specified in https://www.python.org/dev/peps/pep-0561/
ln -s stubgen_output/itk itk-stubs

cd itk-stubs
# Manually modify files to provide the interface to the swig generated code.
```
