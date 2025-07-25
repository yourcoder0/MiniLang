from MiniLangVisitor import MiniLangVisitor
from MiniLangParser import MiniLangParser

class Interpreter(MiniLangVisitor):
    def __init__(self):
        self.vars = {}

    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[name] = value
        return value

    def visitAssignStmt(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[name] = value
        return value

    def visitExprStmt(self, ctx):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        if ctx.ID():
            name = ctx.ID().getText()
            return self.vars.get(name, 0)
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left // right
            if op == '==': return left == right
            if op == '!=': return left != right
            if op == '<': return left < right
            if op == '>': return left > right
            if op == '<=': return left <= right
            if op == '>=': return left >= right
            if ctx.STRING():
                return ctx.STRING().getText()[1:-1]
            if op == '+':
                return str(left) + str(right)
        return self.visitChildren(ctx)

def visitIfStmt(self, ctx):
    condition = self.visit(ctx.expr())
    if condition:
        for stmt in ctx.statement():
            self.visit(stmt)

def visitWhileStmt(self, ctx):
    while self.visit(ctx.expr()):
        for stmt in ctx.statement():
            self.visit(stmt)

def visitPrintStmt(self, ctx):
    value = self.visit(ctx.expr())
    print("OUTPUT:", value)

val = int(ctx.NUMBER().getText())
if not (1 <= val <= 100):
    raise Exception("Number out of bounds")

