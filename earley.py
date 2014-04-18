import sys
import re

from operator import add

class TreeNode:
    def __init__(self, body, children=[]):
        '''Initialize a tree with body and children'''
        self.body = body
        self.children = children

    def __len__(self):
        '''A length of a tree is its leaves count'''
        if self.is_leaf():
            return 1
        else:
            return reduce(add, [len(child) for child in self.children])

    def __repr__(self):
        '''Returns string representation of a tree in bracket notation'''
        st = "[.{0} ".format(self.body)
        if not self.is_leaf():
            st+= ' '.join([str(child) for child in self.children])
        st+= ' ]'
        return st

    def is_leaf(self):
        '''A leaf is a childless node'''
        return len(self.children) == 0

class ParseTrees:
    def __init__(self, parser):
        '''Initialize a syntax tree parsing process'''
        self.parser = parser
        self.charts = parser.charts
        self.length = len(parser)

        self.nodes = []
        for root in parser.complete_parses:
            self.nodes.extend(self.build_nodes(root))

    def __len__(self):
        '''Trees count'''
        return len(self.nodes)

    def __repr__(self):
        '''String representation of a list of trees with indexes'''
        return '<Parse Trees>\n{0}</Parse Trees>' \
                    .format('\n'.join("Parse tree #{0}:\n{1}\n\n" \
                                        .format(i+1, str(self.nodes[i]))
                                      for i in range(len(self))))

    def build_nodes(self, root):
        '''Recursively create subtree for given parse chart row'''
        nodes = []

        # find subtrees of current symbol
        if root.completing:
            down = self.build_nodes(root.completing)
        else:
            down = [TreeNode(root.prev_category())]
        # prepend subtrees of previous symbols
        prev = root.previous
        left = []
        while prev and prev.dot > 0:
            left[:0] = [self.build_nodes(prev)]
            prev = prev.previous
        left.append(down)
        return [TreeNode(root.rule.lhs, children) for children in left]

class Word:
    def __init__(self, word = '', tags = []):
        '''Initialize a word with a list of tags'''
        self.word = word
        self.tags = tags

    def __str__(self):
        '''Nice string representation'''
        return "{0}<{1}>".format(self.word, ','.join(self.tags))

class Sentence:
    def __init__(self, words = []):
        '''A sentence is a list of words'''
        self.words = words

    def __str__(self):
        '''Nice string representation'''
        return ' '.join(str(w) for w in self.words)

    def __len__(self):
        '''Sentence's length'''
        return len(self.words)

    def __getitem__(self, index):
        '''Return a word of a given index'''
        if index >= 0 and index < len(self):
            return self.words[index]
        else:
            return None

    def add_word(self, word):
        '''Add word to sentence'''
        self.words.append(word)

    @staticmethod
    def from_string(text):
        '''Create a Sentence object from a given string in the Apertium
           stream format:
              time/time<N> flies/flies<N>/flies<V> like/like<P>/like<V>
              an/an<D> arrow/arrow<N>'''
        #TODO handle Apertium format's beginning ^ and ending $ symbols

        # prepare regular expressions to find word and tags
        lemmarex = re.compile('^[^\/]*')
        tagsrex = re.compile('\/[^\<]*\<([^\>]*)\>')

        sentence = Sentence()
        words = text.strip().split(' ')
        dbg = True
        ctr = 0
        if dbg: print 'words=',words
        for word in words:
            lemma = lemmarex.match(word).group(0)
            tags = tagsrex.findall(word)
            if dbg: print ctr,'word=',word,'tags=',tags
            w = Word(lemma, tags)
            sentence.add_word(w)
            ctr = ctr + 1

        return sentence

class Chart:
    def __init__(self, rows):
        '''An Earley chart is a list of rows for every input word'''
        self.rows = rows

    def __len__(self):
        '''Chart length'''
        return len(self.rows)

    def __repr__(self):
        '''Nice string representation'''
        st = '<Chart>\n\t'
        st+= '\n\t'.join(str(r) for r in self.rows)
        st+= '\n</Chart>'
        return st

    def add_row(self, row):
        '''Add a row to chart, only if wasn't already there'''
        if not row in self.rows:
            self.rows.append(row)

class ChartRow:
    def __init__(self, rule, dot=0, start=0, previous=None, completing=None):
        '''Initialize a chart row, consisting of a rule, a position
           index inside the rule, index of starting chart and
           pointers to parent rows'''
        self.rule = rule
        self.dot = dot
        self.start = start
        self.completing = completing
        self.previous = previous

    def __len__(self):
        '''A chart's length is its rule's length'''
        return len(self.rule)

    def __repr__(self):
        '''Nice string representation:
            <Row <LHS -> RHS .> [start]>'''
        rhs = list(self.rule.rhs)
        rhs.insert(self.dot, '.')
        rule_str = "[{0} -> {1}]".format(self.rule.lhs, ' '.join(rhs))
        return "<Row {0} [{1}]>".format(rule_str, self.start)

    def __cmp__(self, other):
        '''Two rows are equal if they share the same rule, start and dot'''
        if len(self) == len(other):
            if self.dot == other.dot:
                if self.start == other.start:
                    if self.rule == other.rule:
                        return 0
        return 1

    def is_complete(self):
        '''Returns true if rule was completely parsed, i.e. the dot is at the end'''
        return len(self) == self.dot

    def next_category(self):
        '''Return next category to parse, i.e. the one after the dot'''
        if self.dot < len(self):
            return self.rule[self.dot]
        return None

    def prev_category(self):
        '''Returns last parsed category'''
        if self.dot > 0:
            return self.rule[self.dot-1]
        return None

