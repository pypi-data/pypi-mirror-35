from dotpy.components.digraph import Digraph
from dotpy.components.node import Node
from dotpy.components.edge import Edge
from dotpy.components.attribute_statement import AttributeStatement
from dotpy.components.attribute import Attribute

from dotpy.parser.lexer import MyLexer
import ply.yacc as yacc

class MyParser(object):

    def __init__(self):
        self.lexer = MyLexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.symbols = self.lexer.reserved
        self.parser = yacc.yacc(module=self)

    def __call__(self, s, **kwargs):
        return self.parser.parse(s, lexer=self.lexer.lexer)

    ## Rules are splitted where needed for performance

    def p_graph_1(self, p):
        '''graph : DIGRAPH CLPAR stmt_list CRPAR'''
        p[0] = Digraph("", p[3])

    def p_graph_2(self, p):
        '''graph : DIGRAPH ID CLPAR stmt_list CRPAR'''
        p[0] = Digraph(p[2], p[4])

    def p_stmt_list_1(self, p):
        '''stmt_list : stmt SEMICOLON stmt_list'''
        p[0] = [p[1]] + p[3]

    def p_stmt_list_2(self, p):
        '''stmt_list : stmt stmt_list'''
        p[0] = [p[1]] + p[2]

    def p_stmt_list_3(self, p):
        '''stmt_list : stmt SEMICOLON
                     | stmt'''
        p[0] = [p[1]]

    def p_stmt_1(self, p):
        '''stmt : node_stmt
                | edge_stmt
                | attr_stmt'''
        p[0] = p[1]

    def p_stmt_2(self, p):
        '''stmt : ID EQUALS ID'''
        p[0] = AttributeStatement("", [Attribute(p[1], p[3])])

    def p_node_stmt_1(self, p):
        '''node_stmt : node_id attr_list'''
        p[0] = Node(p[1], p[2])

    def p_node_stmt_2(self, p):
        '''node_stmt : node_id'''
        p[0] = Node(p[1], [])

    def p_edge_stmt_1(self, p):
        '''edge_stmt : node_id edge_rhs attr_list'''
        p[0] = Edge(p[1], p[2], p[3])

    def p_edge_stmt_2(self, p):
        '''edge_stmt : node_id edge_rhs'''
        p[0] = Edge(p[1], p[2], [])

    def p_attr_stmt(self, p):
        '''attr_stmt : NODE attr_list
                     | EDGE attr_list'''
        p[0] = AttributeStatement(p[1], p[2])

    def p_node_id(self, p):
        '''node_id : ID'''
        p[0] = p[1]

    def p_edge_rhs_1(self, p):
        '''edge_rhs : ARROW node_id'''
        p[0] = p[2]

    def p_attr_list(self, p):
        '''attr_list : SLPAR a_list SRPAR'''
        p[0] = p[2]

    def p_a_list_1(self, p):
        '''a_list : ID EQUALS ID SEMICOLON a_list
                  | ID EQUALS ID COMMA a_list'''
        p[0] = [Attribute(p[1], p[3])] + p[5]

    def p_a_list_2(self, p):
        '''a_list : ID EQUALS ID a_list'''
        p[0] = [Attribute(p[1], p[3])] + p[4]

    def p_a_list_3(self, p):
        '''a_list : ID EQUALS ID SEMICOLON
                  | ID EQUALS ID COMMA
                  | ID EQUALS ID'''
        p[0] = [Attribute(p[1], p[3])]

    def p_error(self, p):
        print("Error: syntax error when parsing '{}'".format(p))