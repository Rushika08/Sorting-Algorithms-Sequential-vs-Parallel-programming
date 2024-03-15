# Sorting Algorithms in Sequential vs Parallel programming

This repository contains implementations of sequential and parallel sorting algorithms in Python, focusing on Merge Sort and Quick Sort algorithms. The parallel implementations utilize the multiprocessing module to leverage multiple CPU cores for faster sorting of large datasets.

## Introduction

Sorting algorithms are fundamental to computer science and are used extensively in various applications. Merge Sort and Quick Sort are two efficient sorting algorithms commonly used for sorting large datasets.

This program provides implementations of Merge Sort and Quick Sort in both sequential and parallel manners using Python's multiprocessing module to leverage multiple CPU cores for parallel processing.

## Usage

To run the program, execute the Python script main.py. The program will output the execution time for each sorting algorithm in both sequential and parallel modes.

## Requirements

Python 3,
multiprocessing module (built-in)

## Implemented Algorithms
### Sequential Algorithms
#### Merge Sort: 
A divide-and-conquer algorithm that recursively divides the array into halves until each sub-array contains only one element, then merges them back together in sorted order.

#### Quick Sort: 
Another divide-and-conquer algorithm selects a pivot element and partitions the array into two sub-arrays, one with elements less than the pivot and the other with elements greater than the pivot. It then recursively sorts the sub-arrays.

### Parallel Algorithms
#### Parallel Merge Sort: 
A parallelized version of Merge Sort that utilizes multiprocessing to split the sorting task across multiple CPU cores, improving performance for large datasets.

#### Parallel Quick Sort: 
A parallelized version of Quick Sort also employs multiprocessing for concurrent sorting of sub-arrays.

### Performance Evaluation
The program evaluates the performance of each sorting algorithm by measuring the execution time for sorting a large random list of integers. It compares the execution time of sequential and parallel implementations of Merge Sort and Quick Sort.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or create a pull request.
