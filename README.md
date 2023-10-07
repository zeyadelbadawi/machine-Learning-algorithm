# machine-Learning-algorithms
This Python code appears to be a program for implementing various neural network algorithms, including K-Means, MaxNet, Self-Organizing Maps (SOM), and Self-Organizing Competitive Networks (SCN). The program provides a menu-based interface for selecting one of these algorithms and then executing it. Here's a brief explanation of each algorithm and how the code is structured:

1) K-Means:

The program prompts the user to enter the number of data points and their coordinates.
It also asks for the number of reference points (m) and their initial coordinates.
It then calculates the closest reference point for each data point and updates the reference points based on the mean of the data points assigned to them.
The process continues until the reference points no longer change significantly.

2) MaxNet:

The program prompts the user to enter the number of signals and their values.
It also asks for the inhibitory weight.
It repeatedly calculates the result of a specific equation involving the signals and inhibitory weight until only one signal remains non-zero, which is considered the winner.

3) Self-Organizing Map (SOM):

The program prompts the user to enter the number of output values, vectors' component count, and the number of vectors.
It allows the user to enter vectors manually or generate a random matrix.
The program then performs the SOM algorithm, updating a matrix of weights to cluster the input vectors.

4) Self-Organizing Competitive Network (SCN):

Similar to SOM, it prompts the user to enter the number of output values, vectors' component count, and the number of vectors.
It also allows the user to enter vectors manually or generate a random matrix.
The program performs the SCN algorithm, updating the matrix of weights to find the winning output for each input vector.
The code structure involves separate functions for each algorithm, making it easy to understand and maintain. It also uses a loop to repeatedly ask the user for their choice of algorithm until a valid choice is made. Each algorithm has its own set of user inputs and processing steps.

To run the program, you can execute the script and follow the menu to select the desired algorithm. Make sure you have the NumPy library installed, as it is used for matrix operations in the SOM and SCN algorithms.