class Rule:
    def __init__(self, lhs, rhs):
        '''Initializes grammar rule: LHS -> [RHS]'''
        self.lhs = lhs
        self.rhs = rhs

    def __len__(self):
        '''A rule's length is its RHS's length'''
        return len(self.rhs)

    def __repr__(self):
        '''Nice string representation'''
        return "<Rule {0} -> {1}>".format(self.lhs, ' '.join(self.rhs))

    def __getitem__(self, item):
        '''Return a member of the RHS'''
        return self.rhs[item]

    def __cmp__(self, other):
        '''Rules are equal iff both their sides are equal'''
        if self.lhs == other.lhs:
            if self.rhs == other.rhs:
                return 0
        return 1

class Grammar:
    def __init__(self):
        '''A grammar is a collection of rules, sorted by LHS'''
        self.rules = {}

    def __repr__(self):
        '''Nice string representation'''
        st = '<Grammar>\n'
        for group in self.rules.values():
            for rule in group:
                st+= '\t{0}\n'.format(str(rule))
        st+= '</Grammar>'
        return st

    def __getitem__(self, lhs):
        '''Return rules for a given LHS'''
        if lhs in self.rules:
            return self.rules[lhs]
        else:
            return None

    def add_rule(self, rule):
        '''Add a rule to the grammar'''
        lhs = rule.lhs
        if lhs in self.rules:
            self.rules[lhs].append(rule)
        else:
            self.rules[lhs] = [rule]

    @staticmethod
    def from_file(filename):
        '''Returns a Grammar instance created from a text file.
           The file lines should have the format:
               lhs -> outcome | outcome | outcome'''

        grammar = Grammar()
        for line in open(filename):
            # ignore comments
            line = line[0:line.find('#')]
            if len(line) < 3:
                continue

            rule = line.split('->')
            lhs = rule[0].strip()
            for outcome in rule[1].split('|'):
                rhs = outcome.strip()
                symbols = rhs.split(' ') if rhs else []
                r = Rule(lhs, symbols)
                grammar.add_rule(r)

        return grammar

class Parser:
    GAMMA_SYMBOL = 'GAMMA'

    def __init__(self, grammar, sentence, debug=False):
        '''Initialize parser with grammar and sentence'''
        self.grammar = grammar
        self.sentence = sentence
        self.debug = debug

        # prepare a chart for every input word
        self.charts = [Chart([]) for i in range(len(self)+1)]
        self.complete_parses = []

    def __len__(self):
        '''Length of input sentence'''
        return len(self.sentence)

    def init_first_chart(self):
        '''Add initial Gamma rule to first chart'''
        row = ChartRow(Rule(Parser.GAMMA_SYMBOL, ['S']), 0, 0)
        self.charts[0].add_row(row)

    def prescan(self, chart, position):
        '''Scan current word in sentence, and add appropriate
           grammar categories to current chart'''
        word = self.sentence[position-1]
        if word:
            rules = [Rule(tag, [word.word]) for tag in word.tags]
            for rule in rules:
                chart.add_row(ChartRow(rule, 1, position-1))

    def predict(self, chart, position):
        '''Predict next parse by looking up grammar rules
           for pending categories in current chart'''
        for row in chart.rows:
            next_cat = row.next_category()
            rules = self.grammar[next_cat]
            if rules:
                for rule in rules:
                    new = ChartRow(rule, 0, position)
                    chart.add_row(new)

    def complete(self, chart, position):
        '''Complete a rule that was done parsing, and
           promote previously pending rules'''
        for row in chart.rows:
            if row.is_complete():
                completed = row.rule.lhs
                for r in self.charts[row.start].rows:
                    if completed == r.next_category():
                        new = ChartRow(r.rule, r.dot+1, r.start, r, row)
                        chart.add_row(new)

    def parse(self):
        '''Main Earley's Parser loop'''
        self.init_first_chart()

        i = 0
        # we go word by word
        while i < len(self.charts):
            chart = self.charts[i]
            self.prescan(chart, i) # scan current input

            # predict & complete loop
            # rinse & repeat until chart stops changing
            length = len(chart)
            old_length = -1
            while old_length != length:
                self.predict(chart, i)
                self.complete(chart, i)

                old_length = length
                length = len(chart)

            i+= 1

        # finally, print charts for debuggers
        if self.debug:
            print "Parsing charts:"
            for i in range(len(self.charts)):
                print "-----------{0}-------------".format(i)
                print self.charts[i]
                print "-------------------------".format(i)

    def is_valid_sentence(self):
        '''Returns true if sentence has a complete parse tree'''
        res = False
        for row in self.charts[-1].rows:
            if row.start == 0:
                if row.rule.lhs == self.GAMMA_SYMBOL:
                    if row.is_complete():
                        self.complete_parses.append(row)
                        res = True
        return res



def run():

    grammar = Grammar.from_file("sample.cfg")
    # parse input sentence
    sentence = Sentence.from_string("time/time<N> flies/flies<N>/flies<V> like/like<P>/like<V> an/an<D> arrow/arrow<N>")
    # run parser
    earley = Parser(grammar, sentence, 1)
    earley.parse()

    # output sentence validity
    if earley.is_valid_sentence():
        print '==> Sentence is valid.'

        trees = ParseTrees(earley)
        print 'Valid parse trees:'
        print trees
    else:
        print '==> Sentence is invalid.'
    return grammar

if __name__ == '__main__':
    grammar = run()

