import re
import struct


def comp_entry_15(
    team_id: int, entry_index: int, comp_index: int, comp_id: int
) -> bytes:
    competition_entry = [
        struct.pack("<I", team_id),  # Team ID
        bytearray(2),
        struct.pack("<H", entry_index),  # Entry ID
        bytearray(1),
        struct.pack("B", comp_index),  # Entry Order
        struct.pack("<H", comp_id),  # Competition ID
    ]
    return b"".join(competition_entry)


def comp_entry_19(
    team_id: int, entry_index: int, comp_index: int, comp_id: int
) -> bytes:
    competition_entry = [
        struct.pack("<I", team_id),  # Team ID
        bytearray(2),
        struct.pack("<H", entry_index),  # Entry ID
        struct.pack("<H", comp_id),  # Competition ID
        struct.pack("<H", comp_index),  # Entry Order
    ]
    return b"".join(competition_entry)


def comp_entry_gen(pes_ver: int, team_list: list[str], output_loc: str):
    index = 1
    index_4cc = 1
    index_bak = 1
    index_vgl = 1
    index_inv = 1
    comp_entries = []

    if pes_ver in [15, 16, 17, 18]:
        comp_entry = comp_entry_15
    elif pes_ver in [19, 20, 21]:
        comp_entry = comp_entry_19
    else:
        raise ValueError("Unsupported PES Version.")

    for team_data in team_list:
        team_id, _, team_name = re.match(r"(\d{3}) (\w*) +(.*)", team_data).groups()
        if not any(
            ["Backup" in team_name, "VGL" in team_name, "Invitational" in team_name]
        ):
            comp_entries.append(comp_entry(int(team_id), index, index_4cc, 9))
            index_4cc += 1
        else:
            if "Backup" in team_name:
                comp_entries.append(comp_entry(int(team_id), index, index_bak, 12))
                index_bak += 1
            elif "VGL" in team_name:
                comp_entries.append(comp_entry(int(team_id), index, index_vgl, 11))
                index_vgl += 1
            elif "Invitational" in team_name:
                comp_entries.append(comp_entry(int(team_id), index, index_inv, 10))
                index_inv += 1
        index += 1

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(comp_entries))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "CompetitionEntry.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        data = f.read().split("\n")
    if any(
        [
            "15" in pes_version,
            "16" in pes_version,
            "17" in pes_version,
            "18" in pes_version,
        ]
    ):
        comp_entry_gen(15, data, "CompetitionEntry.bin")
    elif any(["19" in pes_version, "20" in pes_version, "21" in pes_version]):
        comp_entry_gen(19, data, "CompetitionEntry.bin")
    else:
        raise ValueError("Unsupported PES Version.")
