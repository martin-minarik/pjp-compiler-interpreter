class Errors:
    errors_data = []

    @staticmethod
    def report_error(token, message):
        Errors.errors_data.append(f"{token.line}:{token.column} - {message}")

    @staticmethod
    def number_of_errors():
        return len(Errors.errors_data)

    @staticmethod
    def print_and_clear_errors():
        for error in Errors.errors_data:
            print(error)
        Errors.errors_data.clear()
