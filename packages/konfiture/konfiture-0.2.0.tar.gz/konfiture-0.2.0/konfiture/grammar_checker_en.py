import language_check
from termcolor import colored

from .grammar_checker import GrammarChecker


class GrammarCheckerEn(GrammarChecker):

    def correct(self, text):
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(text)
        return self.format_correction(text, matches)

    def format_correction(self, text, matches):
        message = ''
        last = 0
        errors = []

        for match in matches:
            errors.append({
                'type': 'grammar',
                'start': match.fromx,
                'suggestions': match.replacements,
                'end': match.tox})

        # errors = []
        # for spelling_error in spelling_errors:
        #     word = text[spelling_error['nStart']:spelling_error['nEnd']]
        #     errors.append({
        #         'type': 'spelling',
        #         'start': spelling_error['nStart'],
        #         'end': spelling_error['nEnd']})
        #
        # for grammar_error in grammar_errors:
        #     start = grammar_error['nStart']
        #
        #     item = 0
        #     while item < len(errors) and errors[item]['start'] < start:
        #         item += 1
        #
        #     errors.insert(item, {
        #         'type': 'grammar',
        #         'start': start,
        #         'suggestions': grammar_error['aSuggestions'],
        #         'end': grammar_error['nEnd']})

        for error in errors:
            start = error['start']
            end = error['end']
            message += colored(text[last:start], 'cyan')
            if error['type'] == 'spelling':
                message += colored(text[start:end], 'red', attrs=[])
            elif error['type'] == 'grammar':
                message += colored(text[start:end], 'white', 'on_red')
                message += ' '
                message += colored('({})'.format(', '.join(error['suggestions'])), 'white', 'on_green')
            last = end

        if message == '':
            return colored(text, 'green')
        else:
            message += colored(text[last:], 'cyan')
            return message