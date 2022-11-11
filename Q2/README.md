# DEBUG0001. Dataset Validity
Your colleague has prepared a function to check the validity of a dataset. The function should return **true and an empty list** when _all items_ in the list have _isValid = true_, 
and return ```false``` with ***the List of errors*** if the item is ```isValid = false```.

Please find the sample data provided by your manager in below ```input```.

Please implement the function provided in pseudo-code below and fix the validation logic.
```
Read data from input file
allValid = true
errorCodes = []
for each record in input file:
    allValid = record.isValid
    if record.isValid is not true:
        errorCodes append error message

if allValid is true:
    print "Yes"
else:
    print "No"
    print errorCodes sepearated by space character
```


## Input
The first line contains a number **N** `(1 ≤ N ≤ 1000)`, the total number of records <br>
The subsequent N lines contain the record of each item splitted by space character (" "). The first string indicates the **id** of the item, the second string indicates the **isValid** variable, and the third string indicates the **errorMessage** if applicable.

Example:
```
5
1 false ERR_OOM
2 true
3 false ERR_TIME_OUT
4 true
5 true
```


## Output (Expected)
```
No
ERR_OOM ERR_TIME_OUT
```

Explanation: <br>
The item 1 and 3 have `isValid` = false, thus the first output (whether all items are valid) is `No`.\
Then the second line will print all error message for `isValid` = false