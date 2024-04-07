from antlr4 import DiagnosticErrorListener


class StopParsingListener(DiagnosticErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column} - {msg}")
