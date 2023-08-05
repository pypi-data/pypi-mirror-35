# -*- coding: utf-8 -*-
from slack_bang.bang import post_to_slack
from slack_bang.bang_web import run_web


def main():
    post_to_slack()


def web():
    run_web()

if __name__ == "__main__":
    main()
