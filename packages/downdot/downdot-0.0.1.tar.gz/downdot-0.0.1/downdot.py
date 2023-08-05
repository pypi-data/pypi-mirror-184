import argparse
import subprocess
import pip

# Set up the argument parser to parse the command-line arguments
parser = argparse.ArgumentParser(description='Install a package using downdot')
parser.add_argument('package', help='The name of the package to install')
parser.add_argument('--conda', action='store_true', help='Install using conda')
parser.add_argument('init', action='store_true', help='Initialize downdot and install conda')

# Parse the command-line arguments
args = parser.parse_args()

if args.conda:
    # Install the package using conda
    subprocess.run(['conda', 'install', '--option', args.package])
elif args.init:
    subprocess.run(['pip', 'install', 'conda'])
else:
    # Install the package using pip
    pip.main(['install', args.package])

  