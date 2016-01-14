from utility import test_book, alpha_to_pin_num
from pageable import Library
import config_loader

dimensions = (28,4) #canute
config = config_loader.load()

pages = test_book(dimensions)
book_dir = config.get('files', 'library_dir')
native_file = book_dir + 'test' + Library.native_ext

with open(native_file, 'w') as fh:
    for page in pages:
        fh.write(bytearray(page))

""" used for debugging wrong sort order
# write 8 books with only one page
for page in range(8):
    native_file = book_dir + str(page) + Library.native_ext
    print(native_file)
    with open(native_file, 'w') as fh:
        fh.write(bytearray([alpha_to_pin_num(str(page))]*dimensions[0]))
"""
