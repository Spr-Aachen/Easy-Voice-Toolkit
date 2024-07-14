import os


def create_directories(
    *directories
):
    '''
    Create csv directory
    '''
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory, exist_ok = True)
            except OSError:
                print('Creation of directory %s failed' %directory)