#!/bin/python3

from pathlib import Path
from shutil import copy
from os import path, listdir
from sys import argv

gitconfig = path.join(Path.home(), '.gitconfig');
this_directory_realpath = path.dirname(path.realpath(__file__))
backup_gitconfig = path.join(this_directory_realpath, 'gitconfig.tmp.bk')
filenames = listdir(path.join(this_directory_realpath, 'users'))
limit = len(filenames)

print('# Cambiar cuenta Git\n')

for index, username in enumerate(filenames):
    print(f' {index + 1:2d} > {username}')

selector = input(f'\nSeleccione el perfil [0-{limit}] > ')

if selector != '':
    selector = int(selector)
    if selector in range(1, (limit + 1)):
        copy(gitconfig, backup_gitconfig)
        print('|| Copia de seguridad realizada.')

        new_gitconfig = path.join(this_directory_realpath, 'users', filenames[selector -1])
        copy(new_gitconfig, gitconfig)

    with open(gitconfig) as file:
        print('\n' + file.read())
