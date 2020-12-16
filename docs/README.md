# SQA Tasks (Vinuri)
The purpose of this plan is to specify how Software Quality Assuarance will be performed throughout the system. This plan will describe the SQA activities namely the process, methods, standards to be performed and the techniques used to perform those tasks. The plan provides the necessary framework to ensure a consistent approach to software quality assurance throughout the project life cycle. 

Scope: The scope of this plan applies to all stages of the system testing. It defines the approach that will be used to assess the software to provide insight to the functionality and quality. Adherence to the plan will continue throughout as needed, based on the results of the tests.

Objective: The SQA teams Objective is to ensure that the product does not deviate from the software specification. The team will analyse the quality of the system at any stage for functionality enhancement and error detecton.

The purpose of this plan:
- Identify the resposnsiblities of the project team.
- List the SQA standards, metrics and process.
- Defines testing and audits and how they will be carried out.

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
The following are the planned metrics that will be collected, reported, and maintained in the area of software quality assurance:
- Adherence to schedule: Scedules and milestones will be tracked inorder to identify the prcentage of completion of the project.
- Number of software defects found: This reflects the quality of the code. The goal is to produce code that is free of bugs. The  errors and the number of errors found during each testing phase will be recorded.
- Software defect turnaround: This calculates the time and resources it takes to correct the identified defects. 
- Size of the code (LOC): The size of the code and lines of codeused in each indivudual element will be used to estimate required testing effort and overall software productivity.
- Programming time(persons-months): Used to estimate testing effort required. 
- Storage Capacity: The storage capacity of the whole system will be used to measure the ease of implementation and productivity.
- Test case statuse: The passed/failed percentage will be recorded during each testing phase.

# Problem reporting and corrective actions (Yu Jie)
All problems will be reported after each software review or testing is carried out. The leader of the project will review the bug report and determine the severity of the bug (low, medium, high) before passing it to the developer team that is responsible for fixing the bugs found. The developer team will apply the changes to the software according to the severity of bug while making sure there is no collision with any other part of the software. The outcome will be reviewed again to ensure all the bugs are fixed. 

# Tools and technologies source code management (Yu Jie)
Git is used as the version control system to manage the documents and source code of the project. It is installed and maintained on the local system of each team member's devices and provides a self-contained record of the ongoing programming versions. Github is also used as an assist together with Git to allow team collaboration through cloud. GitHub is a code hosting platform that provides Git repository hosting service. It allows the team members to share their codes or documents to each other through remote repository and carry out version control at the same time.   

# Testing methodology: (Ka Shing)
The testing team follows closely alongside every step of the development process. To ensure that all requirements are met and bugs are fixed as soon as possible, several testing methodologies are employed. The testing methodologies that were employed include:
1. Unit testing
2. Integration testing
3. System testing
4. UI testing

## Unit testing
Unit testing is a software testing process which focuses on inidvidual units of source code, such as a functions in a program.  Unit tests are usually written once and reused so that the tests can be automated after a change in the source code. Our team will take a semi-automated approach to unit testing. The purpose of unit testing is to ensure that each unit performs as intended and helps to speed up the debugging process during and after development. Unit tests are white box tests as the test designers have to understand the inputs and outputs of the unit to test it effectively. There are a few guidelines set by our team for unit testing:

1. Unit tests should cover both right and wrong inputs
2. Unit tests should test for the boundary value of a unit
3. Each unit test should be fast and small
4. Each unit test should only cover one unit
5. Results should be documented and bugs should be reported

## Integration testing
Integration testing should take place after unit testing. It tests the integration of individual software modules to check if they work together when combined. The main purpose of integration testing is to uncover defects present between modules when they are integrated. Hence, integration test is a white box test since testers are required to understand all functions of the code base. The team will take a semi-automated approach in this phase of testing. The follow are guidelines set by our team for integration testing:
1. The team shall use a bottom-up approach to integration testing
2. Unit testing shall be done before integration testing
3. Integration testing should only test for the integration between modules rather than the functionality of the modules.

## System testing
System testing is a black-box testing technique and it does not require internal knowledge of the code. It is done after the integration testing and it mainly focus on testing the functionality and features of the system as a whole. Inputs are provided to the system and the outputs are verified according to the expectations stated in the test cases. Test cases is created at the beginning to determine all the aspects to be covered in the system testing. Each test cases are written based on the real-time usage of the software. After the execution of all the test cases, any bugs found are documented in the bug report. 

## UI testing
UI testing is important to test whether the application performs as expected with respect to user interface behaviour. UI testing is done through the web server, where the visual elements available are manipulated. For testing mobile compatibility, the application is access through the available search engine on mobile. To determine the portability of the application, the application needs to be  accessed through different browsers and operating system. All the available widgets such as dropdown bars and buttons need to be tested to check whether it is working as intended and either it responds to user events such as mouse clicks. Layout of the application should be tested to determine whether the GUI elements aligns and responds accordingly to the resize of the web appplication. Position of GUI elements also need to be tested by accessing the application through different screen resolutions. Therefore, consistency of user interface displayed can be determine regardless of the size of monitor.  By accessing the application through different screen resolutions, the readibility of font used can be tested. This is to determine whether the font type and size used is clear and easy to read. For the purpose of testing the display of error message, leave the origin and destination empty.This error message should be informative so user will be informed of the error made. Followings are guidelines set by our team for UI testing:
1. Check screen validations
2. Check the usability conditions
3. Verify navigations
4. Verify data integrity
5. Verify the input fields and formats
 
# Records – collection, maintenance and retention (Ka Shing)
Documentation related to SQA is kept for future reference and to be shared with stakeholders. The Software Quality Assurance plan as well as the Test Case Documentation will be collected, maintained, and retained in our Github repository. In addition, the results of the tests will be maintained as quality records for future reference.
