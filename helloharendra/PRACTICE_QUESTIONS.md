# Naya Prayog Academy — Python DS & AI
## Real-World Practice Questions
### (Basics Day 1–22 + Analytics Day 1–Day6 Seaborn)

> **Instructions for Students:**
> These problems are designed like real tasks you will face as a Data Analyst, Data Scientist, or AI/ML Engineer.
> Each problem gives you a scenario, a dataset to create (or is provided), and tasks to complete.
> Do NOT look at solutions first. Try on your own. Think like a professional.

---

## MODULE 1 — PYTHON BASICS

---

### PROJECT 1: Student Grade Manager
**Role:** You are a junior developer at a school management company.
**Scenario:** Build a console program that manages student grades.

**Tasks:**
1. Ask the user to enter a student's name, marks in 5 subjects (Math, Science, English, Hindi, Computer).
2. Calculate the total marks and percentage.
3. Assign a grade using the following rules:
   - 90% and above → Grade A
   - 75–89% → Grade B
   - 60–74% → Grade C
   - 40–59% → Grade D
   - Below 40% → Grade F (Fail)
4. Print a formatted report card like this:
   ```
   =============================
   Student Report Card
   =============================
   Name      : Rahul Kumar
   Total     : 420 / 500
   Percentage: 84.00%
   Grade     : B
   =============================
   ```
5. Handle the case where the user enters an invalid mark (not a number) using exception handling.

**Concepts used:** variables, input(), int/float conversion, f-strings, if-elif-else, try-except

---

### PROJECT 2: E-Commerce Cart System
**Role:** Junior Python Developer at an online shopping startup.
**Scenario:** Build a simple shopping cart using Python data structures.

**Tasks:**
1. Create a dictionary called `product_catalog` with at least 6 products and their prices. Example:
   ```python
   product_catalog = {
       "Laptop": 55000,
       "Mouse": 799,
       "Keyboard": 1299,
       "Monitor": 12000,
       "Headphones": 2499,
       "USB Hub": 599
   }
   ```
2. Create an empty list called `cart`.
3. Write a menu-driven program (using a while loop) that lets the user:
   - View all products with prices
   - Add a product to cart by name
   - Remove a product from cart
   - View current cart and total bill
   - Exit the program
4. If the user tries to add a product that doesn't exist, print `"Product not found in catalog."`
5. Show the total bill with 18% GST added.

**Concepts used:** dictionary, list, while loop, if-elif, break, in operator, f-strings

---

### PROJECT 3: Zomato Delivery Time Estimator
**Role:** Data Operations Analyst at a food delivery company.
**Scenario:** Build a program that estimates delivery time based on distance and traffic.

**Tasks:**
1. Ask the user:
   - Distance in km (float)
   - Traffic level: 1 = Low, 2 = Medium, 3 = High
2. Use these rules to calculate delivery time:
   - Low traffic: speed = 40 km/h
   - Medium traffic: speed = 25 km/h
   - High traffic: speed = 15 km/h
3. Calculate time in minutes: `time = (distance / speed) * 60`
4. Add a preparation time of 15 minutes always.
5. Print result:
   ```
   Estimated delivery time: 42 minutes
   ```
6. If the user enters an invalid traffic level (not 1, 2, or 3), show an error using exception handling.
7. **Bonus:** Use match-case instead of if-elif for traffic level.

**Concepts used:** input, float conversion, if-elif or match-case, arithmetic, try-except

---

### PROJECT 4: Number Pattern Analyzer
**Role:** Backend Developer — data validation team.
**Scenario:** Your company needs a tool that analyzes a list of numbers for patterns.

**Tasks:**
1. Create a list of 20 numbers entered by the user (use a loop to collect input).
2. Using list comprehension, create:
   - `even_numbers` — all even numbers from the list
   - `odd_numbers` — all odd numbers
   - `squared_values` — square of every number
   - `above_average` — numbers greater than the average of the list
3. Print all results in a clean format.
4. Find and print the maximum, minimum, and average of the list WITHOUT using max(), min() — write your own logic using loops.
5. Check if any number in the list is prime. Print all prime numbers found.

**Concepts used:** list, for loop, list comprehension, while loop, if conditions, user input, exception handling

---

