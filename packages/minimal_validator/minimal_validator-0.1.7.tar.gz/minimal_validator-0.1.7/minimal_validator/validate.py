import itertools

from collections import Counter

from email_validator import validate_email, EmailNotValidError

def flatten(items):
    return list(itertools.chain.from_iterable(items))

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def map_with_predicate(f, items, predicate):
    results = []
    for item in items:
        mapped_value = f(item)
        results.append(mapped_value)

        if not predicate(mapped_value):
            break

    return results

class Result():
    def __init__(self, status, attribute, value, keep_checking = True,
        code = None, params = None, message = None):
        self.status = status
        self.attribute = attribute
        self.value = value
        self.code = code
        self.params = params
        self.message = message
        self.keep_checking = keep_checking

    def to_dict(self):
        d = {
            'status': self.status,
            'attribute': self.attribute,
            'value': self.value,
        }

        if self.code:
            d['code'] = self.code

        if self.params:
            d['params'] = self.params

        if self.message:
            d['message'] = self.message

        return d

def combine_validators(attribute, data, validators):
    def validate_sequentially():
        validation_results = map_with_predicate(lambda v: v(attribute, data),
            validators, lambda r: not r or r.keep_checking)

        return filter(lambda r: r is not None, validation_results)

    return validate_sequentially

def combine_validation_results(*attribute_validators):
    return flatten([validate() for validate in attribute_validators])

def attribute_exists(attribute, data):
    if attribute not in data:
        message = '`{}` has not been supplied'.format(attribute)

        return Result(status='error',
            attribute = attribute,
            value = None,
            keep_checking = False,
            code = 'ATTRIBUTE_UNDEFINED',
            message = message)

    return None

def value_is_set(attribute, data):
    if data[attribute] == None or data[attribute] == '':
        message = '`{}` is empty'.format(attribute)

        return Result(status = 'error',
            attribute = attribute,
            value = data[attribute],
            keep_checking = False,
            code = 'VALUE_EMPTY',
            message = message)

    return None

def value_is_type(attribute, data, expected_type):
    value = data[attribute]

    try:
        expected_type(value)
    except ValueError as e:
        message = '`{}` is wrong type'.format(attribute)

        return Result(status = 'error',
            attribute = attribute,
            value = data[attribute],
            keep_checking = False,
            code = 'VALUE_TYPE_MISMATCH',
            params = { 'expected_type': expected_type.__name__ },
            message = message)

    return None

def value_is_valid_email(attribute, data):
    try:
        value = data[attribute]
        v = validate_email(value)

        return None
    except EmailNotValidError as e:
        message = '`{}` is invalid email'.format(attribute)

        return Result(status = 'error',
            attribute = attribute,
            value = data[attribute],
            code = 'VALUE_INVALID_EMAIL',
            message = message)

def value_has_min_length(attribute, data, min_length):
    value = data[attribute]

    if len(value) < min_length:
        return Result(status = 'error',
            attribute = attribute,
            value = data[attribute],
            code = 'VALUE_TOO_SHORT',
            params = { 'min_length': min_length },
            message = '`{}` is too short'.format(attribute))

    return None

def value_has_max_length(attribute, data, max_length):
    value = data[attribute]

    if len(value) > max_length:
        return Result(status = 'error',
            attribute = attribute,
            value = data[attribute],
            code = 'VALUE_TOO_LONG',
            params = { 'max_length': max_length },
            message = '`{}` is too long'.format(attribute))

    return None

def value_matches_at_least(attribute, data, match_list, min_matches):
    value = data[attribute]

    count = Counter(value)

    num_matches = sum([count[item] for item in match_list])

    if num_matches < min_matches:
        return Result(status='error',
            attribute = attribute,
            value = data[attribute],
            code = 'NOT_ENOUGH_MATCHES',
            params = { 'match_list': match_list ,
                'min_matches': min_matches },
            message = '`{}` does not have enough matches'.format(attribute))

    return None

def value_is_at_least(attribute, data, min_value):
    value = data[attribute]

    if num(value) < min_value:
        return Result(status='error',
            attribute = attribute,
            value = data[attribute],
            code = 'VALUE_TOO_SMALL',
            params = { 'minimum_value': min_value},
            message = '`{}` is too small'.format(attribute))

    return None

def value_is_at_most(attribute, data, max_value):
    value = data[attribute]

    if num(value) > max_value:
        return Result(status='error',
            attribute = attribute,
            value = data[attribute],
            code = 'VALUE_TOO_BIG',
            params = { 'maximum_value': max_value},
            message = '`{}` is too big'.format(attribute))

    return None