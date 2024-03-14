import re
import struct


def team_entry_15(team_id: int, team_abbreviation: str, team_name: str) -> bytes:
    team_name_encoded = team_name.encode('utf8')
    team_name_padding = bytearray(70 - len(team_name))
    team_entry = [
        struct.pack('<I', team_id),  # Manager ID
        bytearray(4),
        struct.pack('<I', team_id),  # Team ID
        bytearray(4),
        struct.pack('<H', 29),  # Stadium ID
        struct.pack('<H', 0xFFFF),  # Team Sort Number
        struct.pack('<H', 231),  # Team Nationality
        struct.pack('<H', 0x0660),  # Anthem Style + Team Licensing
        team_name_encoded,  # Japanese Team Name
        team_name_padding,
        team_name_encoded,  # Spanish Team Name
        team_name_padding,
        team_name_encoded,  # Greek Team Name
        team_name_padding,
        team_name_encoded,  # English Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 1
        team_name_padding,
        team_name_encoded,  # Latam Team Name
        team_name_padding,
        team_name_encoded,  # French Team Name
        team_name_padding,
        team_name_encoded,  # Turkish Team Name
        team_name_padding,
        team_name_encoded,  # Portuguese Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Database Team Name
        bytearray(24 - len(team_abbreviation)),
        team_name_encoded,  # German Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Licensed Abbreviated Team Name
        bytearray(10 - len(team_abbreviation)),
        team_name_encoded,  # Brazilian Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 2
        team_name_padding,
        team_name_encoded,  # Dutch Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 3
        team_name_padding,
        team_name_encoded,  # Swedish Team Name
        team_name_padding,
        team_name_encoded,  # Italian Team Name
        team_name_padding,
        team_name_encoded,  # Russian Team Name
        team_name_padding,
        'None'.encode('utf8'),  # Fake Abbreviated Team Name
        bytearray(6),
        team_name_encoded,  # Empty Team Name 4
        team_name_padding,
        team_name_encoded,  # English US Team Name 3
        bytearray(72 - len(team_name)),
    ]
    return b''.join(team_entry)


def team_entry_19(team_id: int, team_abbreviation: str, team_name: str) -> bytes:
    team_name_encoded = team_name.encode('utf8')
    team_name_padding = bytearray(70 - len(team_name))
    team_entry = [
        struct.pack('<I', team_id),  # Manager ID
        bytearray(4),
        struct.pack('<I', team_id),  # Team ID
        bytearray(4),
        struct.pack('<H', 29),  # Stadium ID
        struct.pack('<H', 0xFFFF),  # Team Sort Number
        struct.pack('<H', 231),  # Team Nationality
        struct.pack('<H', 0x0C60),  # Anthem Style + Team Licensing
        team_name_encoded,  # Japanese Team Name
        team_name_padding,
        team_name_encoded,  # Spanish Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 1
        team_name_padding,
        team_name_encoded,  # English Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 2
        team_name_padding,
        team_name_encoded,  # Latam Team Name
        team_name_padding,
        team_name_encoded,  # French Team Name
        team_name_padding,
        team_name_encoded,  # Turkish Team Name
        team_name_padding,
        team_name_encoded,  # Portuguese Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Database Team Name
        bytearray(24 - len(team_abbreviation)),
        team_name_encoded,  # German Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Licensed Abbreviated Team Name
        bytearray(10 - len(team_abbreviation)),
        team_name_encoded,  # Brazilian Team Name
        team_name_padding,
        team_name_encoded,  # Chinese Name
        team_name_padding,
        team_name_encoded,  # Dutch Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 3
        team_name_padding,
        team_name_encoded,  # Swedish Team Name
        team_name_padding,
        team_name_encoded,  # Greek Team Name
        team_name_padding,
        team_name_encoded,  # Italian Team Name
        team_name_padding,
        team_name_encoded,  # Russian Team Name
        team_name_padding,
        'None'.encode('utf8'),  # Fake Abbreviated Team Name
        bytearray(6),
        team_name_encoded,  # Empty Team Name 4
        team_name_padding,
        team_name_encoded,  # English US Team Name 3
        team_name_padding,
    ]
    return b''.join(team_entry)


