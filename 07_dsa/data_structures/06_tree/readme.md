
# Trees
- Binary Trees, Binary Search Trees (BST)
- AVL Tree, Red-Black Tree
- Tree traversals (inorder, preorder, postorder)
- Binary Heaps

## Intro 
- A tree is a non-linear hierarchical data structure
- top node is called the root-node having child nodes.

## Applications of Trees:
- File systems
- Databases
- XML documents
- Artificial intelligence

## Traversal of Tree
- In-Order: Visit left subtree, current node, then right subtree.
- Pre-Order: Visit current node, left subtree, then right subtree.
- Post-Order: Visit left subtree, right subtree, then current node.

## Binary Trees
- A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.

## Binary Search Trees (BST)
- A Binary Search Tree is a binary tree where each node has a key, and:

- The key in the left subtree of a node is less than the node’s key.
- The key in the right subtree of a node is greater than the node’s key.
- The left and right subtrees must also be binary search trees.

## AVL Tree
- An AVL tree is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one. If at any time they differ by more than one, rebalancing is performed.
- Insertion or deletion might make the tree unbalanced, so after every insertion or deletion, check the balance factor and apply appropriate rotations.

## Red-Black Tree
- A Red-Black Tree is a type of self-balancing BST with the following properties:

- Each node is either red or black.
- The root is always black.
- Red nodes cannot have red children (no two red nodes can be adjacent).
- Every path from a node to its descendant NULL nodes has the same number of black nodes.

## Binary Heap
- A binary heap is a complete binary tree which satisfies the heap property:

- Min-Heap: The key at the root must be the minimum among all keys present in the binary heap, and the same property must be recursively true for all subtrees.
- Max-Heap: The key at the root must be the maximum among all keys present in the binary heap.


## Classification of trees

### By Degree
- Trees can be classified based on the maximum number of children each node can have.
1. Binary Tree (Each node has at most two children.)
2. Ternary Tree (Each node has at most three children.)
3. N-ary Tree (Each node has at most N children.)

### By Ordering
- Trees can be classified based on the ordering of nodes and subtrees
1. Binary Search Tree (BST)
Left child < parent < right child for every node.
2. Heap (Specialized binary tree with the heap property.)

### By Balance
- Trees can be classified based on how well-balanced they are.
1. Balanced Tree (Heights of subtrees differ by at most one. Examples include AVL trees and Red-Black trees.)
2. Unbalanced Tree (Heights of subtrees can differ significantly, affecting performance in operations like search and insertion.)


