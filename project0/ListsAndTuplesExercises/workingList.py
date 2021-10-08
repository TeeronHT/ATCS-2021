careers = ["mafia boss", "hitman", "union boss", "police"]

print("index of hitman: " + str(careers.index("hitman")))
print("hitman" in careers)
careers.append("milk man")
careers.insert(0, "governor")
for jobs in careers:
    print(jobs)