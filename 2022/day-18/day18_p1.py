import os

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
  
  ans = 0
  for coord in existed:
    # Check 6 directions surrounding this block
    neighbors = get_neighbor(coord)
    # Each cube start with 6 faces that count. For every face that touches a neighbor, a face gets reduced
    faces_that_count = 6
    for neighbor in neighbors:
      if neighbor in existed:
        faces_that_count -= 1
    ans += faces_that_count

  return ans
    

def test():
  result = compute("input-test-day18.txt")
  print(result)
  assert result == 64

def main():
  test()
  result = compute("input-day18.txt")
  print(f"{result=}")

if __name__ == "__main__":
  main()