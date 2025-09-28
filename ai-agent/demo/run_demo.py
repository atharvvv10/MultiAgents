from src.agent import handle_command

print("🤖 AI Notes & QnA Agent (type 'exit' to quit)")
while True:
    cmd = input("> ")
    if cmd.lower() in ["exit", "quit"]:
        break
    result = handle_command(cmd)
    print(result)
 
