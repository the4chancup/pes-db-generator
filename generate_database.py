import os
import sys

from generators.coach import coach_gen
from generators.competition_entry import comp_entry_gen
from generators.player import player_gen
from generators.player_appearance import player_appear_gen
from generators.player_assignment import player_assign_gen
from generators.team import team_gen


def gen_multiple_blank_files(output_loc: str, skip_zero: bool = False):
    for i in range(7):
        if skip_zero and i == 0:
            continue
        else:
            with open(output_loc.format("" if i == 0 else i), "wb") as blank_file:
                blank_file.write(b"")


def generate_database(pes_ver: int, team_list: list[str]):
    db_loc = rf"database_{pes_ver}/common/etc/pesdb/"
    appear_loc = rf"database_{pes_ver}/common/character0/model/character/appearance/"

    os.makedirs(db_loc, exist_ok=True)
    os.makedirs(appear_loc, exist_ok=True)

    coach_gen(pes_ver, len(team_list), db_loc + "Coach.bin")
    comp_entry_gen(pes_ver, team_list, db_loc + "CompetitionEntry.bin")
    player_gen(pes_ver, len(team_list), db_loc + "Player.bin")
    player_appear_gen(pes_ver, len(team_list), appear_loc + "PlayerAppearance.bin")
    player_assign_gen(pes_ver, len(team_list), db_loc + "PlayerAssignment.bin")
    team_gen(pes_ver, team_list, db_loc + "Team.bin")

    singular_blank_files = []
    if pes_ver in range(15, 18):
        singular_blank_files += [
            "InstallVersionBallDlcAs.bin",
            "InstallVersionBallDlcEu.bin",
            "InstallVersionBallDlcJp.bin",
            "InstallVersionBallDlcUs.bin",
            "InstallVersionBallDp.bin",
            "InstallVersionBootsDlcAs.bin",
            "InstallVersionBootsDlcEu.bin",
            "InstallVersionBootsDlcJp.bin",
            "InstallVersionBootsDlcUs.bin",
            "InstallVersionBootsDp.bin",
            "InstallVersionGloveDlcAs.bin",
            "InstallVersionGloveDlcEu.bin",
            "InstallVersionGloveDlcJp.bin",
            "InstallVersionGloveDlcUs.bin",
            "InstallVersionGloveDp.bin",
            "InstallVersionStadiumDlcAs.bin",
            "InstallVersionStadiumDlcEu.bin",
            "InstallVersionStadiumDlcJp.bin",
            "InstallVersionStadiumDlcUs.bin",
            "InstallVersionStadiumDp.bin",
        ]
    if pes_ver in [16, 20, 21]:
        singular_blank_files += [
            "MyclubCoach.bin",
            "MyclubTactics.bin",
            "MyclubTacticsFormation.bin",
        ]

    if pes_ver in [19, 20, 21]:
        singular_blank_files += ["PlayerWeekly.bin", "TeamWeekly.bin"]
    if pes_ver == 21:
        singular_blank_files += [
            "CoachDeleteList.bin",
            "Derby.bin",
            "InstallVersionPlayer.bin",
            "PlayerDeleteList.bin",
            "SpecialPlayerAssignment.bin",
            "SpecialPlayerAssignmentKind.bin",
            "Tactics.bin",
            "TacticsFormation.bin",
        ]

    for blank_files in singular_blank_files:
        with open(db_loc + blank_files, "wb") as blank_file:
            blank_file.write(b"")

    if pes_ver in range(15, 21):
        gen_multiple_blank_files(db_loc + "Coach{}.bin", True)
        gen_multiple_blank_files(db_loc + "CoachDeleteList{}.bin")
        gen_multiple_blank_files(db_loc + "CompetitionEntry{}.bin", True)
        gen_multiple_blank_files(db_loc + "Derby{}.bin")
        gen_multiple_blank_files(db_loc + "InstallVersionPlayer{}.bin")
        gen_multiple_blank_files(db_loc + "Player{}.bin", True)
        gen_multiple_blank_files(db_loc + "PlayerAssignment{}.bin", True)
        gen_multiple_blank_files(db_loc + "PlayerDeleteList{}.bin")
        gen_multiple_blank_files(db_loc + "SpecialPlayerAssignment{}.bin")
        gen_multiple_blank_files(db_loc + "SpecialPlayerAssignmentKind{}.bin")
        gen_multiple_blank_files(db_loc + "Tactics{}.bin")
        gen_multiple_blank_files(db_loc + "TacticsFormation{}.bin")
        gen_multiple_blank_files(db_loc + "Team{}.bin", True)

    file_requirements = []
    if pes_ver in range(16, 21):
        file_requirements += [
            f"Competition{i}.bin" if i != 0 else "Competition.bin" for i in range(7)
        ]
        file_requirements += [
            f"CompetitionKind{i}.bin" if i != 0 else "CompetitionKind.bin"
            for i in range(7)
        ]
        file_requirements += [
            f"CompetitionRegulation{i}.bin" if i != 0 else "CompetitionRegulation.bin"
            for i in range(7)
        ]
    if pes_ver in range(15, 21):
        file_requirements += [
            f"Country{i}.bin" if i != 0 else "Country.bin" for i in range(7)
        ]
    if pes_ver == 21:
        file_requirements += [
            "Country.bin",
            "Competition.bin",
            "CompetitionKind.bin",
            "CompetitionRegulation.bin",
        ]

    match pes_ver:
        case 15:
            file_requirements_path = "Data/dt10.cpk/common/etc/pesdb/"
        case 16 | 17:
            file_requirements_path = "Data/dt10_win.cpk/common/etc/pesdb/"
        case 18 | 19 | 20 | 21:
            file_requirements_path = "Data/dt00_x64.cpk/common/etc/pesdb/"
        case _:
            file_requirements_path = ""

    pes_ver_str = (
        f"Pro Evolution Soccer 20{pes_ver}"
        if pes_ver < 20
        else f"eFootball PES 20{pes_ver}"
    )

    print(
        f"\n\33[5m\33[33m{'=' * 41}WARNING{'=' * 41}\33[0m"
        "\nThis script doesn't generate a complete database."
        f"\nSome files are required to be procured from the {pes_ver_str} game files due to legal reasons."
        f"\nThe files required are:\n    {'\n    '.join(file_requirements)}"
        f'\nWhich are located in "{file_requirements_path}"'
    )
    input("\n\nPress any key to continue...")
    exit(0)


if __name__ == "__main__":
    if sys.version_info.major < 3 or sys.version_info.minor < 12:
        raise NotImplementedError("Python versions lower than 3.12 are not supported.")
    pes_version = input(
        "Enter the PES version of what the database needs to be generated for: "
    )
    with open("team_list.txt", "r", encoding="utf-8") as f:
        data = f.read().split("\n")

    for ver in range(15, 22):
        if str(ver) in pes_version:
            generate_database(ver, data)

    raise NotImplementedError("Unsupported PES Version.")
