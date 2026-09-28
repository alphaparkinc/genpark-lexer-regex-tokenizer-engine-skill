"""Deterministic Regex Lexer & Tokenizer Engine
100% Python Standard Library (re).
"""

import re

class LexerEngine:
    """Configurable regular expression lexical scanner."""
    def __init__(self, token_specs=None):
        if token_specs is None:
            self.rules = [
                ("NUMBER", r"\d+(\.\d*)?"),
                ("IDENT", r"[A-Za-z_]\w*"),
                ("ASSIGN", r"="),
                ("PLUS", r"\+"),
                ("MINUS", r"-"),
                ("MUL", r"\*"),
                ("DIV", r"/"),
                ("LPAREN", r"\("),
                ("RPAREN", r"\)"),
                ("SEMICOLON", r";"),
                ("SKIP", r"[ \t]+"),
                ("NEWLINE", r"\n")
            ]
        else:
            self.rules = token_specs

    def tokenize(self, code):
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in self.rules)
        tokens = []
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind not in ["SKIP", "NEWLINE"]:
                tokens.append({"type": kind, "value": value})
        return tokens
