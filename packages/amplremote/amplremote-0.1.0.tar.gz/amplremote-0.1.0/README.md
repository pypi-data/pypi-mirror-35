### AMPL Remote Driver (REST API)

AMPL Remote Driver is a solver driver for AMPL based on a REST API that
allows solving models on a remote machine while using AMPL on a local machine.

#### Documentation

- http://amplremote.readthedocs.io

#### Examples

On the remote machine: Start the server on remote machine where the models will be solved:
```bash
$ amplserver [port]
```
Or:
```bash
$ python -m amplremote.server [port]
```
Default port: 5000.

Load the model on the local machine and send it to the server using `option solver remote;`.
```ampl
ampl: model diet.mod;
ampl: data diet.dat;
ampl: option solver remote;
ampl: option remote_options 'solver=gurobi'; # solver to be used on the server
ampl: option gurobi_options 'outlev=1';
ampl: solve;
``` 

Other options that can also be set:
```ampl
ampl: option remote_options "solver='gurobi' user='admin' pass='secret' url='http://127.0.0.1:5000/api/'";
```

#### Repositories

- GitHub Repository: https://github.com/ampl/ampl-remote
- PyPI Repository: https://pypi.python.org/pypi/amplremote

#### Setup

Install from the [repository](https://pypi.python.org/pypi/amplpy):
```
$ pip install amplremote
```
Or:
```
$ python -m pip install amplremote
```

Alternatively, you can build and install the package locally:
```
$ git clone git@github.com:ampl/ampl-remote.git
$ cd ampl-remote
$ python setup.py build
$ pip install . --upgrade
```

#### License

BSD-3

***
Copyright © 2018 AMPL Optimization inc. All rights reserved.
