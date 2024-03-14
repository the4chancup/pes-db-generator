import os
import sys

from generators.coach import coach_gen
from generators.competition_entry import comp_entry_gen
from generators.player import player_gen
from generators.player_assignment import player_assignment_gen
from generators.player_appearance import player_appearance_gen
from generators.team import team_gen


def gen_multiple_blank_files(output_loc: str, skip_zero: bool = False):
    for i in range(7):
        if skip_zero and i == 0:
            pass
        else:
            open(output_loc.format('' if i == 0 else i), 'wb').write(b'')
    return


def generate_database(pes_ver: int, team_list: list[str]):
    db_loc = f'database_{pes_ver}/common/etc/pesdb/'
    appear_location = f'database_{pes_ver}/common/character0/model/character/appearance/'

    os.makedirs(db_loc, exist_ok=True)
    os.makedirs(appear_location, exist_ok=True)

    coach_gen(pes_ver, len(team_list), db_loc + 'Coach.bin')
    team_gen(pes_ver, team_list, db_loc + 'Team.bin')
    comp_entry_gen(pes_ver, team_list, db_loc + 'CompetitionEntry.bin')
    player_gen(pes_ver, len(team_list), db_loc + 'Player.bin')
    player_assignment_gen(pes_ver, len(team_list), db_loc + 'PlayerAssignment.bin')
    player_appearance_gen(pes_ver, len(team_list), appear_location + 'PlayerAppearance.bin')

    singular_blank_files = []
    if pes_ver in range(15, 18):
        singular_blank_files.extend([
            'InstallVersionBallDlcAs.bin', 'InstallVersionBallDlcEu.bin', 'InstallVersionBallDlcJp.bin',
            'InstallVersionBallDlcUs.bin', 'InstallVersionBallDp.bin', 'InstallVersionBootsDlcAs.bin',
            'InstallVersionBootsDlcEu.bin', 'InstallVersionBootsDlcJp.bin', 'InstallVersionBootsDlcUs.bin',
            'InstallVersionBootsDp.bin', 'InstallVersionGloveDlcAs.bin', 'InstallVersionGloveDlcEu.bin',
            'InstallVersionGloveDlcJp.bin', 'InstallVersionGloveDlcUs.bin', 'InstallVersionGloveDp.bin',
            'InstallVersionStadiumDlcAs.bin', 'InstallVersionStadiumDlcEu.bin', 'InstallVersionStadiumDlcJp.bin',
            'InstallVersionStadiumDlcUs.bin', 'InstallVersionStadiumDp.bin'
        ])
    if pes_ver in [16, 20, 21]:
        singular_blank_files.extend(['MyclubCoach.bin', 'MyclubTactics.bin', 'MyclubTacticsFormation.bin'])
    if pes_ver in [19, 20, 21]:
        singular_blank_files.extend(['PlayerWeekly.bin', 'TeamWeekly.bin'])
    if pes_ver in [20, 21]:
        singular_blank_files.extend([
            'CoachDeleteList.bin', 'Derby.bin', 'InstallVersionPlayer.bin', 'PlayerDeleteList.bin',
            'SpecialPlayerAssignment.bin', 'SpecialPlayerAssignmentKind.bin', 'Tactics.bin', 'TacticsFormation.bin'
        ])

    for blank_files in singular_blank_files:
        open(db_loc + blank_files, 'wb').write(b'')

    if pes_ver in range(15, 20):
        gen_multiple_blank_files(db_loc + 'Coach{}.bin', True)
        gen_multiple_blank_files(db_loc + 'CoachDeleteList{}.bin')
        gen_multiple_blank_files(db_loc + 'CompetitionEntry{}.bin', True)
        gen_multiple_blank_files(db_loc + 'Derby{}.bin')
        gen_multiple_blank_files(db_loc + 'InstallVersionPlayer{}.bin')
        gen_multiple_blank_files(db_loc + 'Player{}.bin', True)
        gen_multiple_blank_files(db_loc + 'PlayerAssignment{}.bin', True)
        gen_multiple_blank_files(db_loc + 'PlayerDeleteList{}.bin')
        gen_multiple_blank_files(db_loc + 'SpecialPlayerAssignment{}.bin')
        gen_multiple_blank_files(db_loc + 'SpecialPlayerAssignmentKind{}.bin')
        gen_multiple_blank_files(db_loc + 'Tactics{}.bin')
        gen_multiple_blank_files(db_loc + 'TacticsFormation{}.bin')
        gen_multiple_blank_files(db_loc + 'Team{}.bin', True)

    file_requirements = []
    if pes_ver in range(15, 20):
        file_requirements.extend([f'Country{i}.bin' if i != 0 else 'Country.bin' for i in range(7)])
    if pes_ver in range(16, 20):
        file_requirements.extend(
            [f'Competition{i}.bin' if i != 0 else 'Competition.bin' for i in range(7)] +
            [f'CompetitionKind{i}.bin' if i != 0 else 'CompetitionKind.bin' for i in range(7)] +
            [f'CompetitionRegulation{i}.bin' if i != 0 else 'CompetitionRegulation.bin' for i in range(7)]
        )
    if pes_ver in [20, 21]:
        file_requirements.extend(['Country.bin', 'Competition.bin', 'CompetitionKind.bin', 'CompetitionRegulation.bin'])

    file_requirements_path = ''
    if pes_ver == 15:
        file_requirements_path = 'Data/dt10.cpk/common/etc/pesdb/'
    elif pes_ver in [16, 17]:
        file_requirements_path = 'Data/dt10_win.cpk/common/etc/pesdb/'
    elif pes_ver in range(18, 23):
        file_requirements_path = 'Data/dt00_x64.cpk/common/etc/pesdb/'

    print(
        f'\n\33[5m\33[33m{'='*41}WARNING{'='*41}\33[0m'
        '\nThis script doesn\'t generate a complete database.'
        '\nSome files are required to be procured from the Pro Evolution Soccer 2015 game files due to legal reasons.'
        f'\nThe files required are:\n    {'\n    '.join(file_requirements)}'
        f'\nWhich are located in "{file_requirements_path}"'
    )
    input('\n\nPress any key to continue...')
    exit(0)


if __name__ == '__main__':
    if sys.version_info.major < 3 and sys.version_info.minor < 12:
        raise NotImplementedError('Python versions lower than 3.12 are not supported.')
    pes_version = input('Enter the PES version of what the database needs to be generated for: ')
    data = open('team_list.txt', 'r').read().split('\n')
    if '15' in pes_version:
        generate_database(15, data)
    elif '16' in pes_version:
        generate_database(16, data)
    elif '17' in pes_version:
        generate_database(17, data)
    elif '18' in pes_version:
        generate_database(18, data)
    elif '19' in pes_version:
        generate_database(19, data)
    elif ('20' in pes_version) or ('21' in pes_version):
        generate_database(20, data)
    else:
        raise NotImplementedError('Unsupported PES Version.')