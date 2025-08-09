---
categories:
- Continuous Testing
date: '2020-08-08'
tags:
- test automation
- testing
title: Demystify Continuous Testing
---

In the previous article **[“There’s more to Continuous Testing than Automating
your tests!”](https://testingchief.com/theres-more-to-continuous-testing-than-
automating-your-tests/)** , I suggested what else test teams should be looking
at in addition to automating their functional tests using their vanilla test
automation framework to be successful at continuous testing. While that’s the
ideal end-state that every team would like to be, I got several questions from
automation engineers on where and how do they can start this journey. I will
try to demystify the process in this article by giving a brief checklist of
critical things that teams can check and incorporate into your test automation
for a jump start.

![continuous testing steps](https://testingchief.com/wp-
content/uploads/2020/08/continuous-testing-steps.png) 01| Evaluate your test
suites along with your engineering and product teams  
to ensure that they **cover all critical business areas, risks, and user
experience**.  
It is very important to get all the stakeholders in sync.  
---|---  
02| Stay on top of the progressive automation of new features added every
sprint,  
keep the **automation and technical debt as low as possible** (<5%) at any
time.  
03| Introduce **Automated test data management** using either static or
dynamic  
methods to identify, generate, refresh, and manage data.  
04| If all your tests are at front-end UI, then its time to re-evaluate your
test strategy  
to **shift left your testing** to include unit, component, and integration
tests as well.  
05| Commit related changes often to a central repository such as Git,
**measure, and**  
**improve code quality** using static code analysis tools like SonarQube.  
06| Enable **uninterrupted test execution** by removing manual interventions,  
ability to take run-time parameters to run tests in any known environment.  
07| Optimize the automated scripts to **reduce the total execution time** (<1
Hr).  
Enable concurrent test runs wherever possible.  
08| **Remove security vulnerabilities** by scanning every piece of code
including tools,  
framework, dependencies, and test automation code using tools like HP Fortify.  
09| If running on a pre-defined schedule, **run tests at least daily or
multiple times**  
**per day**. If connected to the CI-CD pipeline, run the tests for every build  
and deployment.  
10| Introduce **automation in all possible avenues** starting from test case
creation,  
test script generation and script maintenance, bug analysis, and reporting.  
  
You can leave your comments here or on X
[@testingchief](https://x.com/testingchief). Read more about other
software testing blogs [here](https://skthetester.github.io/).