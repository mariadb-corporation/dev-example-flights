# SQA Tasks (Vinuri)
- Explain what activities are we going to do

### 2.0 Standards, Practices, Conventions, and Metrics (Hanna)
This section highlights the standards, practices, conventions, and metrics to be applied to measure the quality of the application.

### Document standards
The IEEE standards, with appropriate modifications, are used as guideline for documentation. The document describes the quality management plan that should be followed by the developers. Document needs to be well-written , spell checked and conforms to the conventions. In this document, HTML  is the preferred format for documentation, which is to be shared in computer readable form.

### Coding Standards
Coding standard gives a uniform appearance to the code even though it is written by different engineers. It helps in improving readability and maintainability of the code. The coding standards are as follows.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phyton and JavaScript naming conventions is used throughout the code. The application contains multiple API projects where its either written using Phyton or JavaScript. Hence, naming conventions are followed respectively. The client, which communicates with the API, is written in JavaScript. The use and creation a class or variable name should be understandable and accurately describes its purpose for easy understanding. Local variables however should be named using camel case which starts with a small letter where as Global variables should start with a capital letter. Throw statements, or also known as throw an exception is used under each function. If an error occurs, JavaScript will stop and generate an error message. This helps simplify the debugging stage. Next, for better understanding and readability of the code, proper indentation is followed. 

### Test Standards
Testing helps discovers bugs or defects before delivering the program to the client. This guarantees the quality of the software. Unit testing, integration testing and system testing are done in this software testing. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Unit testing should be done during the very early stage of development. Each functions, modules or units are isolated, then tested manually to check whether it is working as intended. Bugs identified are fixed before proceeding to the next phase.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After the units have been unit tested, integration testing is performed. In this testing, units are integrated one by one until all the units are integrated. This is to ensure they can be incorporated with each other without error, and validate whether the requirements are implemented correctly or not. The testing is done simultaneously with the development as some units are not available to be test at times. The integration tests ends after all the integration test cases has been executed.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System testing is performed on a complete integrated system. It is carried out on the whole system in the context of either system requirements specifications (SRS) or functional requirements requirements or even both. The testing ends after no critical or priority related bugs are in an open state. If any low or medium priority bugs are in an open state, then it should be implemented with acceptance of customer.

# Metrics (that we have set): (Vinuri)
** additional documentation ** can show the template of documentation u guys follow for test case, peer review, bug report etc

# Problem reporting and corrective actions (Yu Jie)
- Explain what to do when theres a problem ( create bug report, give to leader to determine severity of bug ( low, medium, high) then take action ( Process Audit Report for my group)

# Tools and technologies source code management (Yu Jie)
- What automated framework for testing are we using
- Talk about github

# Testing methodology: (Ka Shing)
- Can describe each step how u guys carry out the testing etc
    1. Unit test
    2. Integration test
    3. System test

    4. UI and UX test

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;UI testing is important to make the usability of application easier for users. UI testing is done through the web server, where the visual elements available are manipulated. For testing mobile compatibility, the application is access through the available search engine on mobile. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To determine the portability of the application, the application needs to be  accessed through different browsers and operating system. All the available widgets such as dropdown bars and buttons need to be tested to check whether it is working as intended and either it responds to user events such as mouse clicks. Layout of the application should be tested to determine whether the GUI elements aligns and responds accordingly to the resize of the web appplication. Position of GUI elements also need to be tested by accessing the application through different screen resolutions. Therefore, consistency of user interface displayed can be determine regardless of the size of monitor.  By accessing the application through different screen resolutions, the readibility of font used can be tested. This is to determine whether the font type and size used is clear and easy to read. For the purpose of testing the display of error message, leave the origin and destination empty.This error message should be informative so user will be informed of the error made. 

# Records – collection, maintenance and retention (Ka Shing) 
- The following documents will be collected, maintained, and retained in the appropriate software configuration management repository:
    - Software Quality Assurance Plan
    - Test Case Documentation
- In addition, the following will be maintained as quality records:
    - Test results
