
<div align="center">
  <h3 align="center">MSCS532 Assignment 3</h3>
</div>

<!-- CLONING THE REPOSITORY -->
## Cloning the Repository

To get a local copy of this repository, use the following commands:
```sh
# Clone the repository
git clone https://github.com/abhattarai28547/MSCS532_Assignment3.git

# Navigate into the project directory
cd MSCS532_Assignment3
```
<!-- Running the code-->
### Randomized Quicksort

To test the **Randomized Quicksort** implementation, execute:
```sh
python randomized_quicksort.py
```
This will run the Randomized Quicksort algorithm on a sample array and output the sorted result.

### Deterministic Quicksort Comparison

To compare the performance of **Randomized Quicksort** with **Deterministic Quicksort**, execute:
```sh
python deterministic_quicksort_comparison.py
```
This script compares the running times of both algorithms on different array sizes and distributions and displays the results.

### Hash Table with Chaining

To test the **Hash Table with Chaining** implementation, run:
```sh
python hash_table.py
```
This script will demonstrate basic operations such as insertion, searching, and deletion in the hash table.

<!-- CUSTOMIZATION -->
Customization
You can modify the hardcoded elements, such as arrays in the implementations, directly within their respective Python files:

`randomized_quicksort.py`: Edit the sample array inside the script to test different input scenarios.

`deterministic_quicksort_comparison.py`: Adjust the array sizes and distributions in the script to explore performance variations.

`hash_table.py`: Change the key-value pairs or the operations performed to fit your testing needs.

 <!-- SUMMARY OF FINDINGS -->

 
### Summary of Findings
<div>  
  <li>Randomized Quicksort: This implementation showed superior performance across various input distributions compared to Deterministic Quicksort. The average-case time complexity of 𝑂(𝑛log𝑛)
  O(nlogn) was confirmed through empirical testing, aligning well with theoretical expectations.</li>
  
  <li>Deterministic Quicksort: This algorithm performed less efficiently on already sorted and reverse-sorted arrays due to suboptimal pivot selection strategies. It consistently demonstrated worse performance compared to the randomized variant.</li>
  
  <li>Hash Table with Chaining: The hash table demonstrated efficient average-case performance for insertion, search, and deletion operations, typically achieving 
  𝑂(1). Effective performance management, including dynamic resizing, is essential for maintaining low load factors and minimizing collisions.</li>
</div>

### Instructions:
<ol>
  <li>
    Clone the Repository: Use the provided Git commands to clone the repository and navigate into the project directory.
  </li>
  <li>
    Run Scripts: Execute the Python scripts using the provided commands.
  </li>
  <li>
    Customize: Modify the hardcoded elements in the Python files as needed for different testing scenarios.
  </li>
  <li>
    Review Findings: Refer to the summary of findings to understand the performance characteristics observed during the implementation and testing.
  </li>
</ol>

This `README.md` now includes detailed instructions for running the implementations, customizing them, and a summary of the findings.
