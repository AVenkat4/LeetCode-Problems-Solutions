class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        self.freq[x] = self.freq[x] + 1
        f = self.freq[x]
        if f > self.max_freq:
            self.max_freq = f
        self.group[f].append(x)
        

    def pop(self):
        x = self.group[self.max_freq].pop()
        self.freq[x] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()