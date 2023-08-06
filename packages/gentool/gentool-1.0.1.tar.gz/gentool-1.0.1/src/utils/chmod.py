# coding:  utf-8

'''Provides functions to add file permissions.

  Taken from : https://gist.github.com/gh640/bcb5cc4ba80497497f44687daa6f4276
'''


import stat
from pathlib import Path
from functools import reduce

# read:
# stat.S_IRUSR
# stat.S_IRGRP
# stat.S_IROTH

# write:
# stat.S_IWUSR
# stat.S_IWGRP
# stat.S_IWOTH

# execute:
# stat.S_IXUSR
# stat.S_IXGRP
# stat.S_IXOTH


def main():
    write_perm(Path('../../tests'), 'o')
    exec_perm(Path('../../tests'), 'ug')


def read_perm(path, target='u'):
    '''Add read permission to specified targets.
    '''
    path = Path(path)
    mode = path.stat().st_mode

    mode_map = {
        'u': stat.S_IRUSR,
        'g': stat.S_IRGRP,
        'o': stat.S_IROTH,
        'a': stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH,
    }

    for t in target:
        mode |= mode_map[t]

    path.chmod(mode)


def write_perm(path, target='u'):
    '''Add "write" permission to specified targets.
    '''
    path = Path(path)
    mode_map = {
        'u': stat.S_IWUSR,
        'g': stat.S_IWGRP,
        'o': stat.S_IWOTH,
        'a': stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH,
    }

    mode_additional = all_perms(target, mode_map)

    path.chmod(path.stat().st_mode | mode_additional)


def exec_perm(path, target='u'):
    '''Add "execute" permission to specified targets.
    '''
    mode = path.stat().st_mode

    mode_map = {
        'u': stat.S_IXUSR,
        'g': stat.S_IXGRP,
        'o': stat.S_IXOTH,
        'a': stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH,
    }

    for t in target:
        mode |= mode_map[t]

    path.chmod(mode)


def all_perms(target, mode_map):
    modes = map(lambda x: mode_map[x], target)
    return reduce(lambda x, y: x | y, modes)


if __name__ == '__main__':
    main()
