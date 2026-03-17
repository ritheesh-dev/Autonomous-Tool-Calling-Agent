import ollama
import action_selection
import parse
import tool_description
import tool_dispatcher

def run_agent(question: str):
    # 1. Ask LLM to decide what to do
    prompt = action_selection.build_prompt(question, tool_description.TOOLS)
    response = ollama.generate(model='mistral', prompt = prompt)
    llm_output = response['response']

    # 2. parse the decision

    action_type, content, argument = parse.parse_action(llm_output)

    if action_type == "tool":
        print(f"[using tool]:{content, argument}")

        tool_result = tool_dispatcher.dispatch_tool(content, argument)
        print(f"[Tool result: {tool_result}]")

        followup = f"""The user asked: "{question}"
        You used the tool '{content}' and got this result: {tool_result}
        Now give a friendly, complete answer to the user."""

        final = ollama.generate(model='mistral', prompt = followup)
        print("Answer:", final['response'])

#Main loop:
while True:
    question = input("\nAsk something (or 'exit' to quit): ")

    if question.lower() in ['exit', 'quit']:
        print("Goodbye! 👋")
        break

    run_agent(question)