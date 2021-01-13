colors = {"black":0,
          "brown":1,
          "red":2,
          "orange":3,
          "yellow":4,
          "green":5,
          "blue":6,
          "violet":7,
          "grey":8,
          "white":9}

answer = 0
answer += 10*colors[input()]
answer += colors[input()]
answer *= 10**colors[input()]

print(answer)
