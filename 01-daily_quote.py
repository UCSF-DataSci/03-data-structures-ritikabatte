#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "The best revenge is massive success. - Frank Sinatra",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "The best preparation for tomorrow is doing your best today. - H. Jackson Brown Jr."
]

def get_quote_of_the_day(quotes):
    today = date.today()
    random.seed(today.toordinal())
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /Users/ritikabatte02/03-data-structures-ritikabatte/01-daily_quote.py >> /Users/ritikabatte02/03-data-structures-ritikabatte/daily_quote.txt