import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):
    
    def setUp(self):
        # Assert starter facts
        file = 'statements_kb6.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)



    def test66(self):

        for f in self.KB.facts:
            if f.supports_rules:
                print(f.statement)


        r1 = read.parse_input("fact: (dresslike profHammond TonyStark)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        ask1 = read.parse_input("fact: (isliterally ?X TonyStark)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : profHammond")
        ask2 = read.parse_input("fact: (resembles profHammond ?Y)")
        print(' Asking if', ask2)
        answer = self.KB.kb_ask(ask2)
        self.assertFalse(answer)
        
        for f in self.KB.facts:
            #print(f.statement)
            #if len(f.supported_by):
            #    print(f.supported_by[0])
            print('-------------')

    
    def test7(self):

        r1 = read.parse_input("fact: (lookslike profHammond TonyStark)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        ask1 = read.parse_input("fact: (resembles profHammond ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)
        a1 = read.parse_input("fact: (lookslike profHammond TonyStark)")
        print(' Reasserting', a1)
        self.KB.kb_assert(a1)
        ask2 = read.parse_input("fact: (resembles profHammond ?Y)")
        print(' Asking if', ask2)
        answer = self.KB.kb_ask(ask2)
        self.assertEqual(str(answer[0]), "?Y : TonyStark")
    
    def test8(self):
 
        r1 = read.parse_input("fact: (techgenius profHammond)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        r2 = read.parse_input("fact: (talkslike profHammond)")
        print(' Retracting', r2)
        #self.KB.kb_retract(r2)
        ask1 = read.parse_input("fact: (isliterally ?X TonyStark)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        #self.assertFalse(answer)
        ask2 = read.parse_input("fact: (IronMan ?X)")
        print(' Asking if', ask2)
        answer = self.KB.kb_ask(ask2)
        #self.assertFalse(answer)
        ask3 = read.parse_input("fact: (Avenger ?X)")
        print(' Asking if', ask3)
        answer = self.KB.kb_ask(ask3)
        #self.assertFalse(answer)
    
    def test9(self):
    
        r1 = read.parse_input("fact: (techgenius profHammond)")
        print(' Retracting', r1)
        self.KB.kb_retract(r1)
        ask1 = read.parse_input("fact: (employable ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)
        ask2 = read.parse_input("fact: (smart ?X)")
        print(' Asking if', ask2)
        answer = self.KB.kb_ask(ask2)
        self.assertFalse(answer)

    def test10(self):
        ask1 = read.parse_input("fact: (Avenger ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : profHammond")
        ask2 = read.parse_input("fact: (smart ?X)")
        print(' Asking if', ask2)
        answer = self.KB.kb_ask(ask2)
        self.assertEqual(str(answer[0]), "?X : profHammond")
        ask3 = read.parse_input("fact: (employable ?X)")
        print(' Asking if', ask3)
        answer = self.KB.kb_ask(ask3)
        self.assertEqual(str(answer[0]), "?X : profHammond")
    
def pprint_justification(answer):
    """Pretty prints (hence pprint) justifications for the answer.
    """
    if not answer: print('Answer is False, no justification')
    else:
        print('\nJustification:')
        for i in range(0,len(answer.list_of_bindings)):
            # print bindings
            print(answer.list_of_bindings[i][0])
            # print justifications
            for fact_rule in answer.list_of_bindings[i][1]:
                pprint_support(fact_rule,0)
        print

def pprint_support(fact_rule, indent):
    """Recursive pretty printer helper to nicely indent
    """
    if fact_rule:
        print(' '*indent, "Support for")

        if isinstance(fact_rule, Fact):
            print(fact_rule.statement)
        else:
            print(fact_rule.lhs, "->", fact_rule.rhs)

        if fact_rule.supported_by:
            for pair in fact_rule.supported_by:
                print(' '*(indent+1), "support option")
                for next in pair:
                    pprint_support(next, indent+2)



if __name__ == '__main__':
    unittest.main()
