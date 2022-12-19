Good morning! Here's your coding interview problem for today.

This problem was asked by Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words `code`, `cob`, `be`, `ax`, `war`, and `we`.

       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \
x   b  e   r  e

C
|
O
|
B


The tree is structured according to the following rules:

- left child nodes link to words lexicographically earlier than the parent prefix
- right child nodes link to words lexicographically later than the parent prefix
- middle child nodes continue the current word

For instance, since code is the first word inserted in the tree, and cob lexicographically precedes cod, cob is represented as a left child extending from cod.

Implement insertion and search functions for a ternary search tree.

---

-Search tree
-Lexicographic search tree
-Search tree algorithms 
-Insertion algorithm for a tree
-Chuck doesn't know what hes talking about
-Is it possible to represent a tree in a dictionary 
-Class for NODE
-Class for the entire tree structure
-Come up with two additional words that aren't in the example. No more than 2 or 3 letters.

1. Be able to yknow hm be able to create the tree and use an insert function to put each word into its correct posititon and then the second thing of course is
2. When given a word that has already been inserted be able to search the tree and find that word cool alright