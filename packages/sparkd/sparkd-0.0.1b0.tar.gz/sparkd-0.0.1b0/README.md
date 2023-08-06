# Spark Networks DevOps coding challenge

https://gitlab.com/askainet/spark-networks-code-challenge

Requirements
------------

- Python >= 3.4

Install
-------

From public Pypi repository:

```
pip install sparkd
```

Demo
----

```
docker build . -t sparkd

docker run -it -e RETRIES=5 sparkd demo.sh
```

Usage
-----

```
usage: sparkd [-h] [--version] [-l LOGFILE]
              [--command-logfile COMMAND_LOGFILE] [-n NAME] [-v] [-d]
              [-r RETRIES] [-i RETRY_INTERVAL] [-c CHECK_INTERVAL]
              [command] [arguments [arguments ...]]

Run any command as a daemon and supervise it

positional arguments:
  command               The command to run as a daemon to supervise
  arguments             Arguments to the command

optional arguments:
  -h, --help            show this help message and exit
  --version             Show version
  -l LOGFILE, --logfile LOGFILE
                        Set the logfile for the Sparkd supervisor
  --command-logfile COMMAND_LOGFILE
                        Set the logfile for the command to supervise
  -n NAME, --name NAME  Set the name of this Sparkd instance
  -v, --verbose         Enable verbose logging
  -d, --debug           Enable debug logging
  -r RETRIES, --retries RETRIES
                        Number of retries to restart the process
  -i RETRY_INTERVAL, --retry-interval RETRY_INTERVAL
                        Seconds to wait between retries to restart the process
  -c CHECK_INTERVAL, --check-interval CHECK_INTERVAL
                        Seconds to wait between checking process status
```

Developing
----------

### Tests

Some basic tests have been added to have coverage only for the `Process` class,
just to demonstrate how to use `unittest` with Python.

```
make test
```

### Linting

Linting with `pylint` to keep a nice and healthy code.

```
make lint
```

### Publish to Pypi

Package and publish to Pypi repository.

```
make dist
```

### Install from source

```
make install
```

### Documentation

Documentation is built using `sphinx` based on docstrings present in the code.

Readthedocs integration is configured to automatically generate and upload
docs to https://sparkd.readthedocs.io/en/latest/ on updates to master branch.

Manual local docs generation is possible running `make docs`
