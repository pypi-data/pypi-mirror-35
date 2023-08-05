# Minimal Validator

`minimal_validator` is a very simple validation framework for python. 

## Installation

Installation into a [virtualenv](https://docs.python.org/3/tutorial/venv.html) is recommended. Also see [pipenv](https://docs.pipenv.org/). 

* Install from [pipy](https://pypi.org/) as external dependency: `$ pip install minimal-validator`
* Install source locally: `$ pip install -e .`
* Run unit tests: `$ python setup.py test`

## Overview
Minimal validator is a very simple validation framework. The framework expects to run through a list of validation functions. Each validation function must have at least two parameters: `attribute` and `data`. The `attribute` is a string representing the attribute in the `data` object to be validated. Each validation function returns a `Result` object. Several validation functions for the same attribute can be chained together with the `combine_validators` function. The `combine_validation_results` function is used to perform all of the validations against a given `data` object. 

Each `Result` has a `keep_checking` boolean that defaults to `True`. For a given attribute, if `keep_checking` is `True`, the `validate_sequentially` function of `combine_validators` will continue gathering results. If it's `False`, `validate_sequentially` will not run any subsequent validations in the list. The idea is that some errors make it impossible to continue validating. For example, if an attribute is not set, then no further validation logic can be applied to it. On the other hand, for something like a password, a number of validations such as "minimum length" and "presence of special characters", etc. can be applied indepdendently. In that case the final result of the validation will include all such errors rather than stopping at the first error encountered. 

## Examples
The following is an example `validate_username_and_password` function (along with a few helper functions) taken from the unit tests:

```python
def value_has_min_length_6(attribute, data):
    return value_has_min_length(attribute, data, 6) 

def value_has_max_length_12(attribute, data):
    return value_has_max_length(attribute, data, 12) 

def value_has_at_least_one_uppercase_char(attribute, data):
    return value_matches_at_least(attribute, data, 
        list(string.ascii_uppercase), 1)
    
def value_has_at_least_one_special_symbol(attribute, data):
    return value_matches_at_least(attribute, data,
        list('!@#$%^&*'), 1)
                        
@pytest.fixture
def validate_username_and_password():
    def validate(data):
        username_validators = combine_validators('username', 
            data, [attribute_exists, 
                value_is_set, 
                value_is_valid_email])        
                
        password_validators = combine_validators('password',
            data, [attribute_exists,
                value_is_set,
                value_has_min_length_6,
                value_has_max_length_12,
                value_has_at_least_one_uppercase_char,
                value_has_at_least_one_special_symbol])

        results = combine_validation_results(
            username_validators, 
            password_validators)
        
        return [result.to_dict() for result in results]            
        
    return validate
```

While the framework includes some validation functions, it will accept any function that takes `attribute` and `data` parameters and returns a valid `Result` object (or `None` if the validation passes and no validation messages are needed). 


If you just need a single validation function for a given attribute, you can just wrap that function in a `lambda` instead of using `combine_validators`. 

