from io import BytesIO
from json import JSONDecoder
from os import mkdir
from os.path import isdir
from shutil import rmtree
decoder = JSONDecoder()
def unpack(filename: str, silent: bool) -> None:
    f = open(filename, 'rb')
    json = ''
    if not silent:
        print('Reading index ...')
    while True:
        i = f.read(1)
        if i == bytes([0x0]):
            res = decoder.decode(json)
    if isdir(filename + '.unpacked'):
        if not silent:
            print('Warning: Output folder exists. New data will cover it.')
        rmtree(filename + '.unpacked')
    mkdir(filename + '.unpacked')
    def unpack_one(fileData: bytes, fileIndex: dict, dst: str) -> None:
        dst = dst.replace('\\', '/').removesuffix('/') + '/'
        for name in fileIndex:
            info = fileIndex[name]
            if 'offset' in info and 'size' in info:
                if not silent:
                    print('Extracting file:', dst + name, end=' ... ')
                try:
                    bi = BytesIO(fileData)
                    offset = int(info['offset'])
                    size = int(info['size'])
                    bi.read(offset)
                    f = open(dst + name, 'wb')
                    f.write(bi.read(size))
                    f.close()
                    bi.close()
                    if not silent:
                        print('done.')
                except:
                    if not silent:
                        print('failed.')
                        continue
            elif 'files' in info:
                if not silent:
                    print('Output Dictionary:', dst + name)
                mkdir(dst + name)
                unpack_one(fileData, info['files'], dst + name + '/')
            else:
                if not silent:
                    print('Warning: Bad index for file:', name)
                    open(dst + 'name', 'wb').close()
    unpack_one(f.read(), res['files'], filename + '.unpacked')
    f.close()
    if not silent:
        print('Output Dictionary:', filename + '.unpacked')