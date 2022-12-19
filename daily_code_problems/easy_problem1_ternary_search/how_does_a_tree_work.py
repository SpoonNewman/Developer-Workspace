class Node:
    def __init__(self, letter, middle = None):
        self.letter = letter
        self.middle = middle
    
    def set_middle_child(self, letter):
        self.middle = letter

    
def main():
# 1, 2, ... N
    words = ['code', 'cob', 'be', 'ax', 'war', 'we']
    # words = ['cob']



    nodes = []
    # region 
    for word in words:
        word_nodes = []
        for letter in word:
            node = Node(letter=letter)
            word_nodes.append(node)
        for index, node_letter in enumerate(word_nodes):
            # 0, C   1, O   2, B
            if index + 1 == len(word_nodes):
                pass
            else:
                node_letter.set_middle_child(word_nodes[index + 1])
        nodes = [*nodes, *word_nodes]
    #endregion
    print(list(map(lambda x: x.letter, nodes)))
    pass




if __name__ == '__main__':
    main()