import sys
import json
from client import LexerEngine

lexer = LexerEngine()

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-lexer-regex-tokenizer-engine-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "tokenize_code",
                    "description": "Scan and tokenize source code string into token stream using regex lexer",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "code": {"type": "string", "description": "Source code text"}
                        },
                        "required": ["code"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "tokenize_code":
            tokens = lexer.tokenize(args.get("code", ""))
            res = {"content": [{"type": "text", "text": json.dumps({"token_count": len(tokens), "tokens": tokens})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
