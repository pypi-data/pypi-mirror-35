# -*- coding: utf-8 -*-
import os
import json
import requests
from furl import furl
from slack_bang import app_config, channel_tokens

DEFAULT_WEBHOOK_URI = app_config.get('slack_webhook_uri', 'https://hooks.slack.com/services/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')
BAMBOO_URL = app_config.get('BAMBOO_URL', os.getenv('BAMBOO_URL', 'https://bamboo.dglecom.net'))
BAMBOO_USER = app_config.get('BAMBOO_USER', os.getenv('BAMBOO_USER'))
BAMBOO_PASSWORD = app_config.get('BAMBOO_PASSWORD', os.getenv('BAMBOO_PASSWORD'))

class SlackPostException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class GenericMessageService(object):
    WEBHOOK_URI = DEFAULT_WEBHOOK_URI

    def __init__(self, token, channel, text, *args, **kwargs):
        self.token = token
        self.channel = channel
        self.text = text
        self.attachments = json.loads(kwargs.get('attachments', '[]'))

        if channel_tokens.get(token) != channel:
            raise UnauthorizedException('Token {t} is not allowed to post to channel {c}'.format(t=token, c=channel))

        # optionals
        self.username = kwargs.get('username', 'monkey-bot')
        self.emoji = kwargs.get('emoji', ':monkey_face:')
        self.webhook_url = kwargs.get('webhook_url', self.WEBHOOK_URI)

    def process(self):
        data = {
            "text": self.text,
            "channel": "#{channel}".format(channel=self.channel),
            "link_names": 1,
            "username": self.username,
            "icon_emoji": "{emoji}".format(emoji=self.emoji),
        }

        if self.attachments:  # may not be null at slack
            data['attachments'] = self.attachments

        resp = requests.post(self.webhook_url, json=data)

        if resp.ok:
            return resp
        else:
            raise SlackPostException(resp.content)


class ProjectBuildService(object):
    WEBHOOK_URI = DEFAULT_WEBHOOK_URI

    def __init__(self, version, plan_name, build_url, channel, *args, **kwargs):
        self.version = version
        self.plan_name = plan_name
        self.build_url = build_url
        self.channel = channel

        # optionals
        self.text = kwargs.get('text', "Build Complete: {build_url}".format(build_url=self.build_url))

        self.plan, self.build_no = self.bamboo_build_url_components(build_url=self.build_url)

        if self.plan and self.build_no:
            self.build_result = self.get_bamboo_build_result(plan=self.plan,
                                                             build_no=self.build_no)

        self.username = kwargs.get('username', 'build-info')

        self.emoji = kwargs.get('emoji', ':cherries:')
        self.webhook_url = kwargs.get('webhook_url', self.WEBHOOK_URI)

    def bamboo_build_url_components(self, build_url):
        url = furl(build_url)
        build = str(url.path).split('/')
        try:
            build_name = build[-1:][0]
            # ['OBB', 'DB', '152']
            build_no = build_name.split('-')[-1:][0]
            # ['152']
            plan = '-'.join(build_name.split('-')[0:-1])
            # 'OBB-DB'
            return plan, build_no
        except IndexError:
            return None, None

    def get_bamboo_build_result(self, plan, build_no):
        # https://bamboo.dglecom.net/rest/api/latest/result/OBB-DB/152.json
        url = furl('{url}/rest/api/latest/result/{plan}/{build_no}.json'.format(url=BAMBOO_URL,
                                                                                plan=plan,
                                                                                build_no=build_no))
        resp = requests.get(url, auth=(BAMBOO_USER, BAMBOO_PASSWORD))
        data = {}
        if resp.ok:
            data = resp.json()
        return data.get('state', 'Unknown')

    def process(self):
        attachments = [{
            "text": "Version: {version}".format(version=self.version)
        }]

        if self.plan_name:
            attachments.append({"text": "Plan: {plan_name}".format(plan_name=self.plan_name)})
        if self.build_url:
            attachments.append({"text": "Build: {build_url}".format(build_url=self.build_url)})
        if self.build_result:
            attachments.append({"text": "Result: {build_result}".format(build_result=self.build_result)})

        data = {
            "text": self.text,
            "attachments": attachments,
            "channel": "{channel}".format(channel=self.channel),
            "link_names": 1,
            "username": self.username,
            "icon_emoji": "{emoji}".format(emoji=self.emoji)
        }

        resp = requests.post(self.webhook_url, json=data)
        if resp.ok:
            return resp
        else:
            raise SlackPostException(resp.content)