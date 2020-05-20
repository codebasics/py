### Binary Tree Part 2 Exercise

Modify delete method in class [BinarySearchTreeNode class](https://github.com/codebasics/py/tree/master/DataStructures/9_Binary_Tree_2/binary_tree_part_2.py)
to use min element from left subtree. You will remove lines marked with ---> and use max value from left subtree

```
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

          --->  min_val = self.right.find_min()
          --->  self.data = min_val
          --->  self.right = self.right.delete(min_val)
```

[Solution](https://github.com/codebasics/py/tree/master/DataStructures/9_Binary_Tree_2/Exercise/binary_tree_part_2_exercise.py)

