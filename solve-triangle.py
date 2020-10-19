import sys

def setup(filename):
    '''
    Read the text file containing the input triangle.
    Return a list of lists to represent the triangle; each list represents one row.
    '''
    with open(filename, 'r') as f:
        tri = [[int(num) for num in line.split()] for line in f]
    return tri


def solve(tri):
    '''
    Calculate the maximum total we could obtain by starting at the top of the triangle and
    moving to adjacent numbers on the row below.
    Here we obtain the maximum total by calculating from bottom up.
    '''
    for i in range(len(tri)-2, -1, -1):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
    return tri[0][0]



if __name__ == '__main__':
    filename = sys.argv[1]
    tri = setup(filename)
    print(solve(tri))
