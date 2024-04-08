from antlr4.Token import Token
from antlr4.ParserRuleContext import ParserRuleContext


class Errors:
    errors_data = []

    @staticmethod
    def report_error(token: Token, message):
        Errors.errors_data.append(f"{token.line}:{token.column} - {message}")

    @staticmethod
    def report_error_rule_context(rule_context: ParserRuleContext, message):
        Errors.errors_data.append(f"{rule_context.start.line}:{rule_context.start.column} - {message}")

    @staticmethod
    def number_of_errors():
        return len(Errors.errors_data)

    @staticmethod
    def print_and_clear_errors():
        for error in Errors.errors_data:
            print(error)
        Errors.errors_data.clear()
