f = open('input2.txt', 'r')
data = f.read().split('\n')
print(repr(data))


def validate_password(entry):
    (occurrences, letter, password) = entry.split()
    letter = letter[0]
    (min1, max1) = map(int, occurrences.split('-'))
    rep = password.count(letter)
    if min1 <= rep <= max1:
        return True
    return False


def validate_password_part2(entry):
    (occurrences, letter, password) = entry.split()
    letter = letter[0]
    (pos1, pos2) = map(int, occurrences.split('-'))
    if (password[pos1-1] == letter) ^ (password[pos2-1] == letter):
        return True
    return False


valid_entries = 0
for entry in data:
    if validate_password(entry):
        valid_entries += 1

valid_entries = 0
for entry in data:
    if validate_password_part2(entry):
        valid_entries += 1

print(valid_entries)
