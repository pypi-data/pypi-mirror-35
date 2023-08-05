import ply.lex as lex
from ply.lex import TOKEN

class MyLexer(object):

    reserved = {
        'digraph':  'DIGRAPH',
        'node':     'NODE',
        'edge':     'EDGE'
    }
    # List of token names.   This is always required
    tokens = (
        'ID',
        'COMMA',
        'ARROW',
        'SLPAR',
        'SRPAR',
        'SEMICOLON',
        'EQUALS',
        'CLPAR',
        'CRPAR'
    ) + tuple(reserved.values())

    # Regular expression rules for simple tokens
    t_COMMA = r','
    t_ARROW = r'\->'
    t_SLPAR = r'\['
    t_SRPAR = r'\]'
    t_CLPAR = r'\{'
    t_CRPAR = r'\}'
    t_SEMICOLON = r';'
    t_EQUALS = r'='

    t_ignore = r'//'+ ' ' + '\n'

    digit = r'[0-9]'
    alphabet = r'[a-zA-Z_]'

    name = '(' + alphabet + ')((' + alphabet + ')|(' + digit + '))*'
    @TOKEN(name)
    def t_ID_Name(self, t):
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        else:
            t.type = 'ID'
        return t

    name = r'-?((\.[0-9]+)|([0-9]+(\.[0-9]+)))'
    @TOKEN(name)
    def t_ID_Float(self, t):
        t.type = 'ID'
        t.value = float(t.value)
        return t

    name = r'[-+]?\d+'
    @TOKEN(name)
    def t_ID_Int(self, t):
        t.type = 'ID'
        t.value = int(t.value)
        return t

    name = r'".*?"'
    @TOKEN(name)
    def t_ID_String(self, t):
        t.type = 'ID'
       # t.value = t.value[1:-1]
        return t

    def t_error(self, t):
        print("Illegal character '%s' in the input formula" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
#     def test(self,data):
#         self.lexer.input(data)
#         while True:
#             tok = self.lexer.token()
#             if not tok:
#                 break
#             print(tok)
#
# # Build the lexer and try it out
# m = MyLexer()
# m.build()           # Build the lexer
# m.test('''digraph MONA_DFA {
#  rankdir = LR;
#  center = true;
#  size = "7.5,10.5";
#  edge [fontname = Courier];
#  node [height = .5, width = .5];
#  node [shape = doublecircle]; 4;
#  node [shape = circle]; 0; 1; 2; 3;
#  node [shape = box];
#  init [shape = plaintext, label = ""];
#  init -> 0;
#  0 -> 1 [label="X"];
#  1 -> 2 [label="X"];
#  2 -> 3 [label="0"];
#  2 -> 4 [label="1"];
#  3 -> 3 [label="X"];
#  4 -> 4 [label="X"];
# }''')     # Test it