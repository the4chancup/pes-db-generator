import struct


def player_entry_15(player_id: int, player_bin: bytes) -> bytes:
    player_entry = [
        struct.pack('<I', player_id),
        player_bin[4:]
    ]
    return b''.join(player_entry)


def player_entry_17(player_id: int, player_bin: bytes) -> bytes:
    player_entry = [
        bytearray(8),
        struct.pack('<I', player_id),
        player_bin[12:]
    ]
    return b''.join(player_entry)


def player_entry_19(player_id: int, player_bin: bytes) -> bytes:
    player_entry = [
        bytearray(4),
        struct.pack('<I', player_id),
        player_bin[8:]
    ]
    return b''.join(player_entry)


def player_gen(pes_ver: int, team_amount: int, output_loc: str):
    team_id = 701
    players = []

    """
    if pes_ver == 15:
        player_entry = player_entry_15
        player_bin = open(r'bin\\Player_Base_15.bin', 'rb').read()
    """
    if pes_ver == 16:
        player_entry = player_entry_19
        player_bin = open(r'bin\Player_Base_16.bin', 'rb').read()
    elif pes_ver == 17:
        player_entry = player_entry_17
        player_bin = open(r'bin\Player_Base_17.bin', 'rb').read()
    elif pes_ver == 18:
        player_entry = player_entry_17
        player_bin = open(r'bin\Player_Base_18.bin', 'rb').read()
    elif pes_ver == 19:
        player_entry = player_entry_19
        player_bin = open(r'bin\Player_Base_19.bin', 'rb').read()
    elif pes_ver in [20, 21]:
        player_entry = player_entry_17
        player_bin = open(r'bin\Player_Base_20.bin', 'rb').read()
    else:
        raise ValueError("Unsupported PES Version.")

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int('{}{}'.format(team_id, f'0{player_index}' if player_index < 10 else player_index))
            players.append(player_entry(player_id, player_bin))
            player_index += 1
        team_id += 1

    open(output_loc, 'wb').write(b''.join(players))


if __name__ == '__main__':
    pes_version = input('Enter the PES version of what the "Player.bin" needs to be generated for: ')
    amount = len(open('../team_list.txt', 'r').read().split('\n'))
    """
    if '15' in pes_version:
        player_gen(15, amount, 'Player.bin')
    """
    if '16' in pes_version:
        player_gen(16, amount, 'Player.bin')
    elif '17' in pes_version:
        player_gen(17, amount, 'Player.bin')
    elif '18' in pes_version:
        player_gen(18, amount, 'Player.bin')
    elif '19' in pes_version:
        player_gen(19, amount, 'Player.bin')
    elif ('20' in pes_version) or ('21' in pes_version):
        player_gen(20, amount, 'Player.bin')
    else:
        raise ValueError("Unsupported PES Version.")
