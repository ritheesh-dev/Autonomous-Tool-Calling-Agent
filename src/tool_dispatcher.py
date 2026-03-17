import create_tools

TOOL_REGISTRY ={
    "get_current_date": lambda arg: create_tools.get_current_date(),
    "calculate":        lambda arg: create_tools.calculate(arg),
    "get_weather":      lambda arg: create_tools.get_weather(arg),

}

def dispatch_tool(tool_name: str, argument: str) -> str:
    if tool_name in TOOL_REGISTRY:
        return TOOL_REGISTRY[tool_name](argument)
    
    return f"unknown tool: {tool_name}"