# nsg-python-sdk

This repository contains changes for nsg-python-sdk python package. This package will be uploaded to the PyPI so that customer can install package and test their changes. 

## nsg-python-sdk package

Install nsg-python-sdk from PyPI. This package exposes nsgsdk binary. 

`pip install nsg-python-sdk`

currently nsgsdk supports running tags, variables and views app request. Supported apps can be found by running the following command.

```sh
# nsgsdk -h
Usage: nsgsdk [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  tags       run tags application
  test       run tests in the current repository
  variables  run variable builder application
  views      run views application
```

### How to run apps on local machine 

Go to the directory which contains scripts for testing.

To run module `tags` using embedded `tags_app.py`, we could use the following steps

to check the required parameters and options we can use the help option 

```sh
# nsgsdk tags -h
Usage: nsgsdk tags [OPTIONS] INPUT_DEVICE

  NetSpyGlass tags assignment Python application

Options:
  -f, --format [json|pb]  use this format to generate output  [default: json]
  -o, --output TEXT       the file name where the result should be stored; if
                          missing or equal to "-", use stdout
  -h, --help              Show this message and exit.
```

`tags` command specifies that we want to run the tags app.

then to run it with input

```sh
nsgsdk tags <path_to_input_file> -o <path_to_output_file>
```

### Run unit test cases. 

* cd to the scripts directory.
* create directory `tests` and put your test modules there. If your tests need data files, we recommend
  placing them in the directory `tests/fixtures`. Directory structure should look like this:

```
    ~/src/test-repo/scripts$ tree
    ├── __init__.py
    ├── rules.py
    ├── tags.py
    ├── tests
    │     ├── __init__.py
    │     ├── fixtures
    │     │     └── ex2200-pb.json
    │     └── test_tags.py
    ├── var_builder.py
    └── views.py
```

to run the tests, change to the directory which contains scripts directory. We can use the following command

`nsgsdk test`

To check the required parameters and option we can use the following command:

```commandline
nsgsdk test -h
Usage: nsgsdk test [OPTIONS] PATH

Options:
  -h, --help  Show this message and exit.
```

here Path can be module or directory path.

To run the tests in the directory, we can use the following command:

`nsgsdk test scripts/tests`

To run the tests in module, we can use the following command:

` nsgsdk test scripts/tests/test_tags_1.py`
