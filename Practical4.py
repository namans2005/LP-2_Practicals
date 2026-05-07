"""
Implement a solution for a Constraint Satisfaction Problem 
using Branch and Bound and Backtracking for 
n-queens problem or a graph coloring problem
"""
def n_queens(n, r=0, cols=[], d1=[], d2=[]):
    if r == n:
        print(cols)
        return
    
    for c in range(n):
        if c not in cols and r-c not in d1 and r+c not in d2:
            n_queens(n, r+1, cols+[c], d1+[r-c], d2+[r+c])
    
n_queens(4)