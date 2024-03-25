import struct


def coach_gen(pes_ver: int, team_amount: int, output_loc: str):
    coach_id = 701
    coaches = []

    if pes_ver in range(15, 19):
        pad = 10
    elif pes_ver in [19, 20, 21]:
        pad = 2
    else:
        raise NotImplementedError("Unsupported PES Version.")

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
    if any(
        [
            "15" in pes_version,
            "16" in pes_version,
            "17" in pes_version,
            "18" in pes_version,
        ]
    ):
        coach_gen(15, amount, "Coach.bin")
    elif any(["19" in pes_version, "20" in pes_version, "21" in pes_version]):
        coach_gen(19, amount, "Coach.bin")
    else:
        raise NotImplementedError("Unsupported PES Version.")
