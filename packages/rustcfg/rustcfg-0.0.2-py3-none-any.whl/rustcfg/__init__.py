# SPDX-License-Identifier: MIT

import pyparsing as pp
from functools import lru_cache

def paren_exp(keyword, contents):
    return pp.Keyword(keyword)('op') + pp.Suppress('(') + contents + pp.Suppress(')')

def cfg_exp():
    option = pp.Word(pp.alphanums + '_')('option')
    exp = pp.Forward()

    assign = (option + pp.Suppress("=") + pp.QuotedString('"')('value'))('assign')

    any_exp = paren_exp('any', pp.delimitedList(exp, delim=','))
    all_exp = paren_exp('all', pp.delimitedList(exp, delim=','))
    not_exp = paren_exp('not', exp)

    exp << pp.Group(any_exp | all_exp | not_exp | assign | option)

    return paren_exp('cfg', exp)

def multiarch_tuple():
    word = pp.Word(pp.alphanums + '_')
    opt = pp.Optional(pp.Suppress('-') + word)
    tup = (word('a') + pp.Suppress('-') + word('b') + opt('c') + opt('d'))('archtuple')
    return tup

@lru_cache()
def cfg_grammar():
    grammar = (cfg_exp() | multiarch_tuple()) + pp.stringEnd()
    return grammar

def dump_tree(t, level=0, evalf=None):
    print('{}structure {}{}{}{}'.format('    '*level, t.getName(),
                                        ' [' if evalf else '',
                                        evalf(t) if evalf else '',
                                        ']' if evalf else ''))
    for item in t:
        if isinstance(item, str):
            print('{}{!r}'.format('    '*(level+1), item))
        else:
            dump_tree(item, level+1, evalf=evalf)

class Evaluator:
    """Evalutate cfg expressions

    From rust docs:
      Configuration options are boolean (on or off) and are named
      either with a single identifier (e.g. foo) or an identifier and
      a string (e.g. foo = "bar"; the quotes are required and spaces
      around the = are unimportant). Note that similarly-named
      options, such as foo, foo="bar" and foo="baz" may each be set or
      unset independently.
    """
    def __init__(self, options=()):
        self.options = options

    def eval_tree(self, tree):
        kind = tree.getName()
        assert kind
        if kind == 'option':
            return tree.option in self.options
        elif kind == 'assign':
            option = tree.option, tree.value
            return option in self.options
        elif kind == 'op':
            op = tree[0]
            if op == 'cfg':
                assert(len(tree) == 2)
                return self.eval_tree(tree[1])
            if op == 'any':
                assert(len(tree) >= 2)
                return any(self.eval_tree(item) for item in tree[1:])
            if op == 'all':
                assert(len(tree) >= 2)
                return all(self.eval_tree(item) for item in tree[1:])
            if op == 'not':
                assert(len(tree) == 2)
                return not self.eval_tree(tree[1])
            assert False, f'Unknown operator {op}'
        elif kind == 'archtuple':
            return 'linux' in list(tree)
        else:
            assert False, f'Unknown element {kind}'

    @classmethod
    def platform(cls):
        """An Evaluator populated with some platform options

        I don't see a list that'd specify what the allowed options
        are, so this is culled from deps used in crates packaged in
        Fedora 28.
        """
        return cls(options=('unix',
                            ('target_os', 'linux')))

    def parse_and_eval(self, string):
        g = cfg_grammar()
        t = g.parseString(string)
        return self.eval_tree(t)
