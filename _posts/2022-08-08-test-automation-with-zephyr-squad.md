---
categories:
- Automation
- Tools
date: '2022-08-08'
tags:
- test automation
- tools
title: Test Automation with Zephyr Squad
---

Zephyr for Jira (Squad / Scale) is a native application that resides in Jira
and brings test management capabilities to any Jira project. It adds the
following capabilities. For more information on the capabilities of Zephyr and
how it can help agile teams, refer to this
[article](https://skthetester.github.io/zephyr-for-test-management-in-agile/).
Zephyr's Test Automation allows you to import test results from various test
automation frameworks directly into its test execution cycles, which ensures
complete visibility and traceability into the automated test process.

## **How does it help?**

When automation exists, posting the results into Jira can be done in several
ways. The simplest of ways is to automatically post results from the framework
by calling the Jira APIs. But at times, this might not be feasible depending
on the automation tool or framework you use, in these cases, Zephyr's test
automation is very handy. It does two things primarily -

  * If test case already exists, upload test results from automation into Jira
  * If test case doesn't exist, create required tests and update results into Jira

![](/assets/img/posts/zephyr_test-automation-1024x576.png)Zephyr Test Automation

## Frameworks Supported

Zephyr Test Automation supports all modern frameworks which allow you to
export results from it in different formats. Some of them are listed below.
Even if your framework is not listed, you can simply write a custom reporter
to generate results in default JUnit or TestNG XML report formats, they can
very well be imported into Zephyr.

  * Cucumber
  * Eggplant
  * JUnit
  * PyTest (JUnit)
  * Robot (JUnit)
  * Selenium
  * SoapUI
  * TestNG
  * Tricentis Tosca
  * UFT

## How to use Zephyr Test Automation?

It involves two tasks; Creating a task for automation and then executing the
created task. While creating the task, the user can provide a unique name to
identify the task, a brief description of the task, the type of automation
framework, an option to upload the results file, and the location of the tests
in Jira where it needs to be updated such as version, cycle, and folder ids.

Once the task is created, it can be edited, executed, or deleted at any time.
When a new test result is available, the user can edit the automation task and
upload the new test results before executing the task. When the task is
executed, it will be scheduled to run and results will be uploaded into Jira.
Based on the results, the status of the task will be updated as "SUCCESS" or
"FAIL"

![](/assets/img/posts/image-1024x451.png)

* * *

If you found this interesting, you can find more such articles
[here](https://skthetester.github.io/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on X
[@testingchief](https://x.com/testingchief). Thank you!

## Additional References

<https://support.smartbear.com/zephyr-squad-cloud/docs/test-
automation/index.html>