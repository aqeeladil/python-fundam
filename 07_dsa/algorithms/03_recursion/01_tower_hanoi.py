'''
The Tower of Hanoi is a classic puzzle where you have three rods and a number of 
# disks of different sizes. Initially, all disks are stacked in ascending order of 
# size on one rod. The objective is to move the entire stack to another rod, following 
# these rules:

- Only one disk can be moved at a time.
- A disk can only be placed on top of a larger disk or on an empty rod.
'''

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)

# Example usage
tower_of_hanoi(3, 'A', 'B', 'C')


