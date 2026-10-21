# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**
Within your data limit.
Total Bill is $40.0
**Evidence (paste your terminal run):**

```
Enter GB used: 10
Enter Base Plane cost: 40
You are within your data limit.
Total Bill: $40.0

```

**Pass / Fail and why:**
Passed. It passed due to going through the correct boolean and if channels to output what we wanted.
## Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**
we will recive moderate usage and it being 50 buckaroos

**Evidence (paste your terminal run):**

```
Enter GB used: 15
Enter Base Plane cost: 40
You are 5.0 GB over your limit
Moderate Extra GB Usage
Total Bill: $50.0

```

**Pass / Fail and why:**
Passed. Went through all the boolan expretions and if/elif statments propperly.
## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**
I expect this to calc the decimal correctly via a float input
**Evidence (paste your terminal run):**

```
Enter GB used: 15.5
Enter Base Plane cost: 50
You are 5.5 GB over your limit
High Extra GB Usage
Total Bill: $61.0

```

**Pass / Fail and why:**
Passed due to having a float input rather than a int.
If a case fails, fix the program and add evidence of the rerun below that case.
