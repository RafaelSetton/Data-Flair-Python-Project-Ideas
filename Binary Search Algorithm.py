

def search(sorted_iter, item):
    low, high = 0, len(sorted_iter)-1
    while True:
        new = int((high+low)/2)
        if sorted_iter[new] > item:
            high = new
        elif sorted_iter[new] < item:
            low = new
        else:
            return new
