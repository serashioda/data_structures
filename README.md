# data-structures

Sample code (with tests) for classic data structures implemented in Python.

## Linked List

- Can be initialized with (or without) iterable argument: LinkedList(iterable=None)

- Module: linked_list

- Attributes:

    - head: first node in linked list

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - remove(node): find and remove node from list

    - search(value): find and return first node with value equal to argument

    - display(): print list in pseudo-tuple format

## Stack

- Can be initialized with (or without) iterable argument: Stack(iterable=None)

- Module: stack

- Attributes:

    - top: top/first node on stack

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - size/len: return size of stack

## Doubly-Linked List

- Can be initialized with (or without) iterable argument: DoublyLinkedList(iterable=None)

- Module: dll

- Methods:

    - push(value): insert value at head of list

    - append(value): add value to tail of list

    - pop(): remove head and return its value

    - shift(): remove tail and return its value

    - remove(val): remove first instance of value in list, or raise exception if no matches

Doubly-linked lists vs Singly-linked Lists:

    Singly-linked lists and doubly-linked lists each have their own unique advantages and 
    disadvantages. Singly-linked lists require less code and less memory as each node only
    has a value and a single pointer. This also makes them faster for both removing and inserting
    near the head node. Doubly-linked lists, however, allow more efficient reverse searches/traversal
    and for quicker appending/removal of new nodes near the tail of the list. And if you ever need
    to look back as you're traversing along the list, doubly-linked lists are easy while,
    with a singly-linked list, you either have to keep track of the node behind as you traverse,
    or you have to traverse all the way up to it from the head.

## Queue

- can be initialized with (or without) iterable argument: Queue(iterable=None)

- Module: queue

- Methods:

    - enqueue(value): add value to end of queue

    - dequeue(): remove head of queue and return its value

    - peek(): return value of head of queue

    - len()/size(): return size of queue
    
## Deque (Double-Ended Queue)

- can be initialized with or without iterable argument

- Module: deque

- Attributes:

    - head
    
    - tail

- Methods:
    
    - append(value): add value to end of deque
    
    - appendleft(value): add value to front of deque
    
    - pop(): remove last item in deque and return its value
    
    - popleft(): remove first item in deque and return its value
    
    - peek(): return value of last item in deque
    
    - peekleft(): return value of first item in deque
    
    - len(deque) / deque.size(): return size of deque
    
## Binary Heap

- Module: bin_heap

- Optional arguments:
    
    - an iterable
    
    - minheap or maxheap ('min' or 'max') defaulted to 'min'

- Methods:
    
    - push(value): add value to bottom of heap and sort as needed
    
    - pop(value): remove first/root node and return its value, move last node to root, sort as needed


## Priority Queue

- can be initialized with (or without) iterable argument: Queue(iterable=None)

- Module: priority_queue

- Methods:

    - insert(data, priority): enqueue data with priority (defaults to 0), lower is
                higher priority

    - pop(): remove and return item of highest priority. If multiple items of the same
                priority exist, pop item first inserted.

    - peek(): return value of next item to be popped


## Graph

- Module: graph

- Methods:

    - add_node(n): add node to graph

    - del_node(n): delete node from graph along with edges it's part of

    - add_edge(n1, n2): add a new edge to the graph connecting ‘n1’ to ‘n2’, if either
                n1 or n2 are not already present in the graph, they are added.

    - del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
                raises an error if no such edge exists

    - g.nodes(): return a list of all nodes in the graph

    - g.edges(): return a list of all edges in the graph

    - g.has_node(n): True if node ‘n’ is contained in the graph, False if not.

    - g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges,
                raises an error if n is not in graph

    - g.adjacent(n1, n2): returns if there is an edge connecting n1 and n2,
                raises an error if either of the supplied nodes are not in graph

    - g.depth_first_traversal(start): Traverses graph depth first starting from 'start',
                returns path

    - g.breadth_first_traversal(start): Traverses graph breadth first starting from 'start',
                returns path

    - g.depth_first_traversal_iterative(start): Traverses graph depth first starting from 'start',
                returns path, slower than recursive version

