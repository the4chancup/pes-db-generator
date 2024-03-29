import struct


def player_assign_gen(pes_ver: int, team_amount: int, output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    assign_index = 1
    team_id = 701
    assignments = []

    for _ in range(team_amount):
        player_index = 1
        for _ in range(23):
            player_id = int(f"{team_id}{player_index:02d}")
            assign_entry = [
                struct.pack("<I", assign_index),  # Assign Index
                struct.pack("<I", player_id),  # Player ID
                struct.pack("<I", team_id),  # Team ID
                struct.pack(
                    "<I", player_index - 1 if pes_ver in [19, 20, 21] else player_index
                ),  # Player Team Order
            ]
            assignments.append(b"".join(assign_entry))
            player_index += 1
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
    if any(
        [
            "15" in pes_version,
            "16" in pes_version,
            "17" in pes_version,
            "18" in pes_version,
        ]
    ):
        player_assign_gen(15, amount, "PlayerAssignment.bin")
    elif any(["19" in pes_version, "20" in pes_version, "21" in pes_version]):
        player_assign_gen(19, amount, "PlayerAssignment.bin")
    else:
        raise NotImplementedError("Unsupported PES Version.")
