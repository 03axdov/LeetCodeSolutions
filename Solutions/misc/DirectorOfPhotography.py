def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  return helper(C, "P", X, Y) + helper(list(reversed(C)), "P", X, Y)


def helper(C, lookingFor, X, Y, carry=0):
  lookingForMap = {
    "P": "A",
    "A": "B"
  }
  
  for t, char in enumerate(C):
    if t + 1 + carry > Y and lookingFor != "P":
      return 0
    if char == lookingFor and (t + 1 + carry >= X or lookingFor == "P"):
      if lookingFor == "B": 
        return 1 + helper(C[t+1:], lookingFor, X, Y, t)
      else:        
        return helper(C[t+1:], lookingForMap[lookingFor], X, Y) + helper(C[t+1:], lookingFor, X, Y, t)
      
  return 0


N = 5
C = "APABA"
X = 2
Y = 3
print(getArtisticPhotographCount(N, C, X, Y))