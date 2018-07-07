# ising2d
This code was developed as part of the Simon's Institute Summer School, 2018.

The overall goal of this code is to determine the ground state of the 2D Ising model, 
but the goal of the exercise is to practice the following:
-Pair Programming
-Test Driven Development
-Version Control (via git/github)
-Continuous Integration (via travis-ci)
-Documentation (via Doxygen)

## Continuous Integration
Travis provides the following definition of continuous integration: "Continuous Integration is the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments. This is where Travis CI comes in."
In essence, the primary functionality of Travis appears to be to:
1. Clone your github repo into a virtual environment
2. Builds and tests your code
3. Tells you whether the builds passed or failed.
I'm sure that there is much more available here, but this seems to be the most important part. 

1. Go to travis-ci.com
2. Link Github account, all public repos should appear
3. Select a repo to work with and toggle the slidebar next to it to activate. 
4. Click on the repo's name to get started
5. Click "Read the Docs and Get Started" to really figure out what is going on, though I'll try to write a brief tutorial here
6. Add a .travis.yml file to your repository to tell Travis CI what to do, commit and push this to the github repo.
7. Go to travis-ci.com again to check the build status and see if your code passed or failed. 
