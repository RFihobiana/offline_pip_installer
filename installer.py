'''
Install python modules from ['.whl', '.zip', '.tar.gz'] files.
'''
import argparse
from offline_pip import install_files

parser = argparse.ArgumentParser(description='Install [.whl, .zip, .tar.gz] files and its dependencies from local files')

parser.add_argument(
    dest='path',
    type=str,
    help='directory containing .whl, .zip, .tar.gz files'
)

parser.add_argument(
    '-fd', '--failed-directory',
    type=str,
    help='''failed file container directory.
        \rFile will created if its is not present''',
    default='.failed_installations')

parser.add_argument(
    '-ff', '--failed-filename',
    type=str,
    help='''the new <filename>.txt to be created inside the `--failed-directory`.
        \rDefault: the path name of containing the .whl files'''
)

if __name__ == '__main__':
    args = parser.parse_args()
    d = args.path
    if d is None:
        parser.print_help()
        exit()
    install_files(directory=d, failed_dir=args.failed_directory, failed_filename=args.failed_filename)

