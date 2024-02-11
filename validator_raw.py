from cerberus import Validator

body = {
    "data": {
        "element": 123,
        "element2": "Hello World",
        "element3": "321",
    }
}

body_validator = Validator(
    {
        "data": {
            "type": "dict",
            "schema": {
                "element": {"type": "float", "required": True, "empty": False},
                "element2": {"type": "string", "required": True, "empty": True},
                "element3": {"type": "string", "required": True, "empty": False},
            },
        }
    }
)

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("Validation passed")
