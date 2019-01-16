from collections import namedtuple

VERSION = '0.0.1.dev1'

# Endianess for storing numbers
# https://zh.wikipedia.org/wiki/%E5%AD%97%E8%8A%82%E5%BA%8F
ENDIAN = 'little'
# 0x0 D0x0C 0x0B 0x0A

# Bytes used for storing references to pages
# Can address 16 TB of memory with 4 KB pages
PAGE_REFERENCE_BYTES = 4

# Bytes used for storing the type of the node in page header
NODE_TYPE_BYTES = 1

# Bytes used for storing the length of the page payload in page header
USED_PAGE_LENGTH_BYTES = 3

# Bytes used for storing the length of the key or value payload in record
# header. Limits the maximum length of a key or value to 64 KB.
USED_KEY_LENGTH_BYTES = 2
USED_VALUE_LENGTH_BYTES = 2

# Max 256 types of frames
FRAME_TYPE_BYTES = 1

# Bytes used for storing general purpose integers like file metadata
OTHERS_BYTES = 4


TreeConf = namedtuple('TreeConf', [
    'page_size',   # Size of a page within the tree in bytes
    'order',       # Branching factor of the tree
    'key_size',    # Maximum size of a key in bytes
    'value_size',  # Maximum size of a value in bytes
    'serializer',  # Instance of a Serializer
])
