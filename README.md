#  News Search
It creates a search routine to perform queries on a set of documents defined.

## Programming Language
python3

## Installation
Ubuntu - sudo apt-get install python3
Windows - refer www.python.org

## Usage
```buildoutcfg
python3 search_query.py
```
This will ask for the query words(Not Case Sensitive) and search type, if search type is valid then it will 
return the respective query, else it will return the error.

Example :-
```
Enter Search keywords: care\
Enter Search Type
  1. AND
  2. OR
AND
{0, 1, 2, 3, 4, 5, 6}
```

## Test Cases
```buildoutcfg
python3 test_search_query.py
```
Have return one positive and negative unit test case to assert the data. 
The possible scenario for positive and negative unit test case, 
depends on the test case dictionary written inside the test_search_query.py

