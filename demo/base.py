import openai
import os
from dotenv import load_dotenv, find_dotenv

# 导入第三方库

_ = load_dotenv(find_dotenv())
# 读取系统中的环境变量

openai.api_key  = os.getenv('OPENAI_API_KEY')
# 设置 API_KEY

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    '''
    prompt: 对应的提示
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)，有内测资格的用户可以选择 gpt-4
    temperature: 温度系数
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]
   

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # 控制模型输出的随机程度
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)