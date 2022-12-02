def getStudentNumber():
    return "500689794"


class MyTrie:
    def __init__(self):
        # Initialize the trie node as needed
        self.children_links = [None] * 54
        self.TERMINAL = 0

    def char_to_position(self,c):
        # index 0 is the TERMINAL flag
        # index 1 is the apostrophe (')
        # index 2-27 is A-Z
        # index 28-53 is a-a
        if c == "'":
            return 1
        elif c == "#":
            return 0
        elif "A" <= c <= "Z":
            return 2 + ord(c) - ord("A")
        elif "a" <= c <= "z":
            return 28 + ord(c) - ord("a")
        return -1

    def insert(self, word, position=0):
        # Insert word into the correct place in the trie
        pointer = self
        length = len(word)
        for i in range(0, length):
            index = self.char_to_position(word[i])
            if self.children_links[index] is not None:
                self = self.children_links[index]

            else:
                self.children_links[index] = MyTrie()
                self = self.children_links[index]
            if i == length - 1:
                self.TERMINAL = 1
        self = pointer

    def remove(self, word, position=0):
        # Find and remove the node that contains the word
        pointer = self
        if position == len(word):
            self.TERMINAL = 0
            if self.isEmpty():
                return None
            return self
        index = self.char_to_position(word[position])
        if self.children_links[index] is not None:
            if position < len(word):
                self.children_links[index] = self.children_links[index].remove(word, position+1)
        return self

    def isEmpty(self):
        result = True
        for i in range(0,54):
            if self.children_links[i] is not None:
                result = False
                break
        return result

    def depth_of_word(self, word, position=0):
        # Return the depth of the node that contains the word
        pointer = self
        index = self.char_to_position(word[0])
        pointer = self.children_links[index]
        depth = 0
        for i in range(0, 54):
            if pointer.children_links[i] is not None:
                depth = depth + 1
        return depth

    def calculateDepth(self):
        if self is None:
            return 0
        depth = 0
        flag = 0
        for i in range(0,54):
            if self.children_links[i] is not None:
                temp = self.children_links[i]
                depth = max(depth, temp.calculateDepth())
                flag = 1
        return depth + flag


    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        pointer = self
        length = len(word)
        for i in range(0,length):
            index = self.char_to_position(word[i])
            if pointer.children_links[index] is not None:
                pointer = pointer.children_links[index]
                if i == length - 1 and pointer.TERMINAL == 1:
                    return True
        return False

    def autoComplete(self, prefix, position=0):
        # Return every word that extends this prefix in alphabetical order
        pointer = self
        length = len(prefix)
        for i in range(0, length):
            index = self.char_to_position(prefix[i])
            if pointer.children_links[index] is not None:
                pointer = pointer.children_links[index]
            else:
                return []
        result = pointer.getWords(prefix)
        return result

    def getWords(self, prefix):
        result = []
        if self.TERMINAL == 1:
            result.append(prefix)
        for i in range(0, 54):
            if self.children_links[i] is not None:
                if i == 1:
                    char = "'"
                elif 2 <= i < 28:
                    char = chr(ord('A') + i - 2)
                else:
                    char = chr(ord('a') + i - 28)
                result.extend(self.children_links[i].getWords(prefix+char))
        return result
