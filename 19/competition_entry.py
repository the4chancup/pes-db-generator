import re
import struct

team_list = open('../team_list.txt', 'r').read()
index = 1
fourcc_index = 1
backup_index = 1
vgl_index = 1
invitational_index = 1
competition_entries = []


def entry_gen(team_id: int, entry_index: int, competition_index: int, competition_id: int) -> bytes:
    competition_entry = [
        struct.pack('<I', int(team_id)),  # Team ID
        bytearray(2),
        struct.pack('<H', entry_index),  # Entry ID
        struct.pack('<H', competition_id),  # Competition ID
        struct.pack('<H', competition_index)  # Entry Order
    ]
    return b''.join(competition_entry)


for team_data in team_list.split('\n'):
    tid, _, tname = re.match(r'(\d{3}) (\w*) +(.*)', team_data).groups()
    if not any(['Backup' in tname, 'VGL' in tname, 'Invitational' in tname]):
        competition_entries.append(entry_gen(tid, index, fourcc_index, 9))
        fourcc_index += 1
    else:
        if 'Backup' in tname:
            competition_entries.append(entry_gen(tid, index, backup_index, 10))
            backup_index += 1
        elif 'VGL' in tname:
            competition_entries.append(entry_gen(tid, index, vgl_index, 8))
            vgl_index += 1
        elif 'Invitational' in tname:
            competition_entries.append(entry_gen(tid, index, invitational_index, 11))
            invitational_index += 1
    index += 1

open('CompetitionEntry.bin', 'wb').write(b''.join(competition_entries))
