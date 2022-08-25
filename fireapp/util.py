from typing import Any, Dict, List


def to_representation(obj):
    return [elem._meta for elem in obj]

def filter_objects(objects: List[object], filter: Dict[str, Any]):
    '''
        Arguments:
            objects: List models Good, Link...
            filter: key - field name, value - field's value
    '''
    return [obj for obj in objects if all([obj._meta.get(key) == value for key, value in filter.items()])]
