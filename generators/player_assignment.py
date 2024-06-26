import struct


def player_assign_gen(pes_ver: int, team_amount: int, output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    assign_index = 1
    team_id = 701
    assignments = []

    for _ in range(team_amount):
        player_idx = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_idx:02d}")
            assign_entry = [
                struct.pack("<I", assign_index),  # Assign Index
                struct.pack("<I", player_id),  # Player ID
                struct.pack("<I", team_id),  # Team ID
                struct.pack(
                    "<I", player_idx - 1 if pes_ver in [19, 20, 21] else player_idx
                ),  # Player Team Order
            ]
            assignments += [b"".join(assign_entry)]
            player_idx += 1
            assign_index += 1
        team_id += 1

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(assignments))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "PlayerAssignment.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        amount = len(f.read().split("\n"))

    for ver in range(15, 22):
        if str(ver) in pes_version:
            player_assign_gen(ver, amount, "PlayerAssignment.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
