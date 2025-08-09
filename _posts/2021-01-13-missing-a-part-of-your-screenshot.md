---
categories:
- Automation
date: '2021-01-13'
tags:
- test automation
title: Are you missing a part of your screenshot from the test script?
---

If you are an automation engineer, taking screenshots and managing them might
play a major role in your framework. Especially if you are performing visual
tests and comparing UI with tools like Applitools, screenshots become even
more important. But, are you missing a part of your screenshot from the test
script and wondering what could have caused this?

![missing a part of screenshot](./assets/img/posts/image-9-1024x605.png)Where does the rest of the screen
go?

It is one of the common issues that engineers face when they change the
Windows scaling. By default, based on the screen resolution supported Windows
10 recommends setting the scaling to 125% or even 150%. But when you don't
handle the viewport settings to accommodate this change in your test code, you
will end up with a partial screenshot.

## How to fix this?

It is a simple fix. Simply add the required scaling that matches your system
settings. You can find it either from the Windows display settings or by
running _window.devicePixelRatio;_ in the browser console.

    
    
    //Before Fix
    Screenshot screenshot = new AShot()
    .shootingStrategy(ShootingStrategies.viewportPasting(1000))
    .takeScreenshot(driver);

* * *

![missing part of screenshot](./assets/img/posts/image-10-1024x605.png)Partial Screenshot + Missing
portion

    
    
    //After Fix - Includes scaling of 125%
    Screenshot screenshot = new AShot()
    .shootingStrategy(ShootingStrategies.viewportPasting(**ShootingStrategies.scaling(1.25f)** , 1000))
    .takeScreenshot(driver);

![Full screenshot login form](./assets/img/posts/image-11-1024x605.png)Full Screenshot

Viola! There's your full screenshot.

* * *

You can leave your comments here or on X
[@testingchief](https://x.com/testingchief). If you are interested in
similar articles on software testing or test automation, you can find them
[here](https://skthetester.github.io/).