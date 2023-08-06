# Appset

## Installation

### Production-ready version

`pip install appset`

for specific version use

`pip install appset==<version>`

### Staged version

`pip install --no-cache-dir --index-url https://test.pypi.org/simple/ appset==<version>`

## Development

`$ virtualenv -p python3 env`

`$ source env/bin/activate`

`ln -s <pwd of appset-modules repo>/modules ./modules`

Run tests with `$ ./run_tests.sh`

`bin/appset` is the file to be run when developing/testing (in PyCharm)

## Usage
`$ appset` lists available modules

Two flags are required: 

`--modules / -m` with path to the modules directory (appset-modules preferably) and `--env / -e` with path to secrets files (see below)

Command's format is `$ appset <submodule> <function> -p <param> --help --debug`

`--help` flag is always there

#### Secrets
Some modules require *secrets* which are credentials used somewhere during their functioning. 
Those *secrets* can be set in three separate ways:
* as `.env` file placed in the same directory your *appset* binary is placed in
* as `secrets` folder containing `*.env` files placed in the same directory your *appset* binary is placed in
* as `.env` file which path is passed as `--conf/-f` parameter
