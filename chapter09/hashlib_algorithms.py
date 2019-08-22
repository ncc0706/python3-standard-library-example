import hashlib

# 返回可用的散列函数名集合, 相同的函数可能会以不同的名字（大小写）出现多次,目前共33个
available = hashlib.algorithms_available

# MDC2 新增的函数
print('available: {}\n{}\n'.format(len(available), ','.join(sorted(available))))

# 返回本模块支持的散列函数名集合, 没有大小写的问题
guaranteed = hashlib.algorithms_guaranteed
print('guaranteed: {}\n{}\n'.format(len(guaranteed), ','.join(sorted(guaranteed))))
