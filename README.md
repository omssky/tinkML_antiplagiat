<!-- GETTING STARTED -->
## Getting Started

Entry task for Tinkoff ML Spring '23. 
A simple anti-plagiarism tool for python code that uses the Levenshtein distance method without using non-standard libraries.

### Usage

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Create a txt file that contains the paths of the files to be compared
   ```sh
    files/main.py plagiat1/main.py
    files/lossy.py plagiat2/lossy.py
    files/lossy.py files/lossy.py
   ```
3. Run `compare.py` with the file from the previous step as the first argument and the file you want to output the result to as the second argument
   ```sh
   python3 compare.py input.txt scores.txt
   ```