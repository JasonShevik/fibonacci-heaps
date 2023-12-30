from .basic_node import BasicNode


class RootNode:
    def __init__(self, basic_node: BasicNode, left, right):
        self._basic_node = basic_node
        self._left = left
        self._right = right

    def get_left(self):
        """

        :return:
        """
        return self._left

    def get_right(self):
        """

        :return:
        """
        return self._right









