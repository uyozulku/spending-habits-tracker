# Contributing to Spending-Habits-Tracker

## Prerequisites:
This project requires Python 3.6 and above. Before starting your contribution, please make sure to have Python installed. 

## Development Dependencies:
To install development dependencies, execute `make develop`. This will install and build this library and its dependencies using `pip`.

## Contribution Instructions:
#### Fork and Clone:
You will need your own fork to work on the code. Go to the `spending-habits-tracker project
page <https://github.com/uyozulku/spending-habits-tracker>` and hit the ``Fork`` button. You will want to clone your fork on your local machine:

    git clone https://github.com/uyozulku/spending-habits-tracker.git sht-dev[YourName]
    cd sht-dev[YourName]
    git remote add upstream https://github.com/uyozulku/spending-habits-tracker.git
    git fetch upstream

#### Branch
You may create a new branch for your contribution as follows:

    git checkout -b new-feature

####  Commit and push your changes:

After making your changes, commit them to your new-feature branch. Then, push your forked feature branch's commits:

    git push origin new-feature

####  Testing and Linting:
Before opening a  PR, please run testing and perform static analysis. Make sure to add new tests for any new features.

To test your changes, please execute `make test` (or `make coverage` to test with coverage).
For static analysis, you may use `make lint`. Further details on these commands are provided in the Further Development Details section.

####  Create a Pull Request:
When you're ready to ask for a code review, file a pull request:
    - Navigate to your repository on GitHub -- https://github.com/your-user-name/spending-habits-tracker
    - Click on ``Branches``
#. Click on the ``Compare`` button for your feature branch
#. Select the ``base`` and ``compare`` branches, if necessary. This will be ``main`` and
   ``new-feature``, respectively.

##  Further Development Details:
This library uses a `Makefile` as a command registry, with the following commands. 

- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution
