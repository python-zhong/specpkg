from argparse import ArgumentParser
from os.path import isdir, isfile, isabs
from os import getcwd
from .pack import pack
from .unpack import unpack
def main(args=None):
    if args is None:
        args = argv[1:]
    parser = ArgumentParser(description='Special Archive Packer/Unpacker')
    parser.add_argument('mode', choices=['pack', 'unpack'], help='Choice for the pack / unpack action.',
                        action='store')
    parser.add_argument('src', help='The dictionary path [Pack Mode] or The Special Archive file path [Unpack Mode]',
                        action='store')
    parser.add_argument('-s', help='Keep silent while packing / unpacking.', action='store_true')
    namespace = parser.parse_args(args)
    mode, src, silent = namespace.mode, namespace.src, namespace.s
    src = src.replace('\\', '/')
    if (mode == 'pack' and not isdir(src)) or (mode == 'unpack' and not isfile(src)):
        raise FileNotFoundError(f'No such file or dictionary: {src}')
    if not isabs(src):
        src = getcwd().removesuffix('/').replace('\\', '/') + '/' + src.removeprefix('/')
    if isdir(src) and not src.endswith('/'):
        src += '/'
    if mode == 'pack':
        pack(src, silent)
    elif mode == 'unpack':
        unpack(src, silent)
if __name__ == '__main__':
    exit(main())