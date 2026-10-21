# Engineering Design

**Team members:**

Plan how your code will meet the product requirements. Keep answers brief.
It will calc how

## Inputs
GB used: 
Base Plan Cost:

*List each input and its Python data type. Note the input assumptions.*

## Processing and decisions

used GB * 2 buckaroos
GB used to 5 extra moderate 
GB used to 10 extra is high 

*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*

## Output

Cost of total bill 
Usage amount 
your over limit 
or
not over limit

*What will the program display for each usage category?*

## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

-base tolerance 
-
-input GB used
-input Base Plan Cost
-
-int calc of Gb over to buckaroos
-
-if gb <= 5 then is moderate
-if gb > 5  then is HIGH
-
-Output Status on usage "You are within your data limit" OR "You are (number) GB over your limit"
-Output Total Bill





```text
Enter data used (GB): 13
Enter base plan cost: 40
You are 3.0 GB over your limit. 
Moderate extra usage.
Your total bill is: $46.00
```

```text
Enter data used (GB): 9
Enter base plan cost: 40
You are within your data limit.
Your total bill is: $40.00
```