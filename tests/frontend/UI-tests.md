## UI/UX tests:

<br /> 

| Scenario Group | Test ID | Decription | Test Steps | Expected Output | Factors | Metrics | Remarks |
| :-             | :-      | :-         | :-         | :-              | :-      | :-      | :-      |
|Mobile Compatibility|UI01|Check the compatibility of the user inteface though a mobile|1. Open the web server using a mobile.|The components of the website does not adjust according to the reduced screen size.<br />The user has to scroll horizaontally to view and input information.|Portability|-|-|
|User Experience|UI02|Check the web interface using different browsers|1. Open the interface suing Google chrome <br/> 2. Open the inteface using Safari.  |The user interface appears consistent on different web browsers.|Portability|-|-|
|User Experience|UI03|Check the web interface in different operating systems.|1. Open the interface in a windows OS.<br />2. Open the interface in a Mac OS.|The user interface appears consistent on different Operating Systems.|Portability|-|-|
|User Experience|UI04 |Alter the size of the window and check the interface. |1. Reduce the window size and check if the interface components adjusts accordingly<br />2. Increase the window size and check if the interface adjust accordingly.|The components do not adjust to the decreasing window size.<br />2. The componently appear perfectly when the window is at its maximum size.|Portability.|-|-|
|User Interaction|UI05|Check the positioning of GUI elements in different screen resolutions.|1. Open the interface in a 13 inch screen.<br />2. Open the interface on a 15 inch screen.|The interface should appear consistent regardless of the size of the monitor.|Correctness|-|-|
|User Interaction|UI06|Check if the font used is readable.|1. Open the interface in a different screens.<br />2. Open the interface on different brightness settings.|The text should be clear and easy to read.|Correctness|-|-|
|User Interaction|UI07|Check if the alignment of the text is proper.|1.Input Los Angeles and chicago as origin and detination airport.<br />2.Input American Airlines as Airline.<br />3. Input 2014 to 2019 as duration.<br />4. Click Search.| The text in the resulting putput tale should be aligned properly according to each heading..|Correctness|-|-|
|User Interaction|UI08|Check if error messeges are displayed correctly.|1. Click the search button without any input for origin airport.|A clear error message is displayed letting the user know not leave the field as null.|Correctness|-|-|
|User Interaction|UI09|Input wrong data.|1. Enter Los Angeles International airport for both origin and destination airports.|There will be no data displayed in the output table.|Correctness|-|-|
|User Interaction|UI10|Input null data.|1. Click the search button without any input.| An error messege will be displayed letting the user know not to leave the field as null.|Correctness|-|-|
