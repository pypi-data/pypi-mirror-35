import maya
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import time
import smtplib


class Watcher(object):
    def __init__(self, url,
                       email_from_addr=None,
                       email_to_addr=None,
                       email_password=None,
                       email_host="smtp.gmail.com",
                       email_port=587,
                       email_subject="New craigslist posts",
                       watch_duration=1,
                       watch_interval=30):
        self.url = url
        self.watch_duration = (int(watch_duration) * 60)
        self.watch_interval = int(watch_interval)
        self.results = OrderedDict()
        self.email_from_addr = email_from_addr
        self.email_to_addr = email_to_addr
        self.email_password = email_password
        self.email_host = email_host
        self.email_port = email_port
        self.email_subject = email_subject

    def add_new_result(self, new_posts=[]):
        dt = maya.now().datetime()
        time = dt.strftime("%H%M%S")
        date = dt.strftime("%Y%m%d")
        stamp = "{}_{}".format(date, time)
        self.results[stamp] = new_posts

    def get_posts(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "html.parser")
        result_rows = soup.findAll("li", {"class": "result-row"})
        data = []
        for result in result_rows:
            title = result.find("a", {"class": "result-title"})
            href = title.get("href")
            text = title.text
            data.append({
                "title": text,
                "url": href,
            })
        return data

    def get_current_posts(self):
        current_posts = []
        for k,v in self.results.items():
            for d in v:
                current_posts.append(d)
        return current_posts

    def filter_new_posts(self, posts):
        current_posts = self.get_current_posts()
        new_posts = []
        for post in posts:
            if post not in current_posts:
                new_posts.append(post)
        return new_posts

    def get_new_posts(self):
        posts = self.get_posts()
        new_posts = self.filter_new_posts(posts)
        self.add_new_result(new_posts)
        return new_posts

    def email_new_posts(self, new_posts):
        if any(x is None for x in [
            self.email_to_addr,
            self.email_from_addr,
            self.email_host,
            self.email_port,
            self.email_password,
            self.email_subject,
        ]):
            print(" >> Can't send email - missing parameter.")
            return
        if not len(new_posts):
            print (" >> No new posts to email. Skipping.")
            return
        try:
            server = smtplib.SMTP(self.email_host, self.email_port)
            server.ehlo()
            server.starttls()
            server.login(self.email_from_addr, self.email_password)
            email_message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(
                self.email_from_addr,
                self.email_to_addr,
                self.email_subject,
                "\n".join([
                    "{} - {}".format(x["title"], x["url"])
                    for x in new_posts
                ])
            )
            server.sendmail(self.email_from_addr, self.email_to_addr, email_message)
            server.close()
        except:
            print(" >> Failed to send email.")
            pass

    def reset_results(self):
        self.results = OrderedDict()

    def start(self):
        repeat = True
        while repeat:
            print(" >> Finding new posts.")
            # Get the new posts and email them.
            new_posts = self.get_new_posts()
            self.email_new_posts(new_posts)
            # Calculate the results
            total_results = len(self.results.keys())
            max_results = (self.watch_duration / self.watch_interval)
            # Toggle whether or not to continue the loop
            if (total_results == max_results):
                repeat = False
            # If the loop is continuing, delay the next cycle.
            if repeat:
                time.sleep(self.watch_interval)
        print(" >> Watch finished")

