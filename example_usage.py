from client import LexerEngine

def main():
    lexer = LexerEngine()
    code = "result = 42 + (step * 2);"
    tokens = lexer.tokenize(code)
    print("Lexer Engine Verification:")
    print(f"Source Code: '{code}'")
    print(f"Tokens Count: {len(tokens)}")
    for t in tokens[:5]:
        print(f"  {t['type']}: {t['value']}")

if __name__ == "__main__":
    main()
