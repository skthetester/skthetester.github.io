---
categories:
- Automation
- Tools
date: '2022-08-13'
tags:
- test automation
- tools
title: Cucumber Framework - Test Automation with Zephyr
---

Zephyr for Jira (Squad / Scale) is a native application that resides in Jira
and brings test management capabilities to any Jira project. It adds the
following capabilities. For more information on the capabilities of Zephyr and
how it can help agile teams, refer to this
[article](https://testingchief.com/zephyr-for-test-management-in-agile/).
Zephyr's Test Automation allows you to import test results from various test
automation frameworks directly into its test execution cycles, which ensures
complete visibility and traceability into the automated test process.  Refer
to my previous article [here](https://testingchief.com/test-automation-with-
zephyr-squad/) to understand more about how Zephyr's test automation works.

On the other hand, Cucumber is an open-source testing tool that enables you to
write acceptance test cases and automate them easily. It is embraced by test
automation engineers worldwide as it ties up the individual test steps with
corresponding glue code i.e. step definitions. I will be writing more about
the cucumber framework shortly, but in the meantime, you can read more about
it [here](https://cucumber.io/tools/cucumber-open/).

![](https://testingchief.com/wp-content/uploads/2022/08/cucumber_zephyr-test-
automation-1024x576.png)Cucumber Framework - Zephyr Test Automation

## What do you need?

You would need the test results in one of the supported formats i.e. XML.
Luckily, the Cucumber framework supports generating test reports in multiple
formats such as HTML, JSON, and JUnit XML. Here is an example of how to
generate the required XML report.

    
    
    package runners;
    
    import org.junit.runner.RunWith;
    import cucumber.api.CucumberOptions;
    import cucumber.api.junit.Cucumber;
    
    @Listeners(org.tchief.TestListeners.class)
    @CucumberOptions(
    		features = "src/test/resources/functionalTests",
    		glue= {"org.tchief.stepDefinitions"},
    		plugin = { "pretty", "json:target/reports/Cucumber.json",
    			**"junit:target/reports/Cucumber.xml"** ,
    			"html:target/reports"},
    		monochrome = true
    		)
     
    public class TestRunner {
       //code here...
    }

## How to post automation results?

Follow these simple steps to upload the test automation results from a
Cucumber-based automation framework.

  * Create an automation task in Jira with type as "Cucumber" or simply "JUnit". 
  * In the upload file field, choose the XML report created
  * Enter the test details such as Version, Cycle and Folder IDs
  * Save the automation task
  * Execute the automation task when required
  * ** _Things to remember -_**
    * Make sure your tests have a label "ZFJ_Automation". Zephyr by default searches for the test cases in Jira project with the exact test name found in the test report and only those with a label ZFJ_Automation. If found an exact single match, it updates the test case result. If not found or more than 1 match found, then it creates a new test case and updates the result.
    * If new results need to be uploaded, simply edit the task and choose the new report file to be updated.

* * *

If you found this interesting, you can find more such articles
[here](https://testingchief.com/blog/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on Twitter
[@testingchief](https://twitter.com/testingchief). Thank you!

## Additional References

  * <https://support.smartbear.com/zephyr-squad-cloud/docs/test-automation/index.html>
  * <https://testingchief.com/zephyr-for-test-management-in-agile/>
  * <https://testingchief.com/test-automation-with-zephyr-squad/>