import ast

class Normalizer:
    def normalize(self, text: str) -> str:
        """
        Normalize the formatting of a Python program by simplifying docstrings and
        function annotations, and normalizing white space and line breaks.
        """
        # Parse the text into an AST
        tree = ast.parse(text)

        # Simplify docstrings and function annotations
        self.simplify_docstrings_and_annotations(tree)

        # Normalize formatting and convert back to text
        text = ast.unparse(tree).strip()

        # Normalize white space and line breaks
        text = self.normalize_whitespace_and_linebreaks(text)

        return text

    def simplify_docstrings_and_annotations(self, tree):
        """Simplify docstrings and function annotations in the given AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                node.value.s = 'DOCSTRING'
            if isinstance(node, ast.FunctionDef):
                node.returns = None
                node.args.args = []
                node.args.vararg = None
                node.args.kwarg = None
                node.args.kwonlyargs = []
                node.args.defaults = []
                node.args.kw_defaults = []

    def normalize_whitespace_and_linebreaks(self, text: str) -> str:
        """Normalize white space and line breaks in the given text."""
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        return '\n'.join(lines)