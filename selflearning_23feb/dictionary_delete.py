data = {"x": 1, "y": 2, "z": 3}
del data["y"]
data.pop("z")
print(data)

#output:
# {'x': 1}