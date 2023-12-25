import struct

assign_index = 1
team_id = 701
player_assignments = []

for _ in range(220):
    player_index = 1
    for _ in range(23):
        player_id = int('{}{}'.format(team_id, f'0{player_index}' if player_index < 10 else player_index))
        assign_entry = [
            struct.pack('<I', assign_index),  # Assign Index
            struct.pack('<I', player_id),  # Player ID
            struct.pack('<I', team_id),  # Team ID
            struct.pack('<I', player_index-1)  # Player Team Order
        ]
        player_assignments.append(b''.join(assign_entry))
        player_index += 1
        assign_index += 1
    team_id += 1

open('PlayerAssignment.bin', 'wb').write(b''.join(player_assignments))
