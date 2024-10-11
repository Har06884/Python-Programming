print("Tuples")

colors = ("Red", "Blue", "Green")

print(colors)
print(colors[2])
print(colors[1:2])

y = list(colors)
y.append("Yellow")
colors = tuple(y)
print(colors)

y = ("Wraithbone",)
colors += y
print(colors)
