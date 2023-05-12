# spending-habits-tracker
Project for Open Source Development (COMS 4995)

![License](https://img.shields.io/github/license/uyozulku/spending-habits-tracker)
![Issues](https://img.shields.io/github/issues/uyozulku/spending-habits-tracker)
[![codecov](https://codecov.io/gh/uyozulku/spending-habits-tracker/branch/main/graph/badge.svg?token=0TCR1MSIWH)](https://codecov.io/gh/uyozulku/spending-habits-tracker)
[![Build Status](https://github.com/uyozulku/spending-habits-tracker/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/uyozulku/spending-habits-tracker/actions?query=workflow%3A%22Build+Status%22)
[![PyPI](https://img.shields.io/pypi/v/spending-habits-tracker)](https://pypi.org/project/spending-habits-tracker/)


## Overview
Spending-Habits-Tracker is a Python library to track and visualize spending habits. The library makes use of documents provided by the user (e.g. bank statements) to generate visualizations of spending habits over time. The library also provides a command line interface to interact with the library.

### Development and Contributions:
For development details and contribution instructions, please refer to the [contribution guidelines](https://github.com/uyozulku/spending-habits-tracker/blob/main/CONTRIBUTING.md).

## Installation
### Requirements
- Python 3.6 or higher
- Pandas
- Matplotlib

### Install from PyPI
```bash
pip install pandas
pip install matplotlib
pip install spending-habits-tracker
```

## Usage
Below is a simple use-case for quick start:
```python
import spending_habits_tracker as sht

# get data from csv file
data = sht.get_data('data.csv')

# create a spending tracker object
tracker = sht.SpendingTracker(data)

# plot spending over time
tracker.plot_spending_over_time()
```


