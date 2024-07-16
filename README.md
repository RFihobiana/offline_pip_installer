# Descriptions
In this program, we will attempt to install a python module .whl, .zip and .tar.gz, from
local machine! It is not limited for an independent module only. He will **find the respective dependences** of your module!!

When your module dependecies files are not already in your machine, don't worry, there is a failure manager file that will be created and the *installation continue*.
You can then read the missing one and get it in the future.

# Download and Installations
Before you run the next commands, make sure python is
installed on your machine.

Type the code bellow (or copy/past) on your terminal.
```console
$ git clone                         # clone this repo
$ cd offline_pip_installer          # enter into downloaded repo
$ pip install -r requirements.txt   # install required module
```


# Usage
You can use this as a command line or a module that will be imported.

## Usage as a command line
Suppose we have a .whl files in a `path="my_database/wheels_dir"`
```console
$ python installer.py my_database/wheels_dir
Here is a long messages depends on what happen
$ python installer.py -fd todo my_database/wheels_dir # create failed directory named todo/
$ python installer.py --failed-filename checkme my_database/wheels_dir # write failed installation result, if exists, to wheels_dir/checkme.txt
```
### Other commands
Some of the argument we just entered was optional.
For full documentations, feel free to see the help command
```console
$ python installer.py -h   # or python installer --help
usage: installer.py [-h] [-fd FAILED_DIRECTORY] [-ff FAILED_FILENAME] path

Install [.whl, .zip, .tar.gz] files and its dependencies from local files

positional arguments:
  path                  directory containing .whl, .zip, .tar.gz files

options:
  -h, --help            show this help message and exit
  -fd FAILED_DIRECTORY, --failed-directory FAILED_DIRECTORY
                        failed file container directory. File will created if its is not present
  -ff FAILED_FILENAME, --failed-filename FAILED_FILENAME
                        the new <filename>.txt to be created inside the `--failed-directory`. Default: the path name of containing the .whl files
```

## Usage as a module

### Basic
```python
# Importing module
from offline_pip import install_files

# install .whl files inside path/to/my/wheels
install_files('path/to/my/wheels')

# Now, run it.
# Then, there must be a new created directory named: ".failed_installations"
# and if there is a failure, you will see in ".failed_installations/wheels.txt" 
# the name of the failed file .whl (or other) which has the same name as file
# in "path/to/my/wheels" and the an absolute Path on your machine to path/to/my/wheels
```

### Using the same argument as installer.py
To use the same argument as installer.py module command line,
you can import the `parser` inside him.
Here is an example:

```python
from installer import parser
```

Then, use it as you like.
```python
args = parser.parse_args()
print(f'Arguments you entered: {args}')
```
