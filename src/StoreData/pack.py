from json import JSONEncoder
from os import listdir
from os.path import isfile, isdir, getsize
encoder = JSONEncoder()
def pack(path: str, silent: bool) -> None:
    def encode_one(dirPath: str, data: bytes = b'', offset: int = 0) -> tuple[dict, bytes, int]:
        index = {}
        dirPath = dirPath.replace('\\', '/').removesuffix('/') + '/'
        d = listdir(dirPath)
        for i in d:
            if isfile(dirPath + i):
                if not silent:
                    print('Adding File:', dirPath + i, end=' ... ')
                try:
                    f = open(dirPath + i, 'rb')
                    data += f.read()
                    f.close()
                    size = getsize(dirPath + i)
                    index[i] = {
                        'offset': str(offset),
                        'size': str(size)
                    }
                    offset += size
                    if not silent:
                        print('done.')
                except:
                    if not silent:
                        print('failed.')
            elif isdir(dirPath + i):
                if not silent:
                    print('Add Dictionary:', dirPath + i)
                ind, data, offset = encode_one(dirPath + i + '/', data, offset)
                index[i] = {'files': ind}
            else:
                continue
        return index, data, offset
    index, data, _ = encode_one(path, bytes([0x0]))
    index_byte = encoder.encode({"files": index}).encode()
    file_data = index_byte + data
    filename = path.replace('\\', '/').removesuffix('/') + '.archive'
    if not silent:
        print('Output File:', filename)
    f = open(filename, 'wb')
    f.write(file_data)
    f.close()