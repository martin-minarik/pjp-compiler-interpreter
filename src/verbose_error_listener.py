from antlr4 import DiagnosticErrorListener


class VerboseErrorListener(DiagnosticErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("Rule stack: {}".format(stack))
        print("line {}:{} at {}: {}".format(line, column, offendingSymbol, msg))
        print()
