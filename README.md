# fibonacci-heaps
This will be a custom implementation of the Fibonacci heap advanced data structure in both a functional and object oriented style.

## Object Oriented Implementation
**Composition over inheritance**
Fibonacci Heaps contain two kinds of nodes: RootNode, which are top level nodes that are part of the doubly linked list, and HeapNode, which are part of the heaps but not roots. These classes could have inherited from the BasicNode class, but I chose to have them composed of the BasicNode instead, meaning that they hold a BasicNode object as one of their attributes. This has a few key benefits:
1. Clean & Readable code: Converting between HeapNode and RootNode when doing operations on the FibonacciHeap object is easier and cleaner to implement. I can just access the BasicNode attribute and pass it to the constructor of either HeapNode or RootNode.
2. Speed & Efficiency: When passing the BasicNode to the constructor of either HeapNode or RootNode, it is passed as a reference. The underlying BasicNode object remains unchanged in memory which is efficient. If instead I had used inheritance, converting a HeapNode to RootNode or visaversa would require deleting objects and creating new ones. That is computationally more expensive and slower.

## Functional Implementation
**tbd**
