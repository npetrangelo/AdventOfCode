from collections import deque

filename = "input.txt"

def run_day(fish_buckets):
    parents = fish_buckets.pop(0)
    fish_buckets[6] += parents
    fish_buckets.append(parents)

with open(filename) as f:
    fishes = [int(fish) for fish in f.readline().strip().split(",")]
#     print(fishes)
    
    fish_buckets = [0,]*9
    for fish in fishes:
        fish_buckets[fish] += 1
    print(fish_buckets)
    
    for _ in range(256):
        run_day(fish_buckets)
    
    print(sum(fish_buckets))
