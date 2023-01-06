from typing import List, Tuple

class InputParser:
  def parse(self, input_file: str) -> List[Tuple[str, str]]:
    """
    Parse the input file containing pairs of file paths.
    """
    pairs = []
    with open(input_file, 'r') as f:
      for line in f:
        pair = tuple(line.strip().split())
        pairs.append(pair)
    return pairs