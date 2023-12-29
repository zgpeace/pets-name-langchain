import time

def measure_execution_time(func, *args, **kwargs):
    """测量并返回给定函数的执行时间。

    Args:
        func: 要测量的函数对象。
        *args: 传递给函数的位置参数。
        **kwargs: 传递给函数的关键字参数。

    Returns:
        tuple: (执行结果, 耗时秒数)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# 示例：假设 chain1 已经定义并且具有 invoke 方法
# chain1 = ...

# 使用 measure_execution_time 来测量 chain1.invoke 的执行时间
# result, exec_time = measure_execution_time(chain1.invoke, {"topic": "bears"})
# print(f"执行结果: {result}")
# print(f"函数执行耗时: {exec_time} 秒")
