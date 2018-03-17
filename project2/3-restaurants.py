# Author: John Gauthier
# Description: There is a circle of N restaurants. You can only travel from restaurant i to restaurant i+1.
# It takes some amount of energy to travel to a restaurant and you recieve some amount of energy from eating there.
# This program finds what restaurant to begin at so you can travel to all of them. Assumes that at least one path exists.
# If there are more than one, find the path that starts with the smallest restaurant number.

# Collaborated with Austin Long

import sys
from collections import deque

def travel_restaurants(queue, n):
    current = 0
    energy = 0

    while(current < n):

        restaurant = queue.popleft()

        energy += restaurant[1]

        if energy > restaurant[2]:
            current += 1
            energy -= restaurant[2]
        else:
            current = 0
            energy = 0

        queue.append(restaurant)

    answer = queue.popleft()
    print(answer[0])


def driver():
    queue = deque([]) # uses python deque function from collections 
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for i in range(n):
            in_data = f.readline().strip().split()
            food, energy_req = int(in_data[0]), int(in_data[1])
            l = [i, food, energy_req]
            queue.append(l)
    travel_restaurants(queue, n)


if __name__ == "__main__":
    driver()
