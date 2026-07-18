def pipeline(value, *steps):
    for step in steps:
        value = step(value)
    return value

result = pipeline(
    "  Hello World  ",
    str.strip,        # it remove whitespace
    str.lower,        # it lowercase
    str.split         # it split to list
)
print(result)  # ===>>>>> ['hello', 'world']