# @author Marco Flores
# @description Program written to assist a friend in a programming class


def isApproxMatch(a, b, k):
    """Return True if equal-length strings a and b have at most k mismatches."""
    errorCounter = 0
    # shows strings being compared
    # print "{} {}".format(a,b)
    for i in range(len(a)):
        if (a[i] == b[i]):
            pass
        else:
            errorCounter += 1
    if (errorCounter <= k):
        return True
    else:
        return False

def findApprox(strand, pattern, k):
    """
    Return the first index at which an approximate match to the pattern begins
    in the given strand, or return -1 if no such match is found.

    An approximate match is one that has at most k mismatched characters.
    """
    for i in range(len(strand)- len(pattern)):
        condition = isApproxMatch(strand[i: i + len((pattern))], pattern, k)
        #if (isApproxMatch(strand[i: i + len((pattern))], pattern, k)):
        if (condition == True):
            return i
        else:
            pass
    return -1




#########################################################
# Do not make any changes to what follows.
#########################################################

for line in open('tests.txt'):
    pieces = line.split()
    if pieces:
        if len(pieces) != 3:
            print('Ignoring line: %s' % line)
        elif not pieces[2].isdigit():
            print('Illegal choice of k: %s' % line)
        else:
            print('Executing findApprox(%s,%s,%s)...' % tuple(pieces))
            print('  returned: %s' % (findApprox(pieces[0], pieces[1], int(pieces[2]))))
