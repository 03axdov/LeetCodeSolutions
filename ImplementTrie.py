class Trie(object):

    def __init__(self):
        self.words = set()
        self.prefixes = set()
        

    def insert(self, word):
        self.words.add(word)
        for i in range(len(word) + 1):
            self.prefixes.add(word[:i])
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word in self.words
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.prefixes
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)