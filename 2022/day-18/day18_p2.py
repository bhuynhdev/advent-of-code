import os
from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

def get_neighbor(current_coord):
  """Get the coordinates of the 6 neighboring blocks"""
  x, y, z = current_coord
  return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]


def compute(input_filename):
  existed = set()
  with open(os.path.join(os.path.dirname(__file__), input_filename), "r") as f:
    for line in f:
      coord = tuple(int(x) for x in line.split(","))
      existed.add(coord)
  
  # Get the bounding box's dimensions so we can do DFS later to see which cube is "exposed"
  MAX_X, MIN_X = max(coord[0] for coord in existed), min(coord[0] for coord in existed)
  MAX_Y, MIN_Y = max(coord[1] for coord in existed), min(coord[1] for coord in existed)
  MAX_Z, MIN_Z = max(coord[2] for coord in existed), min(coord[2] for coord in existed)

  visited = set()

  @lru_cache(None)
  def is_exposed(coord):
    """Check if a cube is trapped, or is exposed to the world"""
    if coord in existed:
      return False

    if coord in visited:
      return False

    visited.add(coord)    

    # If one of the X, Y, Z coordinates reaches outside the bounding box, then current cube is exposed
    if not ((MIN_X, MIN_Y, MIN_Z) <= coord <= (MAX_X, MAX_Y, MAX_Z)):
      return True

    
    # If one of the 6 neighbors is exposed, then current cube is exposed
    for neighbor in get_neighbor(coord):
      if is_exposed(neighbor):
        return True
    
    return False

  ans = 0
  for coord in existed:
    # Check 6 directions surrounding this block
    neighbors = get_neighbor(coord)
    # Each cube start with 6 faces that count. For every face that touches a neighbor, a face gets reduced
    faces_that_count = 6
    for neighbor in neighbors:
      if not is_exposed(neighbor):
        faces_that_count -= 1
    ans += faces_that_count

  return ans
    

def test():
  result = compute("input-test-day18.txt")
  print(result)
  assert result == 58

def main():
  test()
  result = compute("input-day18.txt")
  print(f"{result=}")

if __name__ == "__main__":
  main()