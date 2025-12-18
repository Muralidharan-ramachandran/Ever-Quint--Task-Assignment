🏗️ Max Profit Optimization Problem
📌 Problem Overview

Mr. X owns an infinite strip of land on Mars Land and wants to maximize his earnings by constructing different types of establishments within a fixed time frame.

He can build:

Theatres (T)

Pubs (P)

Commercial Parks (C)

Each establishment:

Takes a specific amount of build time

Generates revenue per unit of operational time

Cannot be built in parallel (only one construction at a time)

The objective is to find all possible construction plans that yield the maximum total profit for a given time input n.

🧩 Establishment Details
Building Type	Build Time	Earnings per Unit Time
Theatre (T)	5 units	$1500
Pub (P)	4 units	$1000
Commercial Park (C)	10 units	$2000
⚙️ Constraints & Assumptions

Only one building can be constructed at any given unit of time.

Earnings begin after construction is completed.

Total available operational time = n - total_construction_time.

If multiple plans yield the same maximum profit, all must be returned.

🧠 Approach & Logic

Brute-force Enumeration

Iterate through all valid combinations of:

Commercial Parks

Theatres

Pubs

Ensure total build time does not exceed available time.

Profit Calculation

Remaining operational time (RT) is computed after construction.

Profit formula:

Profit = RT × (T × 1500 + P × 1000 + C × 2000)


Optimal Plan Selection

Store all valid plans with their profits.

Identify the maximum profit.

Return all plans that match this maximum value.

This approach guarantees correctness while remaining computationally feasible due to constrained build times.

🧪 Sample Input & Output
Input
Enter the value of n: 7

Output
All optimal ways for n=7:

T=0, P=1, C=0, RT=3, profit=3000
T=1, P=0, C=0, RT=2, profit=3000


✔️ Both plans yield the same maximum profit, so both are returned.

▶️ How to Run the Code

Ensure Python 3 is installed

Copy the code into a .py file or Jupyter Notebook

Run the script:

python max_profit.py


Enter the value of n when prompted

🧠 Key Concepts Used

Brute-force optimization

Constraint handling

Profit maximization

Nested iteration

Problem modeling

🚀 Possible Enhancements

Convert brute-force logic to Dynamic Programming

Add time complexity optimizations

Create a visual dashboard for profit comparison

Extend to support parallel construction as a variant

👨‍💻 Author

R Muralidharan
B.Tech – Instrumentation & Control Engineering, NIT Trichy
GitHub: https://github.com/Muralidharan-ramachandran
