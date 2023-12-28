from typing import List


class BasicNode:
    def __init__(self, priority, unique_id, payload: object = None, children: List['BasicNode'] = None):
        self.priority = priority
        self.unique_id = unique_id
        self.payload = payload
        self.children = children if children is not None else []

