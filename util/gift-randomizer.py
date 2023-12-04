
import random

participants = [
    { "name": "Bob", "group": 1},
    { "name": "Joe", "group": 1},
    { "name": "Alice", "group": 2}
]

random.shuffle(participants)
unused_participants = participants.copy()
used_participants = []
chosen = None
while len(unused_participants) > 1:
    print ('---------------')
    next_participant = unused_participants.pop(chosen) if chosen != None else unused_participants.pop(0)
    possible = [participant for participant in participants if participant["group"] != next_participant["group"] and participant["name"] not in used_participants and next_participant['name'] != participant["name"]]
    chosen = random.randint(0, len(unused_participants)-1) if len(unused_participants) != 0 else 0;
    used_participants.append(unused_participants[chosen]['name'])
    print ( next_participant['name'], "giver til", unused_participants[chosen]['name'] )

print ('---------------')
print ( unused_participants[chosen]['name'], "giver til", participants[0]['name'] )
used_participants.append(participants[0]['name'])

print ('---------------')
assert(len(used_participants) == len(participants))
print (used_participants)

    