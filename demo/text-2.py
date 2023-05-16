
# #### 知识点 
# #### 要求一个结构化的输出
from demo.base import get_completion

prompt = f"""
请生成包括书名、作者和类别的三本虚构书籍清单，\
并以 JSON 格式提供，其中包含以下键:book_id、title、author、genre。
"""
response = get_completion(prompt)
print(response)