# cli_covid_bot
This is my attempt to deploy the COVID-Bot in a manner that can be used with the command line instead of an ipynb.

The COVID-Chat-Bot was my final project with Thinkful's Data Science Immersion course.

Feel free to use and upgrade the code/bot mechanics, etc.

Relevant imports are thus:

Pandas
Numpy
Sklearn
NLTK

Versions should not matter, but if you run into version issues, these would be current as of 8.27.2020.

I could write a requirements.txt, but I am just not going to, ha.

The questions and answers come from a fixed list scraped from the CDC, WHO, FDA, and Euro CDC in late March 2020.

Some information might be (probably is) out of date.

Big thanks to Dennis Tran (instructor) for helping me apply all things I learned in such a short time.

$python covid_bot.py to run it

Ask the bot questions and if it is an 80% match or better it will return the answer.

If less than 80%, it will show you the top 3 scoring questions closest to what you asked.

Pick the number corresponding to your question and it will give you the answer.

