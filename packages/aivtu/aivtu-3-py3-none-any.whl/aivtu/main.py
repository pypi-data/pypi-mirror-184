import os

def getPath(filename):
    fname = filename
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    Wanted_file = os.path.join(this_dir, fname)
    with open(Wanted_file,"r") as f:
        print(f.read())
def p1():
    getPath('astar.py')

def p2():
    getPath('aostar.py')
        
def p3():
    getPath('ce.py')
        
def p4():
    getPath('id3.py')
        
def p5():
    getPath('knn.py')
        
def p6():
    getPath('ann.py')
        
def p7():
    getPath('nb.py')
        
def p8():
    getPath('em.py')
        
def p9():
    getPath('reg.py')
        
