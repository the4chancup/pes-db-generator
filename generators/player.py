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

    if pes_ver in [16, 19]:
        padding = bytearray(4)
        binary = player_bin[8:]
    elif pes_ver in [17, 18, 20, 21]:
        padding = bytearray(8)
        binary = player_bin[12:]
    else:
        padding = b""
        binary = player_bin[4:]

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_index:02d}")
            players.append(b"".join([padding, struct.pack("<I", player_id), binary]))
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

    if "15" in pes_version:
        player_gen(15, amount, "Player.bin")
    elif "16" in pes_version:
        player_gen(16, amount, "Player.bin")
    elif "17" in pes_version:
        player_gen(17, amount, "Player.bin")
    elif "18" in pes_version:
        player_gen(18, amount, "Player.bin")
    elif "19" in pes_version:
        player_gen(19, amount, "Player.bin")
    elif ("20" in pes_version) or ("21" in pes_version):
        player_gen(20, amount, "Player.bin")
    else:
        raise NotImplementedError("Unsupported PES Version.")
