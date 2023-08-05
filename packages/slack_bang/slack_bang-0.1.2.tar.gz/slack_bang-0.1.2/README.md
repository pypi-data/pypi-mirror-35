Slack Bang
==========

Simple python script to send Build Success Data to webhooks (slack, or other)


Usage
-----

```
slack_bang --channel it-ops --version 1234567-1 --build_url http://www.example.com
```

or

```
python -m slack_bang
```


```
http post http://localhost:8004/generic-message/ channel=dev-ops text='yay' attachments='[{"fallback": "View Logs","title": "View Logs","actions": [{"name": "action","type": "button","text": "View","url": "http://logs.dglecom.net","value": "view"}]}]' token='d38e7972-9325-44a9-8128-9ac4b64909fb'
```