### PROJECT 5: Bank Account System (OOP Style with Functions)
**Role:** Junior developer at a FinTech startup.
**Scenario:** Create a simple bank account simulation.

**Tasks:**
1. Write the following functions:
   - `create_account(name, initial_balance)` → returns a dictionary representing the account
   - `deposit(account, amount)` → adds money, returns updated balance
   - `withdraw(account, amount)` → deducts money; raise an error if amount > balance
   - `check_balance(account)` → prints current balance
   - `transaction_history(account)` → prints all past transactions
2. Each transaction (deposit/withdraw) should be stored in a list inside the account dictionary.
3. Handle invalid inputs (negative amounts, non-numeric) using try-except.
4. Run a demo: create an account, do 3 deposits, 2 withdrawals, print history.

**Expected output:**
```
Account created for: Priya Sharma | Balance: ₹5000
Deposited ₹2000 | New Balance: ₹7000
Withdrew ₹1500 | New Balance: ₹5500
--- Transaction History ---
+ ₹2000 (Deposit)
+ ₹3000 (Deposit)
- ₹1500 (Withdrawal)
```

**Concepts used:** functions, dictionary, list, loops, exception handling, f-strings

---

### PROJECT 6: Salary Calculator with Tax Slab
**Role:** HR Analyst — payroll automation team.
**Scenario:** Build a salary calculator using India's income tax slabs.

**Tasks:**
1. Ask the user to enter their annual CTC (Cost to Company).
2. Calculate basic salary, HRA, PF, and take-home:
   - Basic = 40% of CTC
   - HRA = 20% of Basic
   - PF (Employee) = 12% of Basic
   - Gross = Basic + HRA
   - Tax based on slab (below):
     ```
     0 – 3,00,000       → No tax
     3,00,001 – 7,00,000 → 5%
     7,00,001 – 10,00,000 → 10%
     10,00,001 – 12,00,000 → 15%
     Above 12,00,000    → 20%
     ```
   - Net Take-Home = Gross - PF - Tax (monthly)
3. Print a formatted salary slip.
4. Use a function `calculate_tax(annual_income)` to keep the tax logic separate.

**Concepts used:** functions, arithmetic, if-elif, f-strings, float formatting

---

### PROJECT 7: Fibonacci & Prime Generator for Cryptography Team
**Role:** Junior Security Developer.
**Scenario:** Generate sequences for internal testing.

**Tasks:**
1. Write a **recursive** function `fibonacci(n)` that returns the nth Fibonacci number.
2. Write a function `is_prime(n)` that returns True/False.
3. Write a function `first_n_primes(n)` using a while loop to generate the first N prime numbers.
4. Using list comprehension, find all Fibonacci numbers up to 500 that are also prime.
5. Using a generator (`yield`), write a `fib_generator()` that generates Fibonacci numbers one at a time.
6. Print the first 15 values from the generator.

**Concepts used:** recursion, functions, while loop, list comprehension, generators/yield

---

### PROJECT 8: Inventory Management — Search & Sort
**Role:** Warehouse Data Analyst.
**Scenario:** A warehouse needs quick item lookup and sorting.

**Tasks:**
1. Create a list of 10 product dictionaries:
   ```python
   inventory = [
       {"name": "Laptop", "qty": 15, "price": 55000},
       {"name": "Mouse", "qty": 200, "price": 799},
       ...
   ]
   ```
2. Implement **linear search** to find a product by name. Print all its details.
3. Sort the inventory by price (ascending) without using `.sort()` — implement **bubble sort** manually using nested loops.
4. Using list comprehension, filter all products where qty < 20 (low stock alert).
5. Use a set to detect if any product names are duplicated.
6. Print low stock products in a formatted table.

**Concepts used:** list of dicts, linear search, nested loops (bubble sort), list comprehension, sets

---

## MODULE 2 — DATA ANALYTICS (PANDAS + NUMPY + MATPLOTLIB + SEABORN)

---

### PROJECT 9: Sales Performance Dashboard (Pandas)
**Role:** Data Analyst at a retail company.
**Scenario:** Analyze monthly sales data and generate insights.

