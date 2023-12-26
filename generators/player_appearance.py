import struct


def player_appearance_gen(team_amount: int, output_loc: str):
    team_id = 701
    player_appearances = []
    appearance_bin = open(r'bin\PlayerAppearance_Base.bin', 'rb').read()

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int('{}{}'.format(team_id, f'0{player_index}' if player_index < 10 else player_index))
            appearance_entry = [
                struct.pack('<I', player_id),  # Player ID
                appearance_bin[4:]
            ]
            player_appearances.append(b''.join(appearance_entry))
            player_index += 1
        team_id += 1

    open(output_loc, 'wb').write(b''.join(player_appearances))


if __name__ == '__main__':
    amount = len(open('../team_list.txt', 'r').read().split('\n'))
    player_appearance_gen(amount, 'PlayerAppearance.bin')
