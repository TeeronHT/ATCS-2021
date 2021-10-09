mountains = {'Mount Everest':8848,'K2':8611,'Kangchenjunga':8586,'Lhotse':8516,'Makalu':8485,}
print("The tallest mountains:")
for mountain in mountains:
    if mountain == "Mount Everest":
        print(str(mountain) + " is the tallest mountain in the world")
    else:
        print(mountain)
print()
print("The highest points in the world: ")
for elevation in mountains.values():
        print(str(mountains[mountain]))
print()
print("The tallest mountains and their height (in meters):")
for mountain, elevation in mountains.items():
    print(str(mountain) + " is " + str(elevation) + " meters tall")
