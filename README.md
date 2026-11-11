# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

### 1. What concepts or skills did you learn while completing this assignment?

While completing this assignment, I learned how Binary Search Trees (BSTs) organize and store data using nodes and pointers. I practiced using recursion to insert values, search for specific values, and perform an in-order traversal. I used the 2026 Las Vegas Raiders receiving-yard statistics to make the assignment more interesting and connect the concepts to something I enjoy following. One thing I learned is that an in-order traversal visits the left subtree, the current node, and then the right subtree. This allows the values to be displayed in ascending order without having to sort them separately.

### 2. What challenges did you encounter, and how did you overcome them?

One challenge I encountered was understanding how recursive methods move through the tree when inserting and searching for values. At first, it was difficult to visualize how each value was placed on the left or right side of a node. I overcame this by using actual Raiders receiving-yard statistics and tracing where each value belonged based on whether it was smaller or larger than the current node. I also tested different situations, including searching for values that did not exist, inserting duplicate values, and working with an empty tree. These tests helped me understand how the program handled different situations and made it easier to identify errors.

### 3. Explain BST behavior and compare how ordering creates efficiency compared to other data structures.

A Binary Search Tree works by organizing values so that smaller values are placed on the left side of a node and larger values are placed on the right. This ordering makes searching more efficient because the program can eliminate part of the tree during each comparison instead of checking every value. When a BST is balanced, searching, inserting, and deleting values can take approximately O(log n) time. In comparison, searching through an unsorted list generally takes O(n) time because each item may need to be checked. A sorted array can also provide O(log n) searching through binary search, but inserting or deleting values can require shifting other elements. One disadvantage of a BST is that if it becomes unbalanced, its performance can decrease to O(n). Overall, I learned that the way a data structure organizes information has a major impact on how efficiently a program can access and manage data.
