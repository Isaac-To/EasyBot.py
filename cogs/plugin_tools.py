import os

def install(library_name):
    os.system(f'pip install {library_name} /dev/null 2>&1')
    os.system(f'pip3 install {library_name} /dev/null 2>&1')
    print(f'Library {library_name} has been installed')

def install_multiple(libraries):
    for library in libraries:
        install(library)