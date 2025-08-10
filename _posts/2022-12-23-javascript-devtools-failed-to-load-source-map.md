---
categories:
- Tools
date: '2022-12-23'
tags:
- tools
title: DevTools failed to load source map?
---

If you are just starting with Javascript and looking at the browser console
logs, you could very well see this naive error "DevTools failed to load source
map: Could not load content for chrome-extension://xxxxxx.js.map: System
error: xxx". This is a very common error and is most often caused by the
Adblock extension installed in your browser.

![Console Error](/assets/img/posts/image.png)

There are two ways to remove these errors.

1\. Simply disable the extensions that are causing these errors. Start with
the Adblock extension and if it doesn't help try disabling the other browser
extensions one by one.

2\. Update the browser DevTools settings to disable JS & CSS source maps. In
order to do this, navigate to developer tools, then Settings. Under
Preferences > Sources, uncheck "Enable JavaScript source maps" and "Enable CSS
source maps".

![DevTools Settings](/assets/img/posts/image-1.png)

Now, if you reload the page in your browser, the errors will be gone. :)

![Clean Console](/assets/img/posts/image-2.png)

* * *

If you found this interesting, you can find more such articles
[here](https://skthetester.github.io/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on X
[@testingchief](https://x.com/testingchief). Thank you!