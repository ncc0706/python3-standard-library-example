import hashlib
from hashlib_data import lorem

sha1 = hashlib.sha1()

sha1.update(lorem.encode('UTF-8'))
print(sha1.hexdigest())