**Dataset to create:**
```python
import pandas as pd
import numpy as np

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"],
    "Region": ["North","South","East","West","North","South",
                "East","West","North","South","East","West"],
    "Product": ["Laptop","Phone","Tablet","Laptop","Phone","Tablet",
                 "Laptop","Phone","Tablet","Laptop","Phone","Tablet"],
    "Units_Sold": [120, 200, 150, 90, 210, 180, 130, 220, 160, 95, 230, 175],
    "Revenue":    [660000, 300000, 225000, 495000, 315000, 270000,
                   715000, 330000, 240000, 522500, 345000, 262500],
    "Returns": [5, 12, 8, 3, 15, 10, 6, 18, 9, 4, 20, 11]
}
df = pd.DataFrame(data)
```

**Tasks:**
1. Display first 5 rows, shape, columns, and data types using df.head(), df.info(), df.describe().
2. Add a new column `Net_Revenue` = Revenue - (Returns × average price per unit).
3. Add a column `Return_Rate` = Returns / Units_Sold * 100 (round to 2 decimal places).
4. Find: which region had the highest total revenue?
5. Find: which product had the most returns?
6. Use groupby to find total Units_Sold and Revenue per Region.
7. Use pivot_table to show Revenue by Product and Region.
8. Sort the DataFrame by Revenue (descending) and reset index.
9. Filter rows where Return_Rate > 5% — these are "High Return" products. Save to a new DataFrame.
10. Export the final DataFrame to a CSV file called `sales_report.csv`.

**Concepts used:** pd.DataFrame, head/info/describe, new columns, arithmetic on columns, groupby, pivot_table, sort_values, boolean filtering, to_csv

---

### PROJECT 10: HR Employee Analytics (Pandas + Missing Data)
**Role:** HR Data Analyst.
**Scenario:** Clean and analyze messy employee data.

**Dataset to create:**
```python
import pandas as pd
import numpy as np

data = {
    "Emp_ID":     [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name":       ["Ravi","Priya","Amit","Sneha","Karan",
                   "Deepa","Rohit","Anita","Vijay","Meena"],
    "Department": ["IT","HR","Finance","IT","Marketing",
                   "HR","Finance","IT","Marketing",None],
    "Salary":     [75000, 55000, 68000, None, 60000,
                   52000, None, 80000, 58000, 63000],
    "Experience": [5, 3, 7, 2, 4, 6, 1, 8, 3, None],
    "Rating":     [4.5, 3.8, 4.2, 3.5, None, 4.0, 3.2, 4.8, 3.9, 4.1],
    "City":       ["Delhi","Mumbai","Pune","Delhi","Bangalore",
                   "Mumbai","Chennai","Delhi","Pune","Mumbai"]
}
df = pd.DataFrame(data)
```

**Tasks:**
1. Find all missing values using `isnull().sum()`. Which columns have nulls?
2. Fill missing `Salary` with the department-wise average salary (use groupby + fillna + transform).
3. Fill missing `Department` with `"Unknown"`.
4. Fill missing `Rating` with the overall median rating.
5. Fill missing `Experience` with 0.
6. Add a column `Salary_Band`:
   - Below 55000 → "Junior"
   - 55000–70000 → "Mid"
   - Above 70000 → "Senior"
   Use apply() and a lambda or function.
7. Group by Department and find: average salary, average rating, employee count.
8. Find the top 3 highest-paid employees.
9. Which city has the most employees?
10. Merge this DataFrame with a new one:
    ```python
    bonus_data = pd.DataFrame({
        "Emp_ID": [101, 103, 105, 108, 110],
        "Bonus":  [15000, 12000, 10000, 20000, 11000]
    })
    ```
    Use a left merge on `Emp_ID`. Fill missing bonus with 0.

**Concepts used:** isnull, fillna, dropna, apply, lambda, groupby, sort_values, merge, boolean conditions

---

### PROJECT 11: NumPy — Student Exam Score Analyzer
**Role:** Academic Data Analyst.
**Scenario:** Analyze exam scores of 50 students across 5 subjects.

**Tasks:**
1. Create a 2D NumPy array of shape (50, 5) using `np.random.randint(30, 100, size=(50, 5))`.
   Columns: Math, Physics, Chemistry, English, CS
2. Calculate and print:
   - Average score per subject (column-wise mean)
   - Average score per student (row-wise mean)
   - Highest and lowest scorer (student index)
   - Standard deviation of each subject
