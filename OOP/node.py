from typing import List


class Node:
    def __init__(self, unique_id, priority, payload: object = None,
                 children: List['Node'] = None, parent=None, left=None, right=None):
        # Public attributes
        self.unique_id = unique_id
        self.priority = priority
        self.payload = payload
        # Internal attributes
        self._children = children if children is not None else []
        self._parent = parent
        self._left = left
        self._right = right
        
    def add_child(self, new_child):
        """
        
        :param new_child: 
        :return: 
        """
            
            
            
            
            
            
            