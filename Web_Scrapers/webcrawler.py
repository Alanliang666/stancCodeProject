"""
File: webcrawler.py
Name: Alan Liang
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    """
    Crawls the SSA website for name data from specific decades (2010s, 2000s, 1990s).
    Parses the HTML text to calculate and print total number of male and female babies.
    """
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        total_men, total_women = 0, 0
        lis = []  # The list contains population counts in an alternating order [Male, Female, Male, Female, ....]
        for tag in tags:
            tokens = tag.text.split()
            for token in tokens:
                if ',' in token:  # Filter for strings containing commas
                    s = ""
                    for ch in token:  # Remove commas to convert formatted number string
                        if ch is not ',':
                            s += ch
                    lis.append(s)

        # Calculate men and women number
        for i in range(len(lis)):
            if i % 2 == 0:  # Even indices represent Male counts.
                total_men += int(lis[i])
            elif i % 2 != 0:  # Odd indices represent Female counts.
                total_women += int(lis[i])

        print(f"Male Number: {total_men}")
        print(f"Female Number: {total_women}")

        driver.quit()


if __name__ == '__main__':
    main()
