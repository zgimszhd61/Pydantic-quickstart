from datetime import datetime
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int  # 必须是整数
    name: str = 'John Doe'  # 默认值为 'John Doe'
    signup_ts: datetime | None  # 可以是 datetime 对象或 None
    tastes: dict[str, PositiveInt]  # 字典，键为字符串，值为正整数

# 外部数据
external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        'cheese': 7,
        'cabbage': '1',
    },
}

# 创建 User 实例
user = User(**external_data)

# 打印用户 ID
print(user.id)  # 输出: 123

# 打印模型数据
print(user.model_dump())
# 输出:
# {
#     'id': 123,
#     'name': 'John Doe',
#     'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
#     'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
# }