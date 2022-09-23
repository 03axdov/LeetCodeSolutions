class Solution:       
    def removeNthFromEnd(self, head, n: int):
        nodes = []
        node = head
        while node.next:
            nodes.append(node)
            node = node.next

        nodes.append(node)

        if len(nodes) == 1:
            return

        nodes.remove(nodes[len(nodes) - n])
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i+1]

        return nodes[0]