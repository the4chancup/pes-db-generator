import struct


def player_appear_gen(pes_ver: int, team_amount: int, output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    appears = []
    team_id = 701
    file_ver = 16 if pes_ver in range(16, 22) else 15

    try:
        with open(rf"bin\PlayerAppearance_Base_{file_ver}", "rb") as appear_file:
            appear_bin = appear_file.read()
    except FileNotFoundError:
        with open(
            rf"generators\bin\PlayerAppearance_Base_{file_ver}.bin", "rb"
        ) as appear_file:
            appear_bin = appear_file.read()

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_index:02d}")
            appear_entry = [
                struct.pack("<I", player_id),  # Player ID
                appear_bin[4:],
            ]
            appears.append(b"".join(appear_entry))
            player_index += 1
        team_id += 1

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(appears))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "Player.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        amount = len(f.read().split("\n"))

    for ver in range(15, 22):
        if str(ver) in pes_version:
            player_appear_gen(ver, amount, "PlayerAppearance.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
