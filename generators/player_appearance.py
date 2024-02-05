import struct


def player_appearance_gen(pes_ver: int, team_amount: int, output_loc: str):
    team_id = 701
    player_appearances = []

    if pes_ver == 15:
        appearance_bin = open(r'bin\PlayerAppearance_Base_15.bin', 'rb').read()
    elif pes_ver in [16, 17, 18, 19, 20, 21]:
        appearance_bin = open(r'bin\PlayerAppearance_Base_16.bin', 'rb').read()
    else:
        raise ValueError('Unsupported PES Version.')

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
    pes_version = input('Enter the PES version of what the "Player.bin" needs to be generated for: ')
    amount = len(open('../team_list.txt', 'r').read().split('\n'))
    sixteen_plus_check = any(
        [
            '16' in pes_version, '17' in pes_version, '18' in pes_version,
            '19' in pes_version, '20' in pes_version, '21' in pes_version
        ]
    )

    if '15' in pes_version:
        player_appearance_gen(15, amount, 'PlayerAppearance.bin')
    elif sixteen_plus_check:
        player_appearance_gen(16, amount, 'PlayerAppearance.bin')
    else:
        raise ValueError('Unsupported PES Version.')