### Weighted Graph

- Module: weighted_graph

- Methods:

    - same as graph

    - g.add_edge(n1, n2, weight)

### Shortest Path

- Module: shortest_path

- Methods:

    - same as weighted graph

    - g.dijkstra(start, end): return shortest path from start to end,
                implemented with dijkstra's algorithm.

    - g.floyd_warshall(): return path_dictionary, distance_dictionary for every
                possible path.

    - g.floyd_warshall_path(path, start, end): return shortest path from start
                to end.

### Binary Search Tree
- Module: bst
- Methods:
    - insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.

    - search(self, val): will return the node containing that value, else None

    - size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.

    - depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 0, if two values it will be 1, if three values it may be 1 or 2, depending, etc.

    - contains(self, val): will return True if val is in the BST, False if not.

    - balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.



# Machine Learning - Supervised Classifiers
## K Nearest Neigbor (Knn) Classifier:

- Module: knn
- K-Nearest Neigbour (Knn) algorithm:  categorizes based on the labels of the K closest data points. 
- The distance between two points (p and q) is calculated as:

```
d = sqrt(sum(p - q) ** 2)
```

- Methods:

    - Predict(dataset): Predict class values for unclassified dataset.

- Initialize:

### Knn(dataset, k=5)

- Advantages:

    - A low cost of learning
    - Often Successful when data is well mixed.

- Disadvantages:

    - Very inefficient for large data sets
    - No real model to interpret
    - Performance depends on the number of dimensions
    - Inconsistent results when there’s ties in votes

## Decision Tree Classifier

- Module: decision_tree

- Initialize:

    - Clf(min_leaf_size=1, max_depth=3)

- Methods:

    - fit(dataset, classes): Build a decision tree off of data. Dataset should be a list of rows, with the final element of         each row being the class value.

    - predict(dataset): Predict class values for unclassified dataset, using prebuilt tree.

    - cross_validate(dataset, classes): Splits a classified dataset in two, one to build the decision tree, the other to     
      predict with. Returns the percentage of predicted labels that match actual labels.

    - convert_csv(file): Reads csv file into useable format.


### Authors:
- Amos Bolder
- Sera Smith
- Ford Fowler

### Coverage:

```
======================= test session starts =========================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /Users/Sera/Dropbox/codefellows/401/data_structures, inifile: 
plugins: cov-2.4.0
collected 241 items 

src/test_bin_heap.py ..................
src/test_bst.py .............
src/test_deque.py .................
src/test_dll.py ........................
src/test_graph.py .............................
src/test_linked_list.py ...............
src/test_priority_queue.py .......
src/test_queue.py ..................
src/test_shortest_path.py ....................................
src/test_simple_graph.py .....................
src/test_stack.py .............
src/test_weighted_graph.py ..............................

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
src/bin_heap.py                 43      0   100%
src/bst.py                      45      0   100%
src/deque.py                    30      0   100%
src/dll.py                      73      0   100%
src/graph.py                    86      0   100%
src/linked_list.py              64      0   100%
src/priority_queue.py           19      0   100%
src/queue.py                    28      0   100%
src/shortest_path.py           146      0   100%
src/simple_graph.py             56      0   100%
src/stack.py                    21      0   100%
src/test_bin_heap.py            73      0   100%
src/test_bst.py                 79      0   100%
src/test_deque.py               53      0   100%
src/test_dll.py                103      0   100%
src/test_graph.py              118      0   100%
src/test_linked_list.py         68      0   100%
src/test_priority_queue.py      32      0   100%
src/test_queue.py               64      0   100%
src/test_shortest_path.py      155      0   100%
src/test_simple_graph.py        79      0   100%
src/test_stack.py               32      0   100%
src/test_weighted_graph.py     127      0   100%
src/weighted_graph.py           87      0   100%
----------------------------------------------------------
TOTAL                         1681      0   100%


====================== 241 passed in 0.82 seconds ========================
  
```
