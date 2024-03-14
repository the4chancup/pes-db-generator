import struct

team_id = 701
players = []
amount = len(open('../team_list.txt', 'r').read().split('\n'))
player_bin = open(r'Bin Files\Player_Edit_Base_19.bin', 'rb').read()
appearance_bin = open(r'Bin Files\PlayerAppearance_Base.bin', 'rb').read()

for _ in range(amount):
    player_index = 1
    for _ in range(23):
        player_id = int(f'{team_id}{f'0{player_index}' if player_index < 10 else player_index}')
        player_entry = [
            struct.pack('<I', player_id),
            struct.pack('<I', player_id),
            player_bin[8:],
            struct.pack('<I', player_id),
            bytearray(8),
            appearance_bin[4:],
            bytearray(4)
        ]
        players.append(b''.join(player_entry))
        player_index += 1
    team_id += 1

open('Player_Edit.bin', 'wb').write(b''.join(players))
