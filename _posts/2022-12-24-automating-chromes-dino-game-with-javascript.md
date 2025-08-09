---
categories:
- Automation
date: '2022-12-24'
tags:
- test automation
title: Automating Chrome's Dino Game with JavaScript
---

I have been holding off starting with JavaScript for a while. Even when given
a chance a few years ago, I chose Python as it might give me an edge in data
analytics. Recently, I took the [Test Automation University
course](https://testautomationu.applitools.com/automating-in-the-browser-
using-javascript/) by Alan Richardson AKA Evil Tester. I was intrigued by how
he was able to automate a game easily with JavaScript and I gave it a try with
Chrome's Dino game.

![Dino Game](https://testingchief.com/wp-content/uploads/2022/12/image-3.png)

## The Lonely T-Rex Chrome Dino Game

The Chrome Dino game was developed by Google back in 2014 and built into the
Chrome browser. Whenever the user attempts to navigate any webpage on Google
Chrome while offline, the browser indicates that they are not connected to the
internet and displays the pixelated Tyrannosaurus rex game. The game is very
simple! Users should avoid obstacles that come in T-Rex's path by using space
or arrow keys.

Users can also play this game by navigating to [chrome://dino](//dino). Since
the game completely runs on the browser, with a little knowledge of
JavaScript, you can easily automate the user's actions and play the game
autonomously.

    
    
    **NOTE : This article doesn't encourage hacking a game in any way. The main objective of this article is to show the capability of JavaScript and kindle your interest to learn JavaScript**. 

## Automating the Game

Automating this game was much easier than I thought and it requires creating a
JavaScript function with the following simple actions.

  * Create a new instance for the T-Rex Runner
  * Identify if there is an obstacle in the T-Rex runner's horizon
  * If an obstacle is found, identify whether its a CACTUS or PTERODACTYL
  * Identify the location (X, Y) of the obstacle (required for Pterodactyls)
  * Based on obstacle type and Y pos, add a condition to Jump or Duck
  * Finally, call the function so that it runs on the browser while the game is played

![Chrome Dina Code Snippet](https://testingchief.com/wp-
content/uploads/2022/12/image-4-1024x412.png)

* * *

https://www.youtube.com/watch?v=mH8OGcPTXCg

## Additional References:

  * <https://testautomationu.applitools.com/automating-in-the-browser-using-javascript/>
  * <https://dev.to/official_fire/making-the-chrome-dino-game-play-itself-using-javascript-2j8n>

* * *

If you found this interesting, you can find more such articles
[here](https://testingchief.com/blog/) on quality assurance, test automation,
tools, and processes. Don’t forget to leave your comments here or on Twitter
[@testingchief](https://twitter.com/testingchief). Thank you!