3. Add 5 bonus marks to all Physics scores, but cap maximum at 100. (Use np.clip or np.where)
4. Using boolean indexing, find all students who scored below 40 in ANY subject (failing students).
5. Normalize the Math scores to a 0–1 scale: `(score - min) / (max - min)`.
6. Find the correlation between Math and Physics scores using `np.corrcoef()`.
7. Reshape the first 10 students' scores into a (2, 5, 5) 3D array.
8. Sort students by their total score (sum of all subjects) in descending order. Print the top 5.

**Concepts used:** np.random.randint, shape/ndim/dtype, axis-wise operations, boolean indexing, np.where, np.clip, np.corrcoef, reshape, argsort

---

### PROJECT 12: Stock Price Simulator (NumPy)
**Role:** Quantitative Analyst at a trading firm.
**Scenario:** Simulate and analyze stock price movements.

**Tasks:**
1. Create a starting price: `price = 1000.0`
2. Simulate 252 trading days (1 year) of daily returns using:
   ```python
   daily_returns = np.random.normal(0.001, 0.02, 252)  # mean, std, days
   ```
3. Calculate daily price series: each day's price = previous day's price × (1 + daily_return).
   Use a loop or NumPy cumulative product.
4. Find:
   - Maximum price reached (peak)
   - Minimum price reached (trough)
   - Final price after 252 days
   - Total return % = (final - start) / start * 100
5. Find all days where price dropped more than 3% in a single day.
6. Calculate a 20-day moving average of prices using a loop (for each day i >= 20, average of last 20 days).
7. Find the day (index) where the maximum price occurred using `np.argmax()`.

**Concepts used:** np.random.normal, cumulative operations, boolean indexing, np.argmax, np.argmin, loops with arrays

---

### PROJECT 13: Sales Revenue Visualization (Matplotlib)
**Role:** Business Intelligence Analyst.
**Scenario:** Create a complete visual dashboard for quarterly sales.

**Dataset:**
```python
quarters = ["Q1", "Q2", "Q3", "Q4"]
products = ["Laptop", "Phone", "Tablet"]
revenue = {
    "Laptop": [1200000, 1500000, 1100000, 1800000],
    "Phone":  [800000,  950000,  870000,  1050000],
    "Tablet": [400000,  450000,  390000,  520000]
}
```

**Tasks — Create the following charts using Matplotlib:**
1. **Line Chart:** Revenue trend for all 3 products across 4 quarters on the same chart. Add markers, legend, title, axis labels, and grid.
2. **Grouped Bar Chart:** Compare all 3 products side by side for each quarter.
3. **Pie Chart:** Total annual revenue share for each product. Show percentages.
4. **Horizontal Bar Chart:** Total revenue per product (annual sum), sorted ascending.
5. **Subplot Dashboard:** Combine all 4 charts into a single 2×2 subplot figure.
   - Add a main title: `"Annual Sales Dashboard — 2024"`
   - Use `tight_layout()`
6. Save the final dashboard as `sales_dashboard.png` with dpi=150.

**Concepts used:** plt.figure, plt.subplots, plt.plot, plt.bar, plt.barh, plt.pie, plt.title, plt.legend, plt.grid, plt.savefig, tight_layout

---

### PROJECT 14: Temperature Data Visualization (Matplotlib)
**Role:** Environmental Data Analyst.
**Scenario:** Analyze and visualize 30 days of temperature readings.

**Dataset to create:**
```python
import numpy as np
days = np.arange(1, 31)
city_a = np.random.normal(32, 4, 30)   # Delhi
city_b = np.random.normal(28, 3, 30)   # Mumbai
city_c = np.random.normal(22, 5, 30)   # Shimla
```

**Tasks:**
1. **Line Plot:** Plot temperature of all 3 cities over 30 days. Use different colors and line styles (solid, dashed, dotted). Add a legend.
2. **Histogram:** Distribution of Delhi temperatures. Use 10 bins, edge color black.
3. **Box Plot:** Compare temperature distribution of all 3 cities side by side.
4. **Scatter Plot:** Plot Delhi vs Mumbai temperatures as a scatter chart. Color points by temperature difference (use a colormap).
5. For the scatter chart, add `plt.colorbar()` to show the color scale.
6. Combine all 4 charts into a 2×2 subplot. Save as `temperature_report.png`.

**Concepts used:** plt.plot, plt.hist, plt.boxplot, plt.scatter, plt.colorbar, np.random.normal, subplots

---

### PROJECT 15: HR Analytics Dashboard (Seaborn)
**Role:** Senior HR Data Analyst.
**Scenario:** Use Seaborn to create professional HR visualizations.

**Dataset to create:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 100
df = pd.DataFrame({
    "Department":  np.random.choice(["IT","HR","Finance","Marketing","Operations"], n),
    "Gender":      np.random.choice(["Male","Female"], n),
    "Experience":  np.random.randint(1, 15, n),
    "Salary":      np.random.randint(40000, 150000, n),
    "Performance": np.random.choice(["Low","Medium","High"], n),
    "Age":         np.random.randint(22, 55, n),
    "Satisfaction": np.random.uniform(1, 5, n).round(1)
})
```

**Tasks:**
1. Set Seaborn theme to `"whitegrid"`.
2. **Count Plot:** Number of employees in each department. Color by Gender (use `hue="Gender"`).
3. **Box Plot:** Salary distribution by Department. Use `hue="Performance"`. Identify which department has the widest salary range.
4. **Violin Plot:** Age distribution by Performance level.
5. **Scatter Plot (sns.scatterplot):** Experience vs Salary, colored by Department.
6. **Bar Plot (sns.barplot):** Average salary per Department with confidence interval.
7. **Heatmap:** Correlation matrix of numeric columns (Salary, Experience, Age, Satisfaction). Use `annot=True`, colormap `"coolwarm"`.
8. **Pair Plot:** Show pairwise relationships between Salary, Experience, Age, and Satisfaction. Use `hue="Performance"`.
9. **KDE Plot:** Distribution of Salary by Gender (overlapping KDE plots for comparison).
10. **FacetGrid:** Create a grid of histograms of Salary, one plot per Department.

**Save all charts individually with descriptive names.**

**Concepts used:** sns.set_theme, sns.countplot, sns.boxplot, sns.violinplot, sns.scatterplot, sns.barplot, sns.heatmap, sns.pairplot, sns.kdeplot, sns.FacetGrid, hue parameter

---

### PROJECT 16: E-Commerce Customer Behavior Analysis (Full Stack — All Libraries)
**Role:** Junior Data Scientist at an e-commerce company.
**Scenario:** You've been given 3 months of order data. Analyze customer behavior end-to-end.

**Dataset to create:**
```python
import pandas as pd
import numpy as np

np.random.seed(10)
n = 200

df = pd.DataFrame({
    "Order_ID":    range(1001, 1001+n),
    "Customer_ID": np.random.randint(1, 51, n),        # 50 unique customers
    "Category":    np.random.choice(["Electronics","Fashion","Grocery","Books","Sports"], n),
    "City":        np.random.choice(["Delhi","Mumbai","Pune","Bangalore","Chennai"], n),
    "Order_Value": np.random.randint(200, 15000, n),
    "Discount":    np.random.choice([0, 5, 10, 15, 20], n),
    "Rating":      np.random.uniform(1, 5, n).round(1),
    "Returned":    np.random.choice([0, 1], n, p=[0.85, 0.15]),
    "Month":       np.random.choice(["January","February","March"], n)
})
# Introduce some missing values
df.loc[df.sample(10).index, "Rating"] = np.nan
df.loc[df.sample(5).index, "City"] = np.nan
```

**Part A — Pandas Tasks:**
1. Check for missing values and handle them appropriately (fill Rating with median, fill City with "Unknown").
2. Add `Final_Value` column = Order_Value × (1 - Discount/100).
3. Find: total revenue by Category per Month (use pivot_table).
4. Find: top 5 customers by total spending (groupby Customer_ID, sum Final_Value).
5. Which city has the highest return rate? (groupby City, mean of Returned × 100).
6. Filter orders where Rating < 3 AND Returned == 1. These are "Problem Orders".

**Part B — NumPy Tasks:**
7. Convert `Final_Value` column to a NumPy array.
8. Find mean, median, std, min, max of Final_Value.
9. Using boolean indexing on the array, find how many orders were above ₹5000.
10. Normalize Final_Value to 0–1 range.

**Part C — Matplotlib Tasks:**
11. Line chart: Total revenue per month.
12. Bar chart: Average order value by Category.
13. Histogram: Distribution of Order_Value (50 bins).

**Part D — Seaborn Tasks:**
14. Box plot: Order_Value by Category (hue by Month).
15. Heatmap: Average Final_Value per City vs Category (use pivot_table as input to heatmap).
16. Count plot: Number of orders per Category colored by Returned.
17. Scatter plot: Discount vs Rating (does higher discount mean better rating?).

**Final Deliverable:** Write 3 business insights based on your analysis.

**Concepts used:** ALL concepts from day1 through day6_seaborn

---

## BONUS CHALLENGE — CAPSTONE

### PROJECT 17: IPL Cricket Analytics Report
**Role:** Sports Data Analyst at a cricket analytics firm.
**Scenario:** Build a complete cricket performance dashboard using only what you've learned.

**Dataset to create:**
```python
import pandas as pd
import numpy as np

