a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]
joined = [x + y for x, y in zip(a, b)]
print("\n")
print("The desired output:")
print(joined)
join_array = ' '.join(joined)
print("\n")
print("The whole statement in one line:\n")
print(join_array)
