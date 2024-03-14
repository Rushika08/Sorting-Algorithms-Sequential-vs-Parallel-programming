# Sorting-Algorithms-Sequential-vs-Parallel-programming

This Python program demonstrates sequential and parallel implementations of two popular sorting algorithms: Merge Sort and Quick Sort. It compares the performance of these algorithms in both sequential and parallel manners.

## Introduction

Sorting algorithms are fundamental to computer science and are used extensively in various applications. Merge Sort and Quick Sort are two efficient sorting algorithms commonly used for sorting large datasets.

This program provides implementations of Merge Sort and Quick Sort in both sequential and parallel manners using Python's multiprocessing module to leverage multiple CPU cores for parallel processing.

## Usage

To run the program, execute the Python script main.py. The program will output the execution time for each sorting algorithm in both sequential and parallel modes.

## Requirements

Python 3.x
multiprocessing module (built-in)

## Implementation Details

### Sequential Merge Sort
The merge_sort function recursively divides the input array into halves until each sub-array contains only one element. Then, it merges these sorted sub-arrays to produce the final sorted array.

### Sequential Quick Sort
The quick_sort function selects a pivot element from the array and partitions the array into three parts: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot. It recursively sorts the sub-arrays to achieve the final sorted array.

### Parallel Merge Sort
The parallel_merge_sort function is similar to the sequential merge sort but leverages Python's multiprocessing module to perform parallel sorting. It divides the input array into halves and recursively sorts each half in parallel using multiple processes.

### Parallel Quick Sort
The parallel_quick_sort function follows the same logic as sequential quick sort but utilizes parallel processing for sorting sub-arrays. It divides the input array into smaller sub-arrays and sorts them concurrently using multiple processes.

### Performance Evaluation
The program evaluates the performance of each sorting algorithm by measuring the execution time for sorting a large random list of integers. It compares the execution time of sequential and parallel implementations of Merge Sort and Quick Sort.
