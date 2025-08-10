---
categories:
- Continuous Testing
date: '2020-08-01'
tags:
- test automation
- testing
title: There's more to Continuous Testing than Automating your Tests!
---

With the increasing demand for all organizations to deliver faster to the
market in order to stay competitive, companies irrespective of the domain that
they operate on started embracing DevOps to the fullest. While faster delivery
is important, so is to maintain the quality of the software released to the
market. “Continuous Testing” is the need of the hour to receive actionable
feedback as quickly as possible using automated tests. It also helps the
product team to monitor, increase quality, and reliability over time.

**Continuous Testing is the process of executing _automated tests_ as part of
the software delivery pipeline to obtain _actionable feedback on the business
risks_ associated with a software release candidate _as rapidly as possible_**

Test early, often, and everywhere is the common theme for continuous testing.
It might seem like a simple procedure to just keep running the automated tests
that the team already has as and when required, but it is not that simple to
implement as it might sound.

DevOps and/or Continuous Testing is not a one-time change, it’s more of a
Journey. If the project team has already automated their test cases, it is a
good start but that’s not just enough to be CT ready.

![](/assets/img/posts/continuous-testing-fact.png)

There are several key things that test teams must ask and prepare themselves
in order to pursue their journey of continuous testing. Firstly, has the team
identified and defined different test suites for validating the right business
risks and features? A single generic test suite will not suffice to access the
associated risks at every stage of the DevOps pipeline. Based on what is being
validated, a new feature, user experience, or regression, an appropriate test
suite should be made available.

Secondly, are all these different test suites automated fully? Though there is
still a need for manual exploratory testing, the tests that are incorporated
into the DevOps pipeline should be 100% automated and there shouldn’t be any
manual intervention required which would become a bottleneck for the whole
continuous delivery process. This is also true for test data management. There
should be an automated data identification, generation, and management process
so that the data used is always the latest and doesn’t become stale. Next, is
your automated test suite robust enough to run in any environment, at any time
and every time. Nowadays, it is even common to test even in the production
environment and the automated suite shouldn’t have any constraints on where,
and how it can run including the associated test data. The test runs should
not impact the user experience in any way.

![](/assets/img/posts/continuous-testing-questions.png)

There are several key things that test teams must ask and prepare themselves
in order to pursue their journey of continuous testing. Firstly, has the team
identified and defined different test suites for validating the right business
risks and features? A single generic test suite will not suffice to access the
associated risks at every stage of the DevOps pipeline. Based on what is being
validated, a new feature, user experience, or regression, an appropriate test
suite should be made available.

Secondly, are all these different test suites automated fully? Though there is
still a need for manual exploratory testing, the tests that are incorporated
into the DevOps pipeline should be 100% automated and there shouldn’t be any
manual intervention required which would become a bottleneck for the whole
continuous delivery process. This is also true for test data management. There
should be an automated data identification, generation, and management process
so that the data used is always the latest and doesn’t become stale. Next, is
your automated test suite robust enough to run in any environment, at any time
and every time. Nowadays, it is even common to test even in the production
environment and the automated suite shouldn’t have any constraints on where,
and how it can run including the associated test data. The test runs should
not impact the user experience in any way.

Finally, how quickly can you get the feedback from your automated runs? There
is no point in waiting for days or even several hours to find the stability
and reliability of the build. The mantra here is to access the business risks
as quickly as possible and provide actionable feedback on the failures. If
there is a need for multi-layered testing, it can be orchestrated in such a
way that the sanity and smoke test run first, followed by functional and then
the regression or end-to-end tests, and passing along the feedback as when
each level of testing completes.

**So, what does it take to transition from the traditional methods to
continuous testing?**

It all starts with the change in the mindset. Adjusting to the cultural shift
from an outdated process of developing software, handing over it to the QA
team for testing, finding and reporting bugs, fixing them, and repeating the
whole process over and over again to the quicker and faster delivery of CI-CD-
CT. Be open to rethinking the test strategy from testing the application just
from the front-end GUI to individually validate each component that is part of
the system. Shift-left the testing and add more of unit and component level
tests at the same time, continue the emphasis on the user experience. When it
comes to automation, teams should also look beyond their test cases, and
introduce automation at all possible avenues. Some of the examples include
automatic test creation from business requirements using models, codeless test
scripting framework, self-healing capabilities, auto-bug analysis, and
reporting.

In order to achieve most of the things discussed above, the testers must
understand the broader picture of the application landscape to evaluate the
business risks in the release candidate. This knowledge would help the team to
choose the right set of tools, techniques, and processes to achieve maximum
efficiency and effectiveness.

**If you are already automating your tests, you have a head-start. By
embracing DevOps, expanding your test focus, stabilizing, and optimizing your
test suites, you can succeed in Continuous Testing!**