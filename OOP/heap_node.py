from .basic_node import BasicNode


class HeapNode:
    def __init__(self, basic_node: BasicNode, parent):
        self._basic_node = basic_node
        self._parent = parent

    def get_parent(self):
        """

        :return:
        """
        return self._parent



