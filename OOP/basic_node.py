from typing import List


class BasicNode:
    def __init__(self, unique_id, priority, payload: object = None, children: List['BasicNode'] = None):
        self._unique_id = unique_id
        self._priority = priority
        self._payload = payload
        self._children = children if children is not None else []

    def get_unique_id(self):
        """

        :return:
        """
        return self._unique_id

    def get_priority(self):
        """

        :return:
        """
        return self._priority

    def get_payload(self):
        """

        :return:
        """
        return self._payload
