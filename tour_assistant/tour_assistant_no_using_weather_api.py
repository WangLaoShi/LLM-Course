# -*- encoding: utf-8 -*-
import json
import sys
import dashscope
from http import HTTPStatus
from dashscope import Assistants, Messages, Runs, Threads
from function_utils import *

dashscope.api_key = "sk-0bea5c93245446f0a4753962ef405a1"


def create_assistant():
    # create assistant with information
    assistant = Assistants.create(
        model='qwen-max',
        name='smart helper',
        description='一个旅游助手，可以通过用户诉求，调用天气查询，路径推荐，当地餐厅推荐等帮助用户。',
        instructions='你是一个旅游助手，可以通过调用插件解决问题。插件例如，天气查询，路径推荐，当地餐厅推荐等，' +
                     '当你无法回答问题时应当结合插件回复进行回答。请根据插件结果适当丰富回复内容。',
        tools=[
            {
                'type': 'function',
                'function': {
                    'name': '天气查询',
                    'description': '用于查询天气的插件和函数',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'location': {
                                'type': 'str',
                                'description': '待查询的地点'
                            },
                            'date': {
                                'type': 'str',
                                'description': '待查询的具体日期'
                            }
                        },
                        'required': ['location', 'date']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '路径规划',
                    'description': '用于推荐出行和旅游的路径规划，包含查询路线，规划起点到终点的路线。也用于推荐最近最热门的旅游行程。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'start': {
                                'type': 'str',
                                'description': '待查询路径规划的出发点'
                            },
                            'destination': {
                                'type': 'str',
                                'description': '待查询路径规划的终点.'
                            },
                            'recommendation': {
                                'type': 'int',
                                'description': '用于控制是否随机推荐，用于在无法判断有路径规划终点时，' +
                                               '设置为1，其他情况为0。此时会推荐最热门的旅游路线.'
                            }
                        },
                        'required': ['destination', 'start', 'recommendation']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '获取目的地建议',
                    'description': '用于推荐最近热门的旅游目的地。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'query': {
                                'type': 'str',
                                'description': '可能需要的信息'
                            },
                        },
                        'required': ['query']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '获取景点推荐',
                    'description': '用于推荐指定城市的旅游景点。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'city': {
                                'type': 'str', 'description': '城市名称'
                            },
                        },
                        'required': ['city']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '获取餐饮推荐',
                    'description': '用于推荐指定城市的餐饮。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'city': {
                                'type': 'str',
                                'description': '城市名称'
                            },
                        },
                        'required': ['city']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '获取旅行提示',
                    'description': '用于获取指定城市的旅行注意事项。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'city': {
                                'type': 'str', 'description': '城市名称'
                            },
                        },
                        'required': ['city']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': '获取当地风俗',
                    'description': '用于获取指定城市的当地风俗。',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'city': {
                                'type': 'str', 'description': '城市名称'
                            },
                        },
                        'required': ['city']
                    }
                }
            },
        ],
    )
    return assistant


function_mapper = {
    "天气查询": get_weather,
    "路径规划": get_path_recommendation,
    "获取目的地建议": get_destination_recommendation,
    "获取景点推荐": get_attraction_recommendation,
    "获取餐饮推荐": get_dining_recommendation,
    "获取旅行提示": get_life_tips,
    "获取当地风俗": get_local_customs,
}


def verify_status_code(res):
    if res.status_code != HTTPStatus.OK:
        sys.exit(res.status_code)

def send_message(assistant, message='查询杭州天气'):
    print(f"Query: {message}")

    # create a thread.
    # dashscope api
    thread = Threads.create()
    print(thread)

    # create a message.
    # dashscope api
    message = Messages.create(thread.id, content=message)
    # create run
    # dashscope api
    run = Runs.create(thread.id, assistant_id=assistant.id)
    print(run)

    # get run statue
    # run_status = Runs.get(run.id, thread_id=thread.id)
    # print(run_status)

    # wait for run completed or requires_action
    run_status = Runs.wait(run.id, thread_id=thread.id)
    print(run_status)

    # if prompt input tool result, submit tool result.
    if run_status.required_action:
        f = run_status.required_action.submit_tool_outputs.tool_calls[0].function
        func_name = f['name']
        param = json.loads(f['arguments'])
        print(func_name)

        if func_name in function_mapper:
            output = function_mapper[func_name](**param)
        else:
            output = ""

        tool_outputs = [{'output': output}]

        run = Runs.submit_tool_outputs(run.id, thread_id=thread.id, tool_outputs=tool_outputs)

        # should wait for run completed
        run_status = Runs.wait(run.id, thread_id=thread.id)
        # print(run_status)
        verify_status_code(run_status)

    run_status = Runs.get(run.id, thread_id=thread.id)
    print(run_status)
    # verify_status_code(run_status)
    # get the thread messages.
    msgs = Messages.list(thread.id)
    # print(msgs)
    # print(json.dumps(msgs, default=lambda o: o.__dict__, sort_keys=True, indent=4))
    print("运行结果:")
    for message in msgs['data'][::-1]:
        print("content: ", message['content'][0]['text']['value'])
    print("\n")


if __name__ == '__main__':
    assistant = create_assistant()
    send_message(assistant=assistant, message="丽江天气怎么样？")
    # send_message(assistant=assistant,message="年假打算出去玩，有什么地点推荐吗")
    # send_message(assistant=assistant,message="从北京去丽江怎么出行方便？")
    # send_message(assistant=assistant,message="丽江有什么好玩的地方？")
    # send_message(assistant=assistant,message="我喜欢吃，丽江有什么美食推荐吗")
    # send_message(assistant=assistant,message="去丽江还应该注意什么？")
    # send_message(assistant=assistant,message="能告诉我丽江当地有什么风俗吗")
    # send_message(assistant=assistant,message='从杭州到北京的出行推荐')
