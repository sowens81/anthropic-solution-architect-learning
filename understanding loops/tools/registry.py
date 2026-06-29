TOOL_DEFINITIONS = []
TOOL_FUNCTIONS = {}


def tool(name: str, description: str, input_schema: dict):
    """
    Decorator used to register Claude tools.
    """

    def decorator(func):

        TOOL_DEFINITIONS.append({
            "name": name,
            "description": description,
            "input_schema": input_schema
        })

        TOOL_FUNCTIONS[name] = func

        return func

    return decorator