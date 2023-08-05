#!/usr/bin/env python
#
#/usr/bin/http -f POST https://hooks.slack.com/services/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 payload='{"text": "Sandbox Build Complete: ${bamboo.resultsUrl}", "attachments":[{"text": "Version: ${bamboo.releaseminion.version}-${bamboo.buildNumber}"}], "channel": "#${bamboo.releaseminion.channel}", "link_names": 1, "username": "bamboo-build-info", "icon_emoji": ":cherries:"}'
#
import argparse

from services import ProjectBuildService, GenericMessageService


def gather_project_build_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', help='The channel to post to', required=True)
    parser.add_argument('--version', help='The Version that was just build', required=True)
    parser.add_argument('--build_url', help='Bamboo Build URL', required=True)
    parser.add_argument('--emoji', help='Which emoji https://get.slack.help/hc/en-us/articles/202931348-Emoji-and-emoticons', required=False)
    parser.add_argument('--webhook_uri', help='Override the default webhook URI', required=False)
    parser.add_argument('--plan_name', help='The plan name', required=False)

    return parser.parse_args()


def gather_generic_message_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--channel', help='The channel to post to', required=True)
    parser.add_argument('--text', help='The generic text to be posted', required=True)
    parser.add_argument('--emoji', help='Which emoji https://get.slack.help/hc/en-us/articles/202931348-Emoji-and-emoticons', required=False)
    parser.add_argument('--webhook_uri', help='Override the default webhook URI', required=False)
    parser.add_argument('--attachments', help='slack Attachments', required=False)

    return parser.parse_args()


def post_to_slack():
    post_project_build()


def post_project_build():
    arguments = gather_project_build_arguments()
    emoji = getattr(arguments, 'emoji') if getattr(arguments, 'emoji') else ':cherries:'
    plan_name = getattr(arguments, 'plan_name') if getattr(arguments, 'plan_name') else None
    webhook_uri = getattr(arguments, 'webhook_uri') if getattr(arguments, 'webhook_uri') else None

    service = ProjectBuildService(version=arguments.version,
                                  plan_name=plan_name,
                                  build_url=arguments.build_url,
                                  channel=arguments.channel,
                                  webhook_uri=webhook_uri,
                                  emoji=emoji)

    resp = service.process()
    print(resp.ok)
    return resp


def post_generic_message_build():
    arguments = gather_generic_message_arguments()
    emoji = getattr(arguments, 'emoji') if getattr(arguments, 'emoji') else ':cherries:'
    attachments = getattr(arguments, 'attachments') if getattr(arguments, 'attachments') else None

    service = GenericMessageService(channel=arguments.channel,
                                    text=arguments.text,
                                    emoji=emoji,
                                    attachments=attachments)

    resp = service.process()
    print(resp.ok)
    return resp


if __name__ == '__main__':
    post_project_build()
