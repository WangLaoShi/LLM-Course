from http import HTTPStatus
from dashscope import Application


def call_agent_app():
    response = Application.call(app_id='8ffce74e085646e5834878e722c1a571',
                                prompt='如何做炒西红柿鸡蛋？',
                                api_key='sk-444',

                                )

    if response.status_code != HTTPStatus.OK:
        print('request_id=%s, code=%s, message=%s\n' % (response.request_id, response.status_code, response.message))
    else:
        print('request_id=%s\n output=%s\n usage=%s\n' % (response.request_id, response.output, response.usage))


if __name__ == '__main__':
    call_agent_app()
