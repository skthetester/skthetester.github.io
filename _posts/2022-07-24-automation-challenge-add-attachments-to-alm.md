---
categories:
- Automation
date: '2022-07-24'
tags:
- test automation
- tools
title: 'Add attachments to ALM # Automation Challenge'
---

Micro Focus ALM (previously HP ALM) has been around for a long time, and
attaching an artifact to an entity (test, test run, or defect) is not new. But
my automation team had difficulties recently in attaching the word document
reports generated from test automation to ALM. They weren't able to find
clearly documented steps on how to do this., Here is how I did it.

### **Background**

Some of the manual QA teams that I work with still use Micro Focus ALM for
their test management. Hence, the automated test results are also posted to
ALM so they all remain within the same tool and reports can be generated. The
ALM version used is also outdated, still at 12.5x and it's high time that it
is upgraded to Octane.

The custom in-house-built test automation framework (Selenium/Java) creates an
optional .docx report with test steps and screenshots. For audit purposes, the
request came in to attach these documents to automated test runs along with
their PASS/FAIL status.

![](https://testingchief.com/wp-
content/uploads/2022/08/add_attachments-1024x576.png)add attachments

### Solution

ALM API is well-documented and widely used but some of the nuances need to be
understood and tried out to effectively use it. Most of the documentation and
suggestions included were to use multipart/form-data, but sending a .docx with
text and images in binary form had its own problems to handle. As a result, I
had to switch to octet-stream. Once it is done, it is pretty straightforward.

  * The framework was using Unirest for all API interactions. So it simplified the request.
  * Request type should be POST
  * The test result should have already been posted, and a test run created
  * Endpoint should include domain, project, and required test run id 
  * Headers set for Content type, Accept and Slug
  * Slug should be the display name of the file
  * Request body should contain the file contents. It should be a stream to ensure that the entire file is uploaded

    
    
    HttpResponse<string> responseXML = Unirest.post(ALM_ENDPOINT + "/rest/domains/" + DOMAIN_NAME + "/projects/" + PROJECT_NAME + "/runs/" + testRunId + "/attachments")
    .header("Content-Type", "application/octet-stream")
    .header("Accept", "application/xml")
    .header("Slug", reportFile.getName())
    .body(Files.newInputStream(reportFile.getPath()))
    .asString();

### Additional References

<https://admhelp.microfocus.com/alm/api_refs/REST/Content/REST_API/attachments.htm>

<https://community.microfocus.com/adtd/sws-qc/f/itrc-895/403766/alm-rest-api-
add-attachment>

* * *

If you found this interesting, you can find more such articles
[here](https://testingchief.com/blog/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on Twitter
[@testingchief](https://twitter.com/testingchief). Thank you!