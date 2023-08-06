# Craigslist Watcher

## Description

Emails a list of urls to new posts found on craigslist page.

## Installation

```
pip install craigslist-watcher
```

or

```
pipenv install craigslist-watcher
```

## Arguments

1. url - The craigslist page to watch
2. email-to-addr/email\_to\_addr - The email to send the new posts to.
3. email-from-addr/email\_from\_addr - The email to send the new posts from.
4. email-password/email\_password - The password for the email-from account.
5. email-host/email\_host - The ip/hostname of the email provider.
6. email-port/email\_port - The port to send the smtp message over.
7. email-subject/email\_subject - The subject of the emails that are sent.
8. watch-interval/watch\_interval - The number of seconds between each watch.
9. watch-duration/watch\_duration - The number of minutes to do all watching for.

## Usage

```
>> craigslist_watcher --url "https://southcoast.craigslist.org/search/jjj?query=&excats=&cat_id=11&userid=&postedToday=1&search_distance=&postal=" --email-to-addr "recipient_email_here@gmail.com" --email-from-addr "sending_email_here@gmail.com" --email-password "123456789" --email-host "smtp.gmail.com" --email-port 587 --email-subject "New craigslist posts" --watch-duration 1 --watch-interval 30
```

```
from craigslist_watcher import Watcher

watcher = Watcher(
    url="https://southcoast.craigslist.org/search/jjj?query=&excats=&cat_id=11&userid=&postedToday=1&search_distance=&postal=",
    email_to_addr="recipient_email_here@gmail.com",
    email_from_addr="sending_email_here@gmail.com",
    email_password="123456789",
    email_host="smtp.gmail.com",
    email_port=587,
    email_subject="New craigslist posts",
    watch_duration=1,
    watch_interval=30
)

watcher.start()
```