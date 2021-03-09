f = open('7.txt')
lines = f.read().split('\n')
f.close()

def parse_line(line):
    words = line.split()
    key = ' '.join(words[:2])
    contents = ' '.join(words[4:]).split(', ')
    if contents == ['no other bags.']:
        return ( key, {} )

    quantities = {}
    for bag in contents:
        words = bag.split()
        amount = int(words[0])
        bag_type = ' '.join(words[1:3])
        quantities[bag_type] = amount

    return ( key, quantities )


bags = list(map(parse_line, lines))

all_containers = []
current_containers = ['shiny gold']
yielded_new_containers = True
while yielded_new_containers:
    new_bags = []
    for bag, contents in bags:
        for container in current_containers:
            if container in contents and bag not in new_bags and bag not in all_containers:
                new_bags.append(bag)

    if len(new_bags) == 0:
        yielded_new_containers = False

    all_containers += new_bags
    current_containers = new_bags


print(all_containers)
print(len(all_containers))