import struct


def coach_gen(pes_ver: int, team_amount: int, output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    coach_id = 701
    coaches = []
    pad = 2 if pes_ver in [19, 20, 21] else 10

    for _ in range(team_amount):
        coach_entry = [
            struct.pack("<I", int(coach_id)),  # Manager ID
            struct.pack("<H", 231),  # Manger Nationality
            bytearray(pad),
            "マネージャー".encode("utf-8"),  # Manager Japanese Name
            bytearray(28),
            "MANAGER".encode("utf-8"),  # Manager English Name
            bytearray(39),
        ]
        coaches.append(b"".join(coach_entry))
        coach_id += 1

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(coaches))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "Coach.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        amount = len(f.read().split("\n"))

    for ver in range(15, 22):
        if str(ver) in pes_version:
            coach_gen(ver, amount, "Coach.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
