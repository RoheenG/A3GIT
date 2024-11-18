# **Increasing Split Tester**

This program checks whether a given number can be split into increasing sequences, based on a provided split size. It performs a series of checks to verify if the split pieces meet the required conditions, such as being strictly increasing and not containing duplicates.

## **Overview**

The program allows users to input a positive integer and a split size. It will then divide the integer into equal-length pieces and check if the pieces form a strictly increasing sequence. If the sequence is valid, it will print a message indicating that the sequence is increasing; otherwise, it will indicate that the sequence is not increasing.

## **How It Works**

The user is prompted for their name and whether they would like to test an integer for an increasing split.
If the user chooses "yes," they are asked to input a positive integer and a valid split size.
The program divides the integer into pieces of the specified size and checks the following:
The pieces should be strictly increasing.
No duplicate pieces should exist.
The length of the number should be divisible by the split size.
The program will print whether the sequence of pieces is increasing or not.
Functions in the Program

**split_tester(N, d)**

This function splits the number N into pieces of length d and checks if the pieces:
Are strictly increasing.
Do not contain duplicates.
Satisfy the condition where each piece's value is greater than the previous one.
Returns True if all conditions are met; otherwise, False.

**main()**

This is the main function that interacts with the user, guiding them through the process of entering their name, a number, and a split size.
The function validates the inputs to ensure they meet the criteria and prints whether the sequence is increasing or not.

**How to Use**

1. Run the program.

2. Enter your name when prompted.

3. Answer whether you want to test a number.

4. If "yes," enter a positive integer and a split size.

5. The program will display the result, telling you if the sequence of pieces is increasing or not.
