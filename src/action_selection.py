import tool_description

def build_prompt(question: str, tools: list) -> str:
    tool_descriptions = "\n".join([
        f"- {t['name']}: {t['description']}" for t in tool_description.TOOLS
    ])

    return f"""You are a helpful assistant with access to these TOOLS:
    {tool_descriptions}

    If the user's question requires a tool, respond ONLY in this exact format:
    USE_TOOL: <tool_name> | <argument>

    If no tool is needed, just answer normally.

    User question: {question}
    """