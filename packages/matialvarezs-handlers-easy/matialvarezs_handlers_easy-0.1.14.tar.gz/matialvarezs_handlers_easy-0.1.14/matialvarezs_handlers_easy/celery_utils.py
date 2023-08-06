from celery.result import AsyncResult


def get_result_task_1(result):
    value = None
    for item in result.collect():
        #print("item", item, item[1])
        value = item[1]
    return value


def get_result_task_2(result):
    for item in result.collect():
        pass
    return result.result


def get_result_task_3(result):
    return result.get(timeout=None)


def get_result_task_4(self, result):
    return AsyncResult(result).ready()