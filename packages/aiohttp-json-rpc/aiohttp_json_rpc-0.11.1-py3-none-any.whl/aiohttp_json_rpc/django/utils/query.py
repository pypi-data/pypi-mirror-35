from copy import copy

from django.db.models import Q


def parse_query(raw_query):
    """
    {'a': 1}
    [{'a': 1}, 'OR', {'b': 1}]

    """

    def parse_part(part):
        for part in query:
            if isinstance(part, dict):
                return Q(**part)

            elif isinstance(part, list):
                for i, sub_part in enumerate(part):
                    if isinstance(part, str):
                        continue

                    part[i] = parse_part(sub_part)


    query = copy(raw_query)

    if not isinstance(query, list):
        query = list(query)

    query = parse_part(query)

    return query


def list_of(types, min_length=None, max_length):
    if not isinstance(types, tuple):
        types = tuple(types)

    def _list_of(l):
        for i in l:
            assert isinstance(i, types)



def number(i=None, allow_float=True, allow_str=True, range=None):
    def _number(i):
        # types
        allowed_types = [int, ]

        if allow_float:
            allowed_types.append(float)

        if allow_str:
            allowed_types.append(str)

        assert isinstance(i, tuple(allowed_types))

    if i:
        return _number(i)

    return _number
