import uuid


class FibonacciHeap:
    def __init__(self):
        self.current_root = None
        self.heap_hash = {}


    def add_node(self, priority, unique_id=None, payload: object = None):
        """
        Method add_node is for adding entirely new user-specified nodes.
        """
        if unique_id is None:
            # If unique_id is None, then I should randomly generate a unique id for use in the hashmap using uuid.

            # The FibonacciHeap will return a handle (the unique ID) when adding a node. The user can choose to store it
            # That way, if they will need to arbitrarily update priorities later, they can do so with the unique ID.
            # If they choose not to store the handle, that's their problem.
        else:
            # If the user provided ID is not unique, throw an exception that they can check for and handle.
            # Create a custom exception class. This exception could have a method to generate an actually unique ID
            # so users can choose to use that ID in their exception handling, or do it their own way.
            # Could also include a create_similar_ID that creates a unique ID that is similar to the failed one.

        adding_node = BasicNode(priority=priority, unique_id=unique_id, payload=payload)
        self.heap_hash[unique_id] = adding_node

        if self.current_root is None:
            self.current_root = RootNode(basic_node=adding_node, left=None, right=None)
        else:
            # Figure out where in the fibonacci heap to put this node.
            # This may involve running a separate method.



