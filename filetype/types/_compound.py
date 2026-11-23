"""Office stream names from the root of a bounded CFB directory.

The FAT sector marker is shared by all compound documents. Prefer an Office
stream belonging to the root storage when its directory is in the sniff window;
otherwise leave the existing signature heuristics to the caller.
"""

import struct

from ..utils import _NUM_SIGNATURE_BYTES


def document_type(buf):
    if len(buf) < 512 or buf[:8] != b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
        return None
    buf = buf[:_NUM_SIGNATURE_BYTES]

    def uint16(offset):
        return struct.unpack_from('<H', buf, offset)[0]

    def uint32(offset):
        return struct.unpack_from('<I', buf, offset)[0]

    version, shift = uint16(26), uint16(30)
    if (version, shift) not in ((3, 9), (4, 12)) or uint16(28) != 0xfffe:
        return None
    sector_size = 1 << shift
    entries_per_sector = sector_size // 128
    no_stream = 0xffffffff
    directory_sectors = [uint32(48)]

    def sector_offset(sector, size):
        offset = (sector + 1) * sector_size
        if sector >= 0xfffffffa or offset + size > len(buf):
            return None
        return offset

    def directory_entry(index):
        page, slot = divmod(index, entries_per_sector)
        # Every visited sector must be present in this small header. Directory
        # cycles and hostile indices cannot turn sniffing into an unbounded walk.
        if page >= len(buf) // sector_size:
            return None
        while len(directory_sectors) <= page:
            previous = directory_sectors[-1]
            fat_index, fat_slot = divmod(previous, sector_size // 4)
            # Only FAT sectors named in the header DIFAT are available here.
            if fat_index >= min(uint32(44), 109):
                return None
            fat = sector_offset(uint32(76 + fat_index * 4), (fat_slot + 1) * 4)
            if fat is None:
                return None
            following = uint32(fat + fat_slot * 4)
            if following in directory_sectors:
                return None
            if sector_offset(following, 128) is None:
                return None
            directory_sectors.append(following)
        start = sector_offset(directory_sectors[page], (slot + 1) * 128)
        if start is None:
            return None
        start += slot * 128
        name_length = uint16(start + 64)
        if not 2 <= name_length <= 64 or name_length % 2:
            return None
        if buf[start + name_length - 2:start + name_length] != b'\0\0':
            return None
        try:
            name = buf[start:start + name_length - 2].decode('utf-16le').lower()
        except UnicodeDecodeError:
            return None
        return (name, buf[start + 66], uint32(start + 68),
                uint32(start + 72), uint32(start + 76))

    root = directory_entry(0)
    if root is None or root[:2] != ('root entry', 5):
        return None
    pending = [root[4]]
    visited = set()
    found = set()
    office_streams = {'worddocument': 'doc', 'workbook': 'xls',
                      'book': 'xls', 'powerpoint document': 'ppt'}
    while pending:
        index = pending.pop()
        if index == no_stream:
            continue
        if index in visited:
            return None
        visited.add(index)
        item = directory_entry(index)
        if item is None or item[1] not in (1, 2):
            return None
        name, kind, left, right, _child = item
        if kind == 2 and name in office_streams:
            found.add(office_streams[name])
        # Siblings belong to the same storage; a storage's children do not.
        # An embedded presentation must not identify its outer Word/Excel file.
        pending.extend((left, right))
    return found.pop() if len(found) == 1 else None
