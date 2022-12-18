import os

def get_neighbor(current_coord):
  """Get the coordinates of the 6 neighboring blocks"""
  x, y, z = current_coord
  return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

def compute(input_filename):
  N = 0
  touching_faces = 0
  existed = set()
  with open(os.path.join(os.path.dirname(__file__), input_filename), "r") as f:
    for line in f:
      N += 1
      coords = tuple(int(x) for x in line.split(","))
      existed.add(coords)
      # Check 6 directions surrounding this block
      neighbors = get_neighbor(coords)
      for neighbor in neighbors:
        if neighbor in existed:
          touching_faces += 1

  # Surface area = 6 faces for each block minus 2 faces lost for each touching faces
  return 6*N - touching_faces * 2
    

def test():
  result = compute("input-test-day18.txt")
  assert result == 64

def main():
  test()
  result = compute("input-day18.txt")
  print(f"{result=}")

if __name__ == "__main__":
  main()