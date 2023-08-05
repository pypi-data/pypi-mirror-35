import sys
import os


def add_data_files(*include_dirs):
    'called from setup.py to include auxillary files for installation'
    data_files = []
    for include_dir in include_dirs:
        for root, directories, filenames in os.walk(include_dir):
            include_files = []
            for filename in filenames:
                include_files.append(os.path.join(root, filename))
            if include_files:
                data_files.append((root, include_files))
    return data_files


if '__main__' == __name__:
    print('Create skeleton project...')
    basedirs = [
        'bin',
        'etc',
        'share/static',
        'share/template',
        'var/log'
        ]

    for basedir in basedirs:
        try:
            os.makedirs(basedir)
        except Exception as e:
            if e.errno != 17:
                print(e)
