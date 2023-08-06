# Bennellick Engineering Limited Kit Drivers

This python package consists of various driver classes used by BEL to control pieces of test equipment.

## Machine-wide install for development

~~~
#!bash
pip install -U --user -e .
~~~

This will install the package in 'editable' mode (`-e`), which means any changes made in this repository will be available immediately to all scripts importing the package. The above command only needs to be re-run if changes are made to `setup.py`.

## Usage

Once installed, the package `bennellickeng` can be imported and used. See the [examples](examples) directory for examples of usage.

As well as installing a python package some command line utilities are also installed:

### `bel-scopegrab`

Grab screenshot of a scope over USB:

~~~
#!bash
bel-scopegrab foobar
# foobar.png will have been created
~~~

## Releasing

This project uses zest.releaser to manage packaging and releases. Simply run 'fullrelease' from within the pipenv.
