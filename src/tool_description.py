TOOLS = [
    {
        "name": "get_current_date",
        "description": "Use this when the user asks about today's date or current time.",
        "parameters": {}   # no inputs needed
    },
    {
        "name": "calculate",
        "description": "Use this for any math calculation. Input is a math expression string.",
        "parameters": {
            "expression": "string  # e.g. '15 * 4 + 7'"
        }
    },
    {
        "name": "get_weather",
        "description": "Use this when the user asks about weather. Input is a city name.",
        "parameters": {
            "city": "string  # e.g. 'Chennai'"
        }
    }
]