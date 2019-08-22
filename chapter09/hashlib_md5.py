import hashlib
from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem.encode('utf-8'))
# 16进制结果
print(h.hexdigest())
