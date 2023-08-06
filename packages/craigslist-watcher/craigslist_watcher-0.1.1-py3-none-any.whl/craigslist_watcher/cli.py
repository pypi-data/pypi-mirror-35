from .watcher import Watcher
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Watches a craigslist url for new posts and emails them to you."
    )
    parser.add_argument(
        "--url",
        help="The craigslist url to watch for new posts."
    )
    parser.add_argument(
        "--email-to-addr",
        help="The email address to send alerts to."
    )
    parser.add_argument(
        "--email-from-addr",
        help="The email to send email alerts from."
    )
    parser.add_argument(
        "--email-password",
        help="The password for the email-from-addr account."
    )
    parser.add_argument(
        "--email-host",
        help="The address of the email host.",
        default="smtp.gmail.com",
    )
    parser.add_argument(
        "--email-port",
        help="The port to connect to the email host on.",
        default=587
    )
    parser.add_argument(
        "--email-subject",
        help="The subject to use for the emails.",
        default="New craigslist posts"
    )
    parser.add_argument(
        "--watch-interval",
        help="The number of seconds to wait between checking for new posts",
        default=30,
    )
    parser.add_argument(
        "--watch-duration",
        help="The number of minutes to continue watching for.",
        default=1
    )
    args = parser.parse_args()
    args_dict = vars(args)
    w = Watcher(**args_dict)
    w.start()


