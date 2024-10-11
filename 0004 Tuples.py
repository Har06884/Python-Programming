print("Tuples")

colors = ("Red", "Blue", "Green")

print(colors)
print(colors[2])
print(colors[1:2])

# to add to a Tuple, it need to be converted to a List then back
y = list(colors)
y.append("Yellow")
colors = tuple(y)
print(colors)

# another method to add to a tuple
y = ("Wraithbone",)
colors += y
print(colors)
