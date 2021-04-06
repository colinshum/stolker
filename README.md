# Stolker

## Preview
CLI UI coming soon:

![image](https://user-images.githubusercontent.com/11053683/113663349-dd1ef400-9677-11eb-96a6-7793804c97e4.png)


## Basics

Stolker is a basic Python-based CLI client to view your portfolio's holdings. It uses the Yahoo Finance API to gather information about your portfolio.

## Getting Started

Firstly, clone this repository:
`git clone https://github.com/colinshum/stolker`

Next, install the dependencies using:
```
pip3 install yfinance
pip3 install pandas
```

In the project's root directory, create a new file called `portfolio.txt` with the following information in each line:
`<TICKER> <SHARES> <AVG_COST [OPTIONAL]>`

### Example:

```
AAPL 5 20.10
GME 20 45.10
MSFT 2
```

Finally, run the program with `python3 stolker.py`.

