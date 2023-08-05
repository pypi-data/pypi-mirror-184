# pyPhases

A small framework for python projects that are mainly progress based.

The main princible of the framework are `Phases`.

# Architecure

![arch](assets/achitektur.svg)

## Project

A Project is the composition of phases and the backend.

## Phase
A Phase has a `main` Method and can export data.

## Decorators

# Compontents

## Exporters

### Exporter

There is a default `PickleExporter` and is compatible with primitive types.

### register Data
When a phase wants to register data (`self.project.registerData("myDataId", myData)` within the phase), the data is passed to an exporter. If an exporter is found the data will be passed to alle the storages. They will save the data somewhere (persitent or not).

example:

![seq](assets/seq-save-data.svg)

### reading the data
A phase can request data with `self.project.getData("myDataId", MyDataType)`. The Data will be passed sequentially to the storage layer and will pass the data from the first storage that can get it. If no storage can provide the data, the project will search for a phase that exports this data-id and run that specific phase.

example:

![get-data](assets/seq-get-data.svg)


### example

This is a example data layer with 3 storages: memory, file, database (`not default`)
![data-layer](assets/data-layer.svg)


# development

## build

`python setup.py sdist bdist_wheel`

## publish

`twine upload dist/*`

## documentation

`sphinx-apidoc -o docs/source pyPhases`
`sphinx-build -b html docs/source docs/build`


# test
`python -m unittest discover -v`
