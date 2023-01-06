from src import FileComparer, InputParser

class Runner:
  def __init__(self, file_comparer: FileComparer, input_parser: InputParser):
    self.file_comparer = file_comparer
    self.input_parser = input_parser

  def compare(self, input_file: str, output_file: str):
    try:
        pairs = self.input_parser.parse(input_file)
        scores = []
        for pair in pairs:
            scores.append(self.file_comparer.compare(*pair))
        with open(output_file, 'w') as f:
            for score in scores:
                f.write(str(score) + '\n')
    except (FileNotFoundError, OSError) as e:
        print(f"Error: {e}")
