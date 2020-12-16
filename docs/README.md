# SQA Tasks (Vinuri)
- Explain what activities are we going to do

# Standards, practice conventions and metrics (Hanna)
## Document standards:
## Coding standards:
## Test Standards:

# Metrics (that we have set): (Vinuri)
** additional documentation ** can show the template of documentation u guys follow for test case, peer review, bug report etc

# Problem reporting and corrective actions (Yu Jie)
All problems will be reported after each software review or testing is carried out. The leader of the project will review the bug report and determine the severity of the bug (low, medium, high) before passing it to the developer team that is responsible for fixing the bugs found. The developer team will apply the changes to the software according to the severity of bug while making sure there is no collision with any other part of the software. The outcome will be reviewed again to ensure all the bugs are fixed. 

# Tools and technologies source code management (Yu Jie)
Git is used as the version control system to manage the documents and source code of the project. It is installed and maintained on the local system of each team member's devices and provides a self-contained record of the ongoing programming versions. Github is also used as an assist together with Git to allow team collaboration through cloud. GitHub is a code hosting platform that provides Git repository hosting service. It allows the team members to share their codes or documents to each other through remote repository and carry out version control at the same time.   

# Testing methodology: (Ka Shing)

The testing team follows closely alongside every step of the development process. To ensure that all requirements are met and bugs are fixed as soon as possible, several testing methodologies are employed. The testing methodologies that were employed include:
1. Unit testing
2. Integration testing
3. System testing
4. UI/UX testing

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


# Records – collection, maintenance and retention (Ka Shing)
Documentation related to SQA is kept for future reference and to be shared with stakeholders. The Software Quality Assurance plan as well as the Test Case Documentation will be collected, maintained, and retained in our Github repository. In addition, the results of the tests will be maintained as quality records for future reference.