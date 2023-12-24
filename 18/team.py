import re
import struct

teams = []
team_list = open('../team_list.txt', 'r').read()

for team_data in team_list.split('\n'):
    team_id, team_abbreviation, team_name = re.match(r'(\d{3}) (\w*) +(.*)', team_data).groups()

    team_entry = [
        struct.pack('<I', int(team_id)),  # Manager ID
        bytearray(4),
        struct.pack('<I', int(team_id)),  # Team ID
        bytearray(4),
        struct.pack('<H', 29),  # Stadium ID
        struct.pack('<H', 65535),  # Team Sort Number
        struct.pack('<H', 231),  # Team Nationality
        struct.pack('<H', 1632),  # Anthem Style + Team Licensing
        team_name.encode('utf8'),  # Japanese Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Spanish Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Greek Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # English Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Empty Team Name 1
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Latam Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # French Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Turkish Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Portuguese Team Name
        bytearray(70 - len(team_name)),
        team_abbreviation.encode('utf8'),  # Database Team Name
        bytearray(24 - len(team_abbreviation)),
        team_name.encode('utf8'),  # German Team Name
        bytearray(70 - len(team_name)),
        team_abbreviation.encode('utf8'),  # Licensed Abbreviated Team Name
        bytearray(10 - len(team_abbreviation)),
        team_name.encode('utf8'),  # Brazilian Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Empty Team Name 2
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Dutch Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Empty Team Name 3
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Swedish Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Italian Team Name
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # Russian Team Name
        bytearray(70 - len(team_name)),
        'None'.encode('utf8'),  # Fake Abbreviated Team Name
        bytearray(6),
        team_name.encode('utf8'),  # Empty Team Name 4
        bytearray(70 - len(team_name)),
        team_name.encode('utf8'),  # English US Team Name 3
        bytearray(72 - len(team_name)),
    ]
    teams.append(b''.join(team_entry))

open('Team.bin', 'wb').write(b''.join(teams))
