---
categories:
- Automation
date: '2020-08-29'
tags:
- test automation
- testing
title: How much does your test automation code smell?
---

> A _**code smell is any characteristic in the source code of a program that
> violates fundamental design principles and negatively impacts design
> quality**_

Usually, code smell indicates that something might be wrong, a problem that
doesn’t necessarily pose any noteworthy challenge now but has the potential to
grow into a deeper and much more expensive problem to fix in the future.
Irrespective of the programming language used and the experience of the
development team, they might accumulate additional work due to non-optimal
design decisions. Just like financial debt, if the team doesn’t pay off this
accumulated debt at regular intervals, it becomes so huge and difficult to
manage the product and must be abandoned at some point.

In the current fast-paced Agile and DevOps environment, the boundaries between
development and QA are quickly blurring and the same sets of standards are
expected from all members of the team including the QA. If you are an
automation engineer and just focusing on getting your test automated but not
on cleaner, simpler, and easily maintainable code, then it’s high time to
start doing it. You don’t want your unmaintained test automation code to be
the reason for the build to fail in the CI-CD pipeline.

Some of the common problems include - No comments to explain what the code
will do, dead code which is never run or redundant code introduced rather than
reusing existing code. Keeping other things constant, long methods and classes
reduce the readability of the test script. Inefficient waits, inappropriate
locator strategy and not having correct assertions are all issues that are
very specific to test automation code that programmers might not have to deal
with in their code.

There are several ways in which the automation engineers can enable static
code analysis for their test automation code. **Sonarlint** , an IDE extension
that helps engineers to detect and fix issues in code as they do the test
automation scripting is the easiest of ways for someone looking to start this
journey. In addition to removing the code smell, it will also help the
automation engineers become better at coding and make the test suite more
efficient. Once the QA team is familiar with the static code analysis process,
code refactoring, and reducing technical debt, they can start using
**SonarQube**. It is an automatic code review tool to detect bugs,
vulnerabilities, code smells, and % duplicate code in the code repository. It
can be easily integrated with the existing workflows to enable continuous code
inspection across all the Bitbucket branches and pull requests.

> As the code quality improves, it will definitely bring down the total cost
> of maintaining your automation test suite in the long run.

Watch this video for more information.

https://youtu.be/Gp1DAdy-XXA

  
Read more about other software testing blogs
[here](https://testingchief.com/category/testing/).  
What do you think about code quality and code smell in test automation
scripts? Leave your comments here or on Twitter
[@testingchief](https://twitter.com/testingchief).

  
**Additional resources:**

  * <https://www.se.rit.edu/~tabeec/RIT_441/Resources_files/How%20To%20Write%20Unmaintainable%20Code.pdf>
  * <https://www.refactoring.com/>
  * <http://c2.com/xp/CodeSmell.html>
  * <http://angiejones.tech/test-automation-code-smells/>
  * <https://club.ministryoftesting.com/t/how-does-your-code-smell/16768>
  * <https://www.sealights.io/code-quality/the-problem-of-code-smell-and-secrets-to-effective-refactoring/>