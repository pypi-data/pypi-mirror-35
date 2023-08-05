============
billionfong
============

Introduction
***************
This is a package created by Billy Fong.

The package aims to create 24 Billy, and some mini games for time killing.

billionfong
***************
This is the master class billionfong, with the followings:

:Subclass:   Child, IT Dog, Musician, Narcissist
:Methods:    create(personality = PERSONALITY), play(game = GAME), shout(), love()

Games
***************
There are 2 games created at this moment.

:Bingo:          Guess number between 1 to 100
:Mastermind: Guess 4 numbers between 1-6 with exact order.

Example
***************
::

  import billionfong

  billy = billionfong.create(personality = "narcissist")
  billy.love()
  billy.shout()
  billy.play(game = "mastermind")
