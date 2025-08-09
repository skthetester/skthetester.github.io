---
categories:
- Automation
- Tools
date: '2021-07-09'
tags:
- test automation
title: What's changed in your monthly utility bills?
---

Have you ever wondered what's in your monthly utility bills or statements that
you receive from the financial institutions? How do you check what has changed
(visually test) since the last bill? Did they add new fees, taxes or is there
a change in the terms and conditions or even fine print? Most of us would
simply look at the total cost that needs to be paid, and if nothing out of the
ordinary will not even bother to open the statements. What if there is an easy
way to identify the change? I came across one such way and thought of sharing
it with you.

I found answers to all the above questions in
[Applitools](https://applitools.com/). Earlier this week, I was taking a free
course provided by [TestAutomationU](https://testautomationu.applitools.com/)
on [Test Automation for Accessibility by Marie
Drake](https://testautomationu.applitools.com/accessibility-testing-tutorial/)
and got intrigued by this simple to use but a very effective visual testing
tool. On subsequent learning, I could see endless potential and use cases
where we could use this tool to automate mundane visual tests, not just for
work but at home as well. Checking your monthly utility bills is one such
example.

## Here's how I did it

  1. [Sign up](https://auth.applitools.com/users/register) for Applitools and get your free account plus API key
  2. Download their [ImageTester](https://github.com/applitools/ImageTester/releases) utility ([Download](https://testingchief.com/wp-content/uploads/2023/07/ImageTester_3.5.1.zip))
  3. Run a single line in the command prompt to create a base with your last month's statement
  4. Run the same command every month with your new statement and see what has changed

> _java -jar ImageTester.jar -k [api-key] -f [file-path]_

## Example (Enbridge Gas Bill)

![Visual Test Results](https://testingchief.com/wp-
content/uploads/2021/07/image-2.png)Test Failed as differences found.

Tests failed (shown above) as there were differences between my statements
other than the obvious ones that would change like usage and cost. Applitools
has a cool feature (my favorite) that lets you select regions that should be
ignored so that only the unknown differences are highlighted.

Looking closely at the result, there are two differences. In my bill, last
month it was an actual meter reading and this month it was only an estimated
value. I didn't know this was the case until I did this comparison. This also
explains why I was billed lesser than last month.

![](https://testingchief.com/wp-
content/uploads/2021/07/image-7-1024x463.png)Actual vs Estimated Cost as a
Difference. Shows Ignored regions configured.

There was also a subtle change in the information section.

![](https://testingchief.com/wp-
content/uploads/2021/07/image-4-1024x427.png)Subtle change in the Information
section that usually goes unnoticed.

## So, how does it help?

  * Be informed
  * Use the tool for quickly comparing multi-page statements
  * Efficiently use features like "ignore" region for better results

* * *

If you found this interesting, you can find more such articles
[here](https://testingchief.com/blog/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments. Thank you!