import struct

team_id = 701
players = []

if __name__ == "__main__":
    with open("../team_list.txt", "r", encoding="utf-8") as team_list:
        amount = len(team_list.read().split("\n"))
    with open(r"bin\Player_Edit_Base_19.bin", "rb") as player_file:
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
            players.append(b"".join(player_entry))
            player_index += 1
        team_id += 1

    with open("Player_Edit.bin", "wb") as f:
        f.write(b"".join(players))
