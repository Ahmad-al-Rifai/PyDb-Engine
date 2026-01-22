import re

class Lexer:
    
    # The Lexer converts a raw SQL string into a list of tokens.
    
    def __init__(self):
        self.patterns = [
            ('KEYWORD', r'\b(SELECT|FROM|WHERE)\b'),
            ('OPERATOR', r'(=|>=|<=|>|<)'),
            ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            ('NUMBER', r'\b\d+\b'),
            ('WHITESPACE', r'\s+'),
        ]

    def tokenize(self, text):
        tokens = []
        text = text.upper() 
        cursor = 0
        while cursor < len(text):
            match = None
            for kind, pattern in self.patterns:
                regex = re.compile(pattern)
                match = regex.match(text, cursor)
                if match:
                    if kind != 'WHITESPACE':
                        tokens.append((kind, match.group(0)))
                    cursor = match.end()
                    break
            if not match:
                raise SyntaxError(f"Unexpected character: {text[cursor]}")
        return tokens

class QueryPlan:
    
    # A structured object representing the intended database operation.
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.table_name = None
        self.columns = []
        self.filter_col = None
        self.filter_val = None

    def parse(self):
        
        # Extracts execution parameters from the token stream.
        
        try:
            # Simple SELECT [col] FROM [table] WHERE [col] = [val] logic
            if self.tokens[0][1] == 'SELECT':
                self.columns = [self.tokens[1][1]]
            
            for i, (kind, val) in enumerate(self.tokens):
                if val == 'FROM':
                    self.table_name = self.tokens[i+1][1].lower()
                if val == 'WHERE':
                    self.filter_col = self.tokens[i+1][1].lower()
                    # Determine if value is a number or string
                    potential_val = self.tokens[i+3][1]
                    try:
                        self.filter_val = int(potential_val)
                    except ValueError:
                        self.filter_val = potential_val.strip("'")
        except (IndexError, ValueError):
            raise SyntaxError("Incomplete or invalid SQL syntax.")