class Difference:
    def __init__(self, a):
        self.__elements = a

	def computeDifference(self):
        self.maximumDifference = max([max([number - other for other in self.__elements]) for number in self.__elements])

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)