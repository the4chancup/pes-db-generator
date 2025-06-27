import struct


def player_edit_gen(pes_ver: int):
    if pes_ver not in range(19, 22):
        raise NotImplementedError("Unsupported PES Version.")

    team_id = 701
    players = []
    file_ver = 20 if pes_ver == 21 else pes_ver

    with open("../team_list.txt", "r", encoding="utf-8") as team_list:
        amount = len(team_list.read().split("\n"))
    with open(rf"bin\Player_Edit_Base_{file_ver}.bin", "rb") as player_file:
        player_bin = player_file.read()
    with open(r"bin\PlayerAppearance_Base_16.bin", "rb") as appear_file:
        appear_bin = appear_file.read()

    for _ in range(amount):
        player_index = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_index:02d}")
            player_entry = [
                struct.pack("<I", player_id),
                struct.pack("<I", player_id),
                player_bin[8:],
                struct.pack("<I", player_id),
                bytearray(8),
                appear_bin[4:],
                bytearray(4),
            ]
            players += [b"".join(player_entry)]
            player_index += 1
        team_id += 1

    with open("Player_Edit.bin", "wb") as f:
        f.write(b"".join(players))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "Player_Edit.bin" needs to be generated for: '
    )

    for ver in range(19, 22):
        if str(ver) in pes_version:
            player_edit_gen(ver)
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
