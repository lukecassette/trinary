# vim: set fileencoding=utf8
#  Keyword.py
#
# A keyword is a reserved word used by the language.
# 

keywords = ("entity", "is", "port", "in", "out", "trit", "end", "inout", 
                "downto", "architecture", "dataflow", "of", "is", "begin",
                 "end", "dataflow" )

class Keyword(object):
    def __init__(self, name):
        '''Initialize Keyword object.  '''

        assert name in keywords
        self.name = name
        
    def __str__(self):
        return "<Keyword:%s>" % (self.name,)
        
if __name__ == "__main__":
    a = Keyword("entity")
    b = Keyword("port")
    c = Keyword("architecture")
    d = Keyword("inout")
    
    print a, b, c, d
