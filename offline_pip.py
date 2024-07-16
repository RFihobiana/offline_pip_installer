import os
import subprocess

import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

def install_files(directory: str, failed_dir = '.failed_installations', failed_filename = None):
    '''
    Install all `.whl` `.zip` and `.tar.gz` files in the specified directory and its 
    dependence from the same directory

    Param:
    ------
        - `directory`: Path to the directory containing .whl files. (Relative or absolute!)
        - `failed_dir`: failed file container directory. 
            File will created if its is not present
        - `failed_filename`: the new <filename>.txt to be created inside the failed_dir option.
        Default: the folder containing files to intall

    .. Note:
        - This function doesn't support multiple directory.
        We must enter directory one by one as `directory` is a string not a list of string
        - When a dependecies is missing in the given `directory`, it will enter failed installation
        file in `failed_dir/failed_failename`. It won't donwload something in the network!
    
    Example:
    --------
        ```python
        # Install necessary module
        from offline_pip import install_files

        # To install .whl and other module archive inside 'path/to/dir/'
        install_files( directory='path/to/dir' )

        # To install modules on the current directory,
        # and name failed installation instruction file 'check_it.txt'
        install_files(
            directory='.',
            failed_filename='check_it'
        )

        # Creates failure result files in directory named 'todo'
        install_files('my/modules/dir/', failed_dir='todo')
        ```
    '''

    if not os.path.exists(directory):
        print(f'Directory {directory} does not exist')
        return
    
    directory = os.path.abspath(directory)
    wheel_files = [file for file in os.listdir(directory) if file.endswith(('.whl', '.zip', '.tar.gz'))]

    if not wheel_files:
        print(f'No required file to install founded inside {directory}')
        return

    # Setup failure directory
    os.makedirs(failed_dir, exist_ok=True)
    if failed_filename is None:
        failed_filename = directory if not directory.endswith('/') else directory[:-1]
    failed_output = open(os.path.join(failed_dir, f'{os.path.basename(failed_filename)}.txt'), 'w')

    for wheel in wheel_files:
        wheel_path = os.path.join(directory, wheel)
        print(Fore.GREEN + f'Installing {wheel} in offline mode...')
        try:
            subprocess.check_call([
                'pip', 'install',
                '--no-index',
                '--find-links', directory,
                wheel_path
            ])
        except subprocess.CalledProcessError:
            failed_output.write(f'{wheel} (PATH: {wheel_path})\n')
            
            print(
                Back.YELLOW + Fore.RED +
                f'''
                    \rFailed to install {wheel}
                    \rFAILED ✖ ''')
        else:
            print(Fore.CYAN + f'{wheel} ✔')
        finally:
            print()

    failed_output.close()
    if os.stat(failed_output.name).st_size == 0:
        os.remove(failed_output.name)
