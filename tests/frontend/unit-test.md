## unit tests:
<br /> 

| Scenario Group | Test ID | Decription | Test Steps | Expected Output | Factors | Metrics | Remarks |
| :-             | :-      | :-         | :-         | :-              | :-      | :-      | :-      |
|User Interaction|UT01|Testing origin and destination airport|1.Select the origin airport<br />2. Select the dstination airport|Data will be filtered according to input values|Correctness|-|-|
|User Interaction|UT02|Leaving origin and destination airport as null|1. Leave origin airport as empty<br />2. Leave destination airport as empty|No table displayed.|Correctness|-|-|
|User Interaction|UT03|Viewing the month drop down |1. click on the drop down to view the list of months|List of months from January to December should appear.|Correctness|-|-|
|User Interaction|UT04|Viewing the year drop down list|1. Click on the drop down list to view|List of years from 1990 to 2019 should be viewable.|Correctness|-|-|
|User Interaction|UT05|Sorting function|1. Click on the table heading once to sort according to it.<br >2.Click on it a second time to display the results in descending order.|Results are displayed according to the canceled percentage in decending order by default. Users is abe to change it by clicking on required table heading.|Correctness<br />Flexibility|-|-|
