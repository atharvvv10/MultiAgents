from agents import Agent
from utils.logger import logger

if __name__ == "__main__":
    agent = Agent()
    print("Multi-LLM Chat (type 'exit' or 'quit' to stop)")
    while True:
        prompt = input("User: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = agent.run(prompt)
        logger.info(f"Response: {response}")
        print(f"Assistant: {response}")
