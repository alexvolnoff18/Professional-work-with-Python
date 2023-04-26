
from HW7_Interview.packages.solution import check_brackets
from HW7_Interview.packages.solution import balance_information


BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


if __name__ == '__main__':
    balance_information(check_brackets(UNBALLANCED_LIST))
    balance_information(check_brackets(BALLANCED_LIST))