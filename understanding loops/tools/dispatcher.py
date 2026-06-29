from tools.registry import TOOL_FUNCTIONS


def execute_tool(tool_use):

    fn = TOOL_FUNCTIONS.get(tool_use.name)

    if fn is None:
        raise ValueError(f"Unknown tool '{tool_use.name}'")

    return fn(**tool_use.input)