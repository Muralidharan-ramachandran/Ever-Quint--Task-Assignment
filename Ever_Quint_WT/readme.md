💧 Water Tank Problem – Trapped Rainwater
📌 Overview

This project solves the Water Tank (Trapping Rain Water) problem and presents the solution using a simple web application built with HTML, CSS, and Vanilla JavaScript.

Given an array representing block heights, the application computes how many units of water can be trapped between the blocks and displays the result visually.

🧩 Problem Statement

Input: An array of non-negative integers (n > -1)

Each integer represents the height of a block

Objective: Calculate the total units of water trapped between the blocks

Example

Input

[0,4,0,0,0,6,0,6,4,0]


Output

18 Units

🧠 Approach

Precompute maximum height to the left and right of each block

Water at each index is calculated as:

min(left_max, right_max) - block_height


Sum water across all indices

Time Complexity: O(n)
Space Complexity: O(n)

🛠️ Tech Stack

HTML

CSS

Vanilla JavaScript

▶️ How to Run

Clone the repository:

git clone https://github.com/Muralidharan-ramachandran/Ever-Quint--Task-Assignment.git


Navigate to the project folder:

cd Ever_Quint_WT


Open index.html in any web browser

👨‍💻 Author

R Muralidharan
B.Tech – Instrumentation & Control Engineering, NIT Trichy
GitHub: https://github.com/Muralidharan-ramachandran
