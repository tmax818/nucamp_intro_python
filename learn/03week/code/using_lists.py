states = ["Washington", "Oregon", "California"]

print("Indexes")
print(states[0])
print(states[1])
print(states[2])

print("Reverse indexes")
print(states[-1])
print(states[-2])
print(states[-3])

states[2] = "Arizona"
print(states)
print(len(states))
states.append("new York")
print(states)
states.pop()
print(states)
states.pop(1)
print(states)
