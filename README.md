# Machine-Learning
Machine learning / linear regression


In this program, I used Python to implement a linear regression of data.
I used a dataset from the Stanford Large Network Dataset Collection shows a product copurchasing network on Amazon.
I calculated the RMS value of the dataset to be around 95,000. That means that the data is
mostly uncorrelated, but that is to be expected, because the data I used is supposed to
represent a graph with edges and nodes, not a polynomial curve.


With such large data, I encountered a few obstacles with the runtime complexity of the
program. Initially, I wanted to separate the data into training data and test data by using
the pop function for lists, but the compiler was taking too long to compile. From the Python
Wiki (https://wiki.python.org/moin/TimeComplexity), I found that the pop function is
O(n) runtime complexity. So, using this function was not efficient, and I had to use
something else. In the end, I shuffled the x and y lists, and then separated each list into two
chunks. This was O(1) runtime complexity.


Dataset: https://snap.stanford.edu/data/#amazon
