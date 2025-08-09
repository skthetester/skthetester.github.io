---
categories:
- Automation
date: '2020-08-05'
tags:
- test automation
title: The fallacy of Thread.Sleep
---

A simple search in our test automation repository for "Thread.Sleep" returns
over 600 instances in just the baseline regression suite alone. With an
average of 10 seconds per instance, nearly 2 hours of wait time induced by
using Thread.Sleep() alone. By enabling high reuse in the test automation
code, this wait time could inherently be exponentially higher.

While I understand the intent and accept the need for waits in test scripts,
shouldn’t these be replaced with smarter wait handlers such as explicit or
fluent waits? It will definitely reduce the overall execution time.

> **Is it convenience or ignorance driving this behavior among test engineers?
> What are your thoughts?**

![](https://testingchief.com/wp-content/uploads/2020/08/thread-
sleep-1024x896.png)

Inspired from

  * <https://blogs.msmvps.com/peterritchie/2007/04/26/thread-sleep-is-a-sign-of-a-poorly-designed-program/>
  * <https://saucelabs.com/blog/how-to-avoid-threadsleep-in-test-automation>
  * <https://www.seleniumhq.org/docs/04_webdriver_advanced.jsp#explicit-and-implicit-waits>

What do you think? I would love to hear them. You can leave your comments here
or on Twitter [@testingchief](https://twitter.com/testingchief). Read more
about other software testing blogs
[here](https://testingchief.com/category/testing/).