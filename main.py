from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from interpreter import Interpreter

with open("test.minilang") as f:
    code = f.read()

input_stream = InputStream(code)
lexer = MiniLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiniLangParser(token_stream)

tree = parser.program()
interpreter = Interpreter()
interpreter.visit(tree)

print("Variables:", interpreter.vars)
