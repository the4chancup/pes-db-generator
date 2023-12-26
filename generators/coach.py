import struct


def coach_entry_15(coach_id: int) -> bytes:
    coach_entry = [
        struct.pack('<I', int(coach_id)),  # Manager ID
        struct.pack('<H', 231),  # Manger Nationality
        bytearray(10),
        'マネージャー'.encode('utf-8'),  # Manager Japanese Name
        bytearray(28),
        'MANAGER'.encode('utf-8'),  # Manager English Name
        bytearray(39)
    ]
    return b''.join(coach_entry)


def coach_entry_19(coach_id: int) -> bytes:
    coach_entry = [
        struct.pack('<I', int(coach_id)),  # Manager ID
        struct.pack('<H', 231),  # Manger Nationality
        bytearray(2),
        'マネージャー'.encode('utf-8'),  # Manager Japanese Name
        bytearray(28),
        'MANAGER'.encode('utf-8'),  # Manager English Name
        bytearray(39)
    ]
    return b''.join(coach_entry)


def coach_gen(pes_ver: int, team_amount: int, output_loc: str):
    coach_id = 701
    coaches = []

    if pes_ver in [15, 16, 17, 18]:
        coach_entry = coach_entry_15
    elif pes_ver in [19, 20, 21]:
        coach_entry = coach_entry_19
    else:
        raise ValueError("Unsupported PES Version.")

    for _ in range(team_amount):
        coaches.append(coach_entry(coach_id))
        coach_id += 1

    open(output_loc, 'wb').write(b''.join(coaches))


if __name__ == '__main__':
    pes_version = input('Enter the PES version of what the "Coach.bin" needs to be generated for: ')
    amount = len(open('../team_list.txt', 'r').read().split('\n'))
    if any(["15" in pes_version, "16" in pes_version, "17" in pes_version, "18" in pes_version]):
        coach_gen(15, amount, 'Coach.bin')
    elif any(["19" in pes_version, "20" in pes_version, "21" in pes_version]):
        coach_gen(19, amount, 'Coach.bin')
    else:
        raise ValueError("Unsupported PES Version.")
