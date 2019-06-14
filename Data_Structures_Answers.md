Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) or Constant time.

2. What is the space complexity of your ring buffer's `append` function?
O(1) since we're only passing one parameter into the method.

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) technically since `self.storage` can be of variable length depending on the ring buffer created.

4. What is the space complexity of your ring buffer's `get` method?
O(n) I think since the result we're returning can be of variable length depending upon the storage capacity.

5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) because it's using a nested for loop, both of 10,000 items each.

6. What is the space complexity of the provided code in `names.py`?
O(n) because we're creating more space dependent on how many duplicates there are between the two files.

7. What is the runtime complexity of your optimized code in `names.py`?
O(n) since we only have one for loop and the dictionary lookup time is constant when checking for duplicates.

8. What is the space complexity of your optimized code in `names.py`?
O(n) because we're adding a variable amount of duplicates to an list.