np.random.seed(5)
teams = ["Mumbai Indians","Chennai Super Kings","Royal Challengers",
         "Kolkata Knight Riders","Delhi Capitals","Sunrisers Hyderabad"]

matches = pd.DataFrame({
    "Match_ID":  range(1, 61),
    "Team1":     np.random.choice(teams, 60),
    "Team2":     np.random.choice(teams, 60),
    "Venue":     np.random.choice(["Wankhede","Chepauk","Eden Gardens","Chinnaswamy","Feroz Shah Kotla"], 60),
    "Team1_Score": np.random.randint(120, 220, 60),
    "Team2_Score": np.random.randint(110, 210, 60),
    "Season":    np.random.choice([2021, 2022, 2023], 60)
})
matches["Winner"] = np.where(matches["Team1_Score"] > matches["Team2_Score"],
                              matches["Team1"], matches["Team2"])
```

**Tasks:**
1. **(Pandas)** Find total matches won by each team across all seasons.
2. **(Pandas)** Find average score for each team as Team1 vs as Team2.
3. **(Pandas)** Find which Venue had the highest average total score (Team1 + Team2).
4. **(NumPy)** Calculate the "run margin" = |Team1_Score - Team2_Score| for each match. Find mean and max margin.
5. **(Matplotlib)** Bar chart: Total wins per team. Horizontal. Sorted by wins.
6. **(Matplotlib)** Line chart: Average match scores per season (both teams combined).
7. **(Seaborn)** Box plot: Score distribution (Team1_Score and Team2_Score) — compare spread.
8. **(Seaborn)** Count plot: Wins by team per season (hue=Season).
9. **(Seaborn)** Heatmap: Number of matches played at each Venue per Season.
10. **(Python Basics)** Write a function `team_report(team_name, df)` that prints:
    - Total matches played
    - Total wins
    - Win percentage
    - Average score when batting first

---

## TOPIC REFERENCE GUIDE (What Concept Is Tested Where)

| Concept | Projects |
|---|---|
| Variables, data types, input() | 1, 3, 6 |
| if-elif-else, match-case | 1, 3, 6 |
| while loop, break | 2, 4, 7 |
| for loop, range() | 4, 5, 8 |
| List comprehension | 4, 7, 8 |
| Functions, return | 5, 6, 7, 17 |
| Recursion | 7 |
| Exception handling | 1, 2, 5 |
| Generators (yield) | 7 |
| Linear search, sets | 8 |
| Pandas Series/DataFrame | 9, 10, 16 |
| fillna, dropna | 10, 16 |
| groupby, pivot_table | 9, 10, 16 |
| merge, concat | 10 |
| apply, lambda | 10 |
| NumPy arrays, indexing | 11, 12, 16 |
| NumPy statistics | 11, 12, 16 |
| Broadcasting, reshape | 11 |
| Matplotlib line/bar/pie | 13, 14, 16 |
| Matplotlib subplots | 13, 14 |
| Seaborn categorical plots | 15, 16, 17 |
| Seaborn heatmap, pairplot | 15, 16, 17 |
| End-to-end analysis | 16, 17 |

---

*Naya Prayog Academy — "Practice Like a Professional, Think Like an Analyst"*
