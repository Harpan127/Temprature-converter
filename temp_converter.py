# Convert °F to °C and vice versa - the correct syntax is (int)c or (int)f

f_or_c = input("(x)F/(x)C: ")

try:
    if "c" in f_or_c or "C" in f_or_c:
        c = int(f_or_c[:-1])
        f = (c * 1.8) + 32
        print(f"{c}°C = {f}°F")

    elif "f" in f_or_c or "F" in f_or_c:
        f = int(f_or_c[:-1])
        c = (f - 32) * (5/9)
        print(f"{f}°F = {c}°C")

except ValueError:
    print(f"{f_or_c} is wrong format. Please enter 30c or 30f")
