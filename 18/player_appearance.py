import struct

player_appearances = []
appearance_bin = open(r'Bin Files\PlayerAppearance_Base.bin', 'rb').read()
team_id = 701

for _ in range(220):
    player_index = 1
    for _ in range(23):
        assign_entry = [
            struct.pack('<I', int('{}{}'.format(team_id, f'0{player_index}' if player_index < 10 else player_index))),  # Player ID
            appearance_bin[4:]
        ]
        player_appearances.append(b''.join(assign_entry))
        player_index += 1
    team_id += 1

open('PlayerAppearance.bin', 'wb').write(b''.join(player_appearances))
