class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.date = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.date.get(letter)
            if not child:
                new_node = TrieNode()
                node.date[letter] = new_node
                node = new_node
            else:
                node = child
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            child = node.date.get(letter)
            if not child:
                return False
            else:
                node = child
        if node.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            child = node.date.get(letter)
            if not child:
                return False
            else:
                node = child
        if node.is_word or node.date:
            return True
        else:
            return False


if __name__ == '__main__':
    trie = Trie()
    trie.insert("somestring")
    trie.insert("somebody")
    trie.insert("somebody1")
    trie.insert("somebody3")
    print(trie.search("key"))
    print(trie.search("somebody3"))
    print(trie.startsWith("some"))

