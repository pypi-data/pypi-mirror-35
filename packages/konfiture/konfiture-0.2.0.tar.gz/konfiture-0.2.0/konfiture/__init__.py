from .grammar_checker_en import GrammarCheckerEn
from .grammar_checker_fr import GrammarCheckerFr

def check_grammar(content, language):
    grammar_checker = GrammarCheckerFr()
    content_splitted = content.split('\n')
    content_splitted_checked = []
    for element in content_splitted:
        element_checked = grammar_checker.correct(element)
        content_splitted_checked.append(element_checked)

    return '\n'.join(content_splitted_checked)