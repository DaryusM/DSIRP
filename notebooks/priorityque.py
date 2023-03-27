class PQ:
    """
      >>> pq = new()
      >>> pq.size()
      0
    """
    def __init__(self):
        self.data = []

    def __eq__(self, other):
        return self.data == other.data

    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size() == 0
            

def printPQ(pq):
    return(pq.data)


def new():
    """
      >>> pq = new()
      >>> isinstance(pq, PQ)
      True
    """
    return PQ()


def insert(val, pq):
    """
      >>> pq = new()
      >>> pq.size()
      0
      >>> insert(7, pq)
      >>> pq.size()
      1
      >>> insert(4, pq)
      >>> printPQ(pq)
      [4, 7]
      >>> insert(5, pq)
      >>> printPQ(pq)
      [4, 5, 7]
      >>> insert(2, pq)
      >>> printPQ(pq)
      [2, 4, 5, 7]

    """

    pos = -1
    pq.data.append(val)
    
    if pq.size() != 1:

        while pq.data[0] != pq.data[pos]:
            if pq.data[pos] < pq.data[pos - 1]:
                pq.data[pos], pq.data[pos - 1] = pq.data[pos - 1], pq.data[pos]
                pos -= 1
            else:
                break



def min(pq):
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> insert(4, pq)
      >>> insert(5, pq)
      >>> insert(2, pq)
      >>> min(pq)
      2


    """
    return pq.data[0]


def dm(pq):
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> insert(4, pq)
      >>> insert(5, pq)
      >>> insert(2, pq)
      >>> dm(pq)
      >>> printPQ(pq)
      [4, 5, 7]

    """

    pq.data.pop(0)


def priority(pq, val):
    """
      >>> pq = new()
      >>> insert(7, pq)
      >>> insert(4, pq)
      >>> insert(5, pq)
      >>> insert(2, pq)
      >>> priority(pq, 5)
      3
      >>> priority(pq, 2)
      4
      >>> priority(pq,7)
      1
      >>> priority(pq, 123)
      The value given is not in the priority queue
    """

    items = len(pq.data)
    val_dex = 0

    try:
        val_dex = pq.data.index(val)

        if val_dex == 0:
            return items
        elif val == pq.data[-1]:
            return 1
        else:
            return (items + 1) - val_dex
    except:
        print("The value given is not in the priority queue")
        

    


if __name__ == "__main__":
    import doctest
    doctest.testmod()

