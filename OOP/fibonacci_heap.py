from .basic_node import BasicNode
from .heap_node import HeapNode
from .root_node import RootNode
import uuid


class FibonacciHeap:
    def __init__(self, heap_type):
        self.current_root = None
        self.heap_hash = {}

        if heap_type not in ["max", "min"]:
            raise ValueError("Invalid heap type: must be 'max' or 'min'.")
        else:
            self.is_max_heap = heap_type == 'max'

    def add_node(self, priority, unique_id=None, payload: object = None):
        """
        Method add_node is for adding entirely new user-specified nodes.
        :param priority: A numeric value that indicates the priority of this node.
        :param unique_id: A unique ID that will be used to access this node quickly via the heap_hash dictionary.
        :param payload: A custom object that the user may store in the node to add versatility to the structure.
        :return: The unique ID, so that the user may store it to keep track of specific nodes they care about.
        """
        # Handling the priority
        if not isinstance(priority, (int, float)):
            raise TypeError(f"Invalid priority: must be numeric, but received {type(priority)} instead.")

        # Handling the unique_id
        if unique_id is None:
            unique_id = uuid.uuid4()
        elif unique_id in self.heap_hash:
            raise ValueError(f"Invalid unique ID: ID {unique_id} is already in use.")

        # Create the node using the parameters
        adding_node = BasicNode(priority=priority, unique_id=unique_id, payload=payload)

        # Operations for maintaining the FibonacciHeap
        # Add the node to the heap_hash using the unique_id as the key
        self.heap_hash[unique_id] = adding_node

        # Place the new node in the appropriate place within the Fibonacci Heap
        if self.current_root is None:
            self.current_root = RootNode(basic_node=adding_node, left=None, right=None)
        else:
            # Figure out where in the fibonacci heap to put this node.
            # This may involve running a separate method.

        # Return the unique_id so that users may store it to keep track of this node if they want to.
        return unique_id



