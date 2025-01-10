from jsonschema import validate, ValidationError

def validate_json(response_json, schema):
    """
    Validate JSON response against a given schema.
    :param response_json: JSON data from API response.
    :param schema: Schema to validate against.
    :return: True if valid, False otherwise.
    """
    try:
        validate(instance=response_json, schema=schema)
        return True
    except ValidationError as e:
        print(f"Validation error: {e}")
        return False
