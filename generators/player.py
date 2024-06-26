import struct


def player_gen(pes_ver: int, team_amount: int, output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    team_id = 701
    players = []
    file_ver = 20 if pes_ver == 21 else pes_ver

    try:
        with open(rf"bin\Player_Base_{file_ver}.bin", "rb") as player_file:
            player_bin = player_file.read()
    except FileNotFoundError:
        with open(rf"generators\bin\Player_Base_{file_ver}.bin", "rb") as player_file:
            player_bin = player_file.read()

    match pes_ver:
        case 16 | 19:
            padding = bytearray(4)
            binary = player_bin[8:]
        case 17 | 18 | 20 | 21:
            padding = bytearray(8)
            binary = player_bin[12:]
        case _:
            padding = b""
            binary = player_bin[4:]

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_index:02d}")
            players += [padding + struct.pack("<I", player_id) + binary]
            player_index += 1
        team_id += 1

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(players))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "Player.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        amount = len(f.read().split("\n"))

    for ver in range(15, 22):
        if str(ver) in pes_version:
            player_gen(ver, amount, "Player.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
