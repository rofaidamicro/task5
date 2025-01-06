## Project: Binary Search Tree & SDN Traffic Classification
This repository contains two tasks involving a Binary Search Tree and SDN Traffic Classification using decision trees. The tasks are as follows:

# Task 1: Binary Search Tree
In this task, a Binary Search Tree (BST) is created and operated on using the following functions:

Insert: Inserts elements into the tree in the correct order.
Delete: Removes elements from the tree.
Search: Finds specific elements in the tree.
Traverse: Traverses the tree in different orders (in-order, pre-order, post-order).
Data:
We use three lists to build the BST and perform operations on it:
``` 
List a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
List b = [149, 38, 65, 197, 60, 176, 13, 217, 5, 11]
List c = [49, 38, 65, 97, 64, 76, 13, 77, 5, 1, 55, 50, 24]
```
Output:
For each operation (search, insert, delete, and traverse), the output will be printed in the console, and tree plots will be generated to show the updated structure of the tree after each operation.
# Task 2: SDN Traffic Classification with Decision Tree
In this task, we used decision tree classifiers to categorize SDN traffic into different protocol categories based on a dataset.

Approach:
Dataset: We used the SDN traffic dataset from the second practical exercise.
Algorithms: We implemented and compared the performance of two decision tree algorithms:
ID3 (Iterative Dichotomiser 3): A traditional decision tree algorithm that builds the tree based on entropy and information gain.
CART (Classification and Regression Trees): A more commonly used decision tree algorithm that builds binary trees using Gini impurity as the decision criterion.
Goal:
We aimed to classify SDN traffic into various categories or protocols and compare the performance of both decision tree algorithms using classification metrics.

# Problems Encountered in ISCXIDS2012 Tasks
While working on the ISCXIDS2012 tasks, I faced several challenges:

Large File Sizes: The dataset files were too large to push to GitHub due to the 100 MB size limit on GitHub, especially when trying to use Git LFS. This was resolved by storing the large files on an external platform.
Missing and Noisy Data: The dataset had missing values and noise, which made it difficult to properly train the models. Handling this was an iterative process, involving imputation techniques and feature engineering.
Model Performance: Achieving the desired performance in the network traffic classification tasks was challenging, as it required fine-tuning the models and testing with various algorithms and hyperparameters to reduce errors and improve accuracy.
the codes are in the compressed file I will be submitting along with the report where you'll find the link to this!
