class TrieNode:
    def __init__(self):
        # for i in range(26):
        #     self.child[i] = None
        self.child = [None for _ in range(26)]
        self.isWord = False

    def printTrie(self, node, prefix):
        if node and node.isWord:
            print(prefix)
        for i in range(26):
            if node.child[i]:
                self.printTrie(node.child[i], (prefix + chr(ord('a') + i)))


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        root = self.root
        length = len(word)
        for i in range(length):
            index = self.charToIndex(word[i])

            if not root.child[index]:
                root.child[index] = self.getNode()
            root = root.child[index]
        root.isWord = True

    def search(self, word):
        root = self.root
        length = len(word)
        for i in range(length):
            index = self.charToIndex(word[i])
            if not root.child[index]:
                return False
            root = root.child[index]
        return root.isWord

    def print(self):
        self.root.printTrie(self.root, "")


if __name__ == "__main__":
    keys = ["and", "ant", "man", "mans"]
    trie = Trie()
    for key in keys:
        trie.insert(key)
    trie.print()
    print("Is Word ant in trie: ", trie.search("ant"))
    print("Is Word kop in trie: ", trie.search("kop"))

