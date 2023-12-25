import struct

team_id = 701
players = []
player_bin = open(r'Bin Files\Player_Base.bin', 'rb').read()

for _ in range(220):
    player_index = 1
    for _ in range(23):
        player_id = int('{}{}'.format(team_id, f'0{player_index}' if player_index < 10 else player_index))
        player_entry = [
            bytearray(4),
            struct.pack('<I', player_id),
            player_bin[8:]
        ]
        players.append(b''.join(player_entry))
        player_index += 1
    team_id += 1

open('Player.bin', 'wb').write(b''.join(players))