def team_entry_20(team_id: int, team_abbreviation: str, team_name: str) -> bytes:
    team_name_encoded = team_name.encode('utf8')
    team_name_padding = bytearray(70 - len(team_name))
    team_entry = [
        struct.pack('<I', team_id),  # Manager ID
        bytearray(4),
        struct.pack('<I', team_id),  # Team ID
        bytearray(48),
        struct.pack('<H', 29),  # Stadium ID
        struct.pack('<H', 0xFFFF),  # Team Sort Number
        struct.pack('<H', 231),  # Team Nationality 1
        bytearray(4),
        struct.pack('<H', 0x039C),  # Team Nationality 2
        bytearray(12),
        struct.pack('<I', 0x0C),  # Team & Kit Licensing
        team_name_encoded,  # Japanese Team Name
        team_name_padding,
        team_name_encoded,  # Spanish Team Name
        team_name_padding,
        team_name_encoded,  # Swedish Team Name
        team_name_padding,
        team_name_encoded,  # Greek Team Name
        team_name_padding,
        team_name_encoded,  # English Team Name
        team_name_padding,
        team_name_encoded,  # Latam Team Name
        team_name_padding,
        team_name_encoded,  # French Team Name
        team_name_padding,
        team_name_encoded,  # Turkish Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 1
        team_name_padding,
        team_name_encoded,  # Portuguese Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Database Team Name
        bytearray(24 - len(team_abbreviation)),
        team_name_encoded,  # German Team Name
        team_name_padding,
        team_abbreviation.encode('utf8'),  # Licensed Abbreviated Team Name
        bytearray(10 - len(team_abbreviation)),
        team_name_encoded,  # Brazilian Team Name
        team_name_padding,
        team_name_encoded,  # Chinese Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 2
        team_name_padding,
        team_name_encoded,  # Italian Team Name
        team_name_padding,
        team_name_encoded,  # Empty Team Name 3
        team_name_padding,
        team_name_encoded,  # Russian Team Name
        team_name_padding,
        team_name_encoded,  # Dutch Team Name
        team_name_padding,
        'None'.encode('utf8'),  # Fake Abbreviated Team Name
        bytearray(6),
        team_name_encoded,  # Empty Team Name 4
        team_name_padding,
        team_name_encoded,  # English US Team Name 3
        team_name_padding,
    ]
    return b''.join(team_entry)


def team_gen(pes_ver: int, team_list: list[str], output_loc: str):
    teams = []

    if pes_ver in [15, 16, 17, 18]:
        team_entry = team_entry_15
    elif pes_ver == 19:
        team_entry = team_entry_19
    elif pes_ver in [20, 21]:
        team_entry = team_entry_20
    else:
        raise ValueError('Unsupported PES Version.')

    for team_data in team_list:
        team_id, team_abbreviation, team_name = re.match(r'(\d{3}) (\w*) +(.*)', team_data).groups()
        teams.append(team_entry(int(team_id), team_abbreviation, team_name))

    open(output_loc, 'wb').write(b''.join(teams))


if __name__ == '__main__':
    pes_version = input('Enter the PES version of what the "Team.bin" needs to be generated for: ')
    data = open('../team_list.txt', 'r').read().split('\n')
    if any(['15' in pes_version, '16' in pes_version, '17' in pes_version, '18' in pes_version]):
        team_gen(15, data, 'Team.bin')
    elif '19' in pes_version:
        team_gen(19, data, 'Team.bin')
    elif ('20' in pes_version) or ('21' in pes_version):
        team_gen(20, data, 'Team.bin')
    else:
        raise ValueError('Unsupported PES Version.')
