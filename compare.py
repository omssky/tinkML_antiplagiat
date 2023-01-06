import argparse
import src

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input file containing pairs of file paths')
    parser.add_argument('output_file', help='output file where the results will be written')
    args = parser.parse_args()

    # Create the anti-plagiarism utility
    normalizer = src.Normalizer()
    distance_calculator = src.Levenshtein()
    file_comparer = src.FileComparer(normalizer, distance_calculator)
    input_parser = src.InputParser()
    utility = src.Runner(file_comparer, input_parser)

    # Compare the pairs of files and write the results to the output file
    utility.compare(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
