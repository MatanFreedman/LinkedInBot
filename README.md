# LinkedInBot
<hr>
This project could be used to scrape LinkedIn job listings based on some keywords and locations. <br><br>

The project has been set up as a Python class object called LinkedInBot.

To use the bot, you'll need to set up the environment:

`pip install -r requirements.txt`

The bot has a "run" function that will login, go to the jobs tab, search a keyword string + location, and then scrape the first 8 pages saving the job title, company, location, and job description in a database saved in "data/linkedin_data.db".
```
EMAIL = "your email"
PASSWORD = "your password"

bot = LinkedInBot()
bot.run(EMAIL, PASSWORD, "Data Scientist", "Canada")
```

Once you've logged in once, the bot will save the browser cookies for reuse next time. If you wanted to configure your own 'run' function you'd use the following functions:

```
# log in and save cookies:
bot.login(email=EMAIL, password=PASSWORD)
bot.save_cookie("data/cookies.txt")

# go to jobs page and search:
keywords = "some string"
location = "whatever location"
bot.search_linkedin(keywords, location)
bot.wait()

# get all jobs from sidebar, scroll to each job and scrape info:
jobs = bot.driver.find_elements_by_class_name("occludable-update")
for job in jobs:
    bot.scroll_to(job)
    [position, company, location, details] = bot.get_position_data(job)

    # do whatever you like with the info...

bot.close_session()
```

Hope this is useful!