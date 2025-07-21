import re

TOKENS = [
    ('KEYWORD', r'\b(if|else|for|int|return|while|void|float|char|double|break|continue)\b'),
    ('BOOLEAN', r'\b(true|false)\b'),
    ('CHAR', r"'(\\.|[^'])'"),
    ('NUMBER', r'\b\d+(\.\d+)?\b'),
    ('STRING', r'""".*?"""|".*?"'),
    ('COMMENT', r'//.*?$'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('OPERATOR', r'[+\-*/=<>!&|]+'),
    ('PUNCTUATION', r'[(){};,\[\]]'),
]

COLORS = {
    'KEYWORD': 'blue',
    'BOOLEAN': 'darkorange',
    'CHAR': 'darkred',
    'NUMBER': 'red',
    'STRING': 'green',
    'COMMENT': 'gray',
    'IDENTIFIER': 'black',
    'OPERATOR': 'purple',
    'PUNCTUATION': 'teal',
}

def highlight(code):
    highlighted = ''
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
            match = regex.match(code, pos)
            if match:
                text = match.group(0)
                color = COLORS[token_type]
                highlighted += f'<span style="color:{color}">{text}</span>'
                pos = match.end()
                break
        if not match:
            highlighted += code[pos]
            pos += 1
    return f"<pre>{highlighted}</pre>"
