from functools import reduce
import operator
from typing import Any


def getFromDict(data_dict: dict, dict_path_list: list) -> Any:
    return reduce(operator.getitem, dict_path_list, data_dict)
