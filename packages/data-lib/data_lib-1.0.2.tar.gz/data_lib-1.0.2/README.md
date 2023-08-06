# Data library for python. Helping people with reading writing and manipulation of data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
1) python3
2) pip3
3) serial
```

### Installing

```
1) apt-get install python3
2) apt-get install pip3
3) pip3 install --user python-asip-client --upgrade
3.1) pip3 install --user . --no-cache-dir (When installing local files, development mode)
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

This package is deployed on pip global server. In order to make new release, please follow below:

```
In case of there is an existing buid it can be removed by follwoing command:
1) rm -r build/ dist/ data_lib.egg-info
2) python3 setup.py sdist bdist_wheel
3) twine upload --repository pypi dist/*     Note using this command make sure you have installed twine and config file.

```
## Built With
```
?
```
## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [PEP 440](https://www.python.org/dev/peps/pep-0440/) for versioning.
PEP 440 Version Identification and Dependency Specification

## Authors

* **Adam Jarzebak** - *Computer Scientists* - [Github](https://github.com/jarzab3)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

