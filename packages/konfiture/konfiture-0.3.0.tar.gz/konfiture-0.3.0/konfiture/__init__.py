from .grammar_checker import GrammarChecker

def check_grammar(content, language):
    grammar_checker = GrammarChecker()
    content_splitted = content.split('\n')
    content_splitted_checked = []
    for element in content_splitted:
        element_checked = grammar_checker.correct(element)
        content_splitted_checked.append(element_checked)

    return '\n'.join(content_splitted_checked)