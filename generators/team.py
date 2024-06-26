import re
import struct


def team_gen(pes_ver: int, team_list: list[str], output_loc: str):
    if pes_ver not in range(15, 22):
        raise NotImplementedError("Unsupported PES Version.")

    teams = []
    regex = re.compile(r"(\d{3}) (\w*) +(.*)")

    for team_data in team_list:
        team_id, team_abbrev, team_name = regex.match(team_data).groups()
        team_name_field = team_name.encode("utf8") + bytearray(70 - len(team_name))
        team_entry = [
            struct.pack("<I", int(team_id)),  # Manager ID
            bytearray(4),
            struct.pack("<I", int(team_id)),  # Team ID
            bytearray(48 if pes_ver in [20, 21] else 4),
            struct.pack("<H", 29),  # Stadium ID
            struct.pack("<H", 0xFFFF),  # Team Sort Number
            struct.pack("<H", 231),  # Team Nationality
        ]

        match pes_ver:
            case 15 | 16 | 17 | 18:
                team_entry += [
                    struct.pack("<H", 0x0660)
                ]  # Anthem Style + Team Licensing
            case 19:
                team_entry += [
                    struct.pack("<H", 0x0C60)
                ]  # Anthem Style + Team Licensing
            case 20 | 21:
                team_entry += [
                    bytearray(4),
                    struct.pack("<H", 0x039C),  # Team Nationality 2
                    bytearray(12),
                    struct.pack("<I", 0x0C),  # Team & Kit Licensing
                ]

        team_entry += [
            team_name_field,  # Japanese Team Name
            team_name_field,  # Spanish Team Name
        ]

        match pes_ver:
            case 15 | 16 | 17 | 18:
                team_entry += [
                    team_name_field,  # Greek Team Name
                    team_name_field,  # English Team Name
                    team_name_field,  # Empty Team Name 1
                    team_name_field,  # Latam Team Name
                    team_name_field,  # French Team Name
                    team_name_field,  # Turkish Team Name
                ]
            case 19:
                team_entry += [
                    team_name_field,  # Empty Team Name 1
                    team_name_field,  # English Team Name
                    team_name_field,  # Empty Team Name 2
                    team_name_field,  # Latam Team Name
                    team_name_field,  # French Team Name
                    team_name_field,  # Turkish Team Name
                ]
            case 20 | 21:
                team_entry += [
                    team_name_field,  # Swedish Team Name
                    team_name_field,  # Greek Team Name
                    team_name_field,  # English Team Name
                    team_name_field,  # Latam Team Name
                    team_name_field,  # French Team Name
                    team_name_field,  # Turkish Team Name
                    team_name_field,  # Empty Team Name 1
                ]

        team_entry += [
            team_name_field,  # Portuguese Team Name
            team_abbrev.encode("utf8"),  # Database Team Name
            bytearray(24 - len(team_abbrev)),
            team_name_field,  # German Team Name
            team_abbrev.encode("utf8"),  # Licensed Abbreviated Team Name
            bytearray(10 - len(team_abbrev)),
            team_name_field,  # Brazilian Team Name
        ]

        match pes_ver:
            case 15 | 16 | 17 | 18:
                team_entry += [
                    team_name_field,  # Empty Team Name 2
                    team_name_field,  # Dutch Team Name
                    team_name_field,  # Empty Team Name 3
                    team_name_field,  # Swedish Team Name
                    team_name_field,  # Italian Team Name
                    team_name_field,  # Russian Team Name
                ]
            case 19:
                team_entry += [
                    team_name_field,  # Chinese Name
                    team_name_field,  # Dutch Team Name
                    team_name_field,  # Empty Team Name 3
                    team_name_field,  # Swedish Team Name
                    team_name_field,  # Greek Team Name
                    team_name_field,  # Italian Team Name
                    team_name_field,  # Russian Team Name
                ]
            case 20 | 21:
                team_entry += [
                    team_name_field,  # Chinese Name
                    team_name_field,  # Empty Team Name 2
                    team_name_field,  # Italian Team Name
                    team_name_field,  # Empty Team Name 3
                    team_name_field,  # Russian Team Name
                    team_name_field,  # Dutch Team Name
                ]

        team_entry += [
            "None".encode("utf8"),  # Fake Abbreviated Team Name
            bytearray(6),
            team_name_field,  # Empty Team Name 4
            team_name_field,  # English US Team Name 3
        ]

        if pes_ver in range(15, 19):
            team_entry += [bytearray(2)]

        teams += [b"".join(team_entry)]

    with open(output_loc, "wb") as output_file:
        output_file.write(b"".join(teams))


if __name__ == "__main__":
    pes_version = input(
        'Enter the PES version of what the "Team.bin" needs to be generated for: '
    )
    with open("../team_list.txt", "r", encoding="utf-8") as f:
        data = f.read().split("\n")

    for ver in range(15, 22):
        if str(ver) in pes_version:
            team_gen(ver, data, "Team.bin")
            exit(0)

    raise NotImplementedError("Unsupported PES Version.")
