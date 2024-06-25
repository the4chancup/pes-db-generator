import re
import struct


def comp_entry_gen(pes_ver: int, team_list: list[str], output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    index = 1
    index_4cc = 1
    index_bak = 1
    index_vgl = 1
    index_inv = 1
    comp_entries = []
    regex = re.compile(r"(\d{3}) (\w*) +(.*)")

    def comp_entry(tid: int, entry_idx: int, comp_idx: int, comp_id: int) -> bytes:
        entry = [
            struct.pack("<I", tid),  # Team ID
            bytearray(2),
            struct.pack("<H", entry_idx),  # Entry ID
        ]

        match pes_ver:
            case 15 | 16 | 17 | 18:
                entry.extend(
                    [
                        bytearray(1),
                        struct.pack("B", comp_idx),  # Entry Order
                        struct.pack("<H", comp_id),  # Competition ID
                    ]
                )
            case 19 | 20 | 21:
                entry.extend(
                    [
                        struct.pack("<H", comp_id),  # Competition ID
                        struct.pack("<H", comp_idx),  # Entry Order
                    ]
                )

        return b"".join(entry)

    for team_data in team_list:
        team_id, _, team_name = regex.match(team_data).groups()
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

    for ver in range(15, 22):
        if str(ver) in pes_version:
            comp_entry_gen(ver, data, "CompetitionEntry.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
