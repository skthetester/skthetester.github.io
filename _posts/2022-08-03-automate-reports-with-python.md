---
categories:
- Automation
date: '2022-08-03'
tags:
- test automation
title: Automate Reports with Python
---

In the new series of automating boring stuff, I will tell you how I automated
our team's weekly status reports with Python.

## The Boring stuff?

While they are important, generating the daily, weekly, and monthly status are
really daunting and boring. If your ecosystem consists of visualization tools
like Power BI or Tableau and is capable of generating required reports
automatically, you are in bliss. Not everyone is that lucky, in our case I had
to rely on my team to provide the data manually. Without the help of such
tools, compiling such a report, generating insights, making charts, and
sending them is monotonous and boring to do every day.

![](https://testingchief.com/wp-
content/uploads/2022/08/automate_reports_python-1024x576.png)

## Solution

As always, 1st question I asked was, why not automate it? What if I can take
these numbers, compare them against previous months' data, generate trends for
different metrics, put them into the desired format (.PPTX, .docx, etc), and
send them out to recipients - All with a click of a button. amazing isn't it?

With the help of Python's pandas, matplotlib, and pptx libraries, and a few
lines of code, reports in the required format can be generated and added to a
Microsoft Powerpoint template (.pptx)

### Pre-requisites:

  * A Microsoft Powerpoint Template (.pptx) with required slides, headers, and formatting. 
  * Required data for generating reports. It can be readily available in the form of a flat file, CSV, Excel, or can be scraped from daily status reports in emails or from Confluence pages. 

### Procedural Steps:

  1. Import the required libraries - pandas, matplotlib, numpy, os, datetime, pptx, plotly
  2. Ensure that the pre-requisites are completed, data and template to update are ready
  3. Set the constants like data path, dates to calculate, template file to update, etc.
  4. Use panda to read input data
  5. Query, group, sort, and order data as required. Some might be straightforward like the "number of new tests automated" this week, whereas others like "effort saved with automation" this week need multiple values to be computed to get the final value. 
  6. Plot figure using matplotlib; Format axis, size, and position of the charts
  7. Add text over charts to add more info
  8. Open the Powerpoint template, make a copy of it and rename the file
  9. Add computed text and generated graphics to the newly created file
  10. Save report

Review the content, add/update as required, or configure to send the report to
stakeholders automatically. That's pretty much it, code once and run whenever
required. Replicate the same for weekly, monthly, or even quarterly/yearly
reports by simply changing the timeline for which the report is generated.

_*** NOTE *** I will be adding the GitHub repository with a sample working
code shortly for anyone looking to get a jump start with their report
automation ***_

* * *

If you found this interesting, you can find more such articles
[here](https://testingchief.com/blog/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on Twitter
[@testingchief](https://twitter.com/testingchief). Thank you!