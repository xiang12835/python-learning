# coding=utf-8

"""

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.


"""

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void

        root = <type 'dict'>: {'a': {'p': {'p': {'l': {'e': {'#': '#'}}}}}}
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end_of_word in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':

    word = "apple"
    obj = Trie()
    obj.insert(word)
    param_1 = obj.search(word)
    param_2 = obj.search("app")
    param_3 = obj.startsWith("app")

    print(param_1)
    print(param_2)
    print(param_3)
