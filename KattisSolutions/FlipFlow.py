def flipFlow(t, s, n, times):
    halves = [s,
              0] # Index 1: the upper half of the hourglass after initial flip

    current = 2 # From where the sand is leaking
    prevTime = times[0]
    for time in times[1:]:
        halves[(current + 1) % 2] += min(time - prevTime, halves[current % 2])
        halves[current % 2] -= min(time - prevTime, halves[current % 2])
        current += 1
        prevTime = time
    
    return halves[current % 2] - min((t - prevTime, halves[current % 2]))


print(flipFlow(100, 10, 5, [15, 20, 93, 96, 97,100, 150, 200, 1000, 10**6]))