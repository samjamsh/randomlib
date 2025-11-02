from ramlib import genrandom

# Get & Print a random value
start = 1
end = 10

random_value = genrandom(start, end)
print("\nRandom Value:", random_value.getnew())     # get a random value once
print()

for i in range(5):
    newrandom = random_value.generate(start, end)   # get a random value multiple times
    print("New Random:", newrandom)
print()

