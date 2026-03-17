def parse_action(response_text: str):
    """
    return ('tool', tool_name, arg) or ('answer', text, None)
    """

    text = response_text.strip()
    if text.startswith("USE_TOOL:"):
        parts = text.replace("USE_TOOL:", "").split("|")
        tool_name = parts[0].strip()
        argument = parts[1].strip() if len(parts) > 1 else ""
        return ("tool", tool_name, argument)
    return("answer", text, None)