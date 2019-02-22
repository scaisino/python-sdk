# -*- coding: utf-8 -*-
"""
改变文件状态，可用或不可用
"""
from qiniu import Auth
from qiniu import BucketManager

# 需要填写你的 Access Key 和 Secret Key
access_key = 'C3S6li9F4Iq9toDkq3tzoHz_tRwS2LWNE9aUjIJy'
secret_key = 'VsjH9zF3XdFfeo6K6y-nyEU5ia62NTW4KM7xcwt4'

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

# 空间名
bucket_name = 'bernie'

# 文件名
key = '233.jpg'

# 条件匹配，只有匹配上才会执行修改操作
# cond可以填空，一个或多个
cond = {"fsize": "186371",
        "putTime": "14899798962573916",
        "hash": "FiRxWzeeD6ofGTpwTZub5Fx1ozvi",
        "mime": "image/png"}

ret, info = bucket.change_status(bucket_name, key, '1', cond)
print(info)
