# test.py
#!/bin/python

first = ("James", "Michael", "Jennifer", "Sarah")
last = ("Whitaker", "Jones", "Gayles", "Davidson")
names = []
[[names.append(f"{firstname} {lastname}") for firstname in first] for lastname in last]
[print(name) for name in names]
