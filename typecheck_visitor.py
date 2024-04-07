from language.LanguageVisitor import LanguageVisitor
from language.LanguageParser import LanguageParser


class TypeCheckingVisitor(LanguageVisitor):
    def __init__(self):
        self.symbol_table = {}

    def visitDeclaration(self, ctx: LanguageParser.DeclarationContext):

        return self.visitChildren(ctx)

    def visitExpression(self, ctx: LanguageParser.ExpressionContext):
        return self.visitChildren(ctx)