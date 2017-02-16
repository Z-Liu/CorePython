from __future__ import division
def trans(F):
    return (F-32)*(5/9)
if __name__ == '__main__':
    print [trans(i) for i in [10, 32, 24, 3, 100]]