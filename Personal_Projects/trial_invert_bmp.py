import os.path
# import
bmp_filename = "vintage-halloween-bat.bmp"

with open(bmp_filename, 'r+b') as filename:
    file_header = filename.read(14)
    file_id = file_header[:2]
    # expect an error
    file_size = int.from_bytes(file_header[2:6], 'little')
    print(f'file_size is: {file_size} bytes')

    act_file_size = os.path.getsize(bmp_filename)
    print(f'actual size of the bmp file is: {act_file_size} bytes')
    offset = int.from_bytes(file_header[-4:], 'little')

    if file_id == b'BM':
        print(f'file size in file matches the act file size')
