class Underscore(object):
    def map(self, alist, callback):
        for i in range(0, len(alist)):
            alist[i] = callback(alist[i])
        return alist

    def reduce(self, alist, callback, memo):
        result = memo
        for i in range(0, len(alist)):
            result += callback(memo, alist[i])
        return result

    def find(self, alist, callback):
        for e in alist:
            if callback(e):
                return e

    def filter(self, alist, callback):
        arr = []
        for i in range(0, len(alist)):
            if callback(alist[i]):
                arr.append(alist[i])
        return arr

    def reject(self, alist, callback):
        arr = []
        for i in range(0, len(alist)):
            if not callback(alist[i]):
                arr.append(alist[i])
        return arr


_ = Underscore()
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# find = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
evens = _.reduce([1, 2, 3, 4, 5, 6], lambda memo, e: memo + e, 0)
print evens
# evens = _.map([1, 2, 3, 4, 5, 6], lambda x: x * 2)
