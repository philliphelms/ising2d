# ising2d
This code was developed as part of the Simon's Institute Summer School, 2018.

The overall goal of this code is to determine the ground state of the 2D Ising model, 
but the goal of the exercise is to practice the following:
+ Pair Programming
  + Two coders work on one workstation, i.e. physically passing a laptop back and forth. 
  + One writes the code while the other observes to check for correctness.
  + Frequently collabarte about possible approaches/solutions.
  + Roles switch frequently.
+ Test Driven Development
  + A software development strategy that relies on a short cycle:
    1. Create Test (which will initially fail and thus defines short term goals).
    2. Write code until the test can be passed.
    3. Refactor code, i.e. clean up whatever was done so the code looks nice again.
  + An additional possible step is to add documentation (via Doxygen?) after refactoring. 
+ Version Control (via git/github)
+ Continuous Integration (via travis-ci)
  + Detailed discussion given below
+ Documentation (via Doxygen)
  + This was not covered in depth, but in essence, it allows programmers to write documentation within the comments of their code. 

## Continuous Integration
Travis provides the following definition of continuous integration: "Continuous Integration is the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments. This is where Travis CI comes in."
In essence, the primary functionality of Travis appears to be to:
1. Clone your github repo into a virtual environment
2. Builds and tests your code
3. Tells you whether the builds passed or failed.


I'm sure that there is much more available here, but this seems to be the most important part. 

Below is a brief set of instructions on how to do this. It seems fairly intuitive and took me only a few minutes to set up.

1. Go to travis-ci.com
2. Link Github account, all public repos should appear
3. Select a repo to work with and toggle the slidebar next to it to activate. 
4. Click on the repo's name to get started
5. Click "Read the Docs and Get Started" to really figure out what is going on, though I'll try to write a brief tutorial here
6. Add a .travis.yml file to your repository to tell Travis CI what to do (as described in the Travis documentation), commit and push this to the github repo.
7. Go to travis-ci.com again to check the build status and see if your code passed or failed. 
8. Additionally, when you look at commits in github, there will be a green checkmark next to those that passed the unittest and a red x next to those that failed.
