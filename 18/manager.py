import struct

managers = []
manager_id = 701

for _ in range(220):
    manager_entry = [
        struct.pack('<I', int(manager_id)),  # Manager ID
        struct.pack('<H', 231),  # Manger Nationality
        bytearray(10),
        'マネージャー'.encode('utf-8'),  # Manager Japanese Name
        bytearray(28),
        'MANAGER'.encode('utf-8'),  # Manager English Name
        bytearray(39)
    ]
    managers.append(b''.join(manager_entry))
    manager_id += 1

open('Coach.bin', 'wb').write(b''.join(managers))
