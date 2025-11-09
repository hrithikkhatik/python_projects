s1 = "Hello World"
print(f"Length of string:{len(s1)}")
print(f"First character:{s1[0]}")
print(f"Last character:{s1[-1]}")
print(f"S1[2:7:1] = ...{s1[2:7:1]}")
print(f"S1[2:9:2] = ...{s1[2:9:2]}")
print(f"s1[1:12:3] = ...{s1[1:12:3]}")
S1_slice = s1[1:12:3]
print(type(S1_slice))