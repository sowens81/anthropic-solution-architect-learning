from agent import Agent


def main():

    agent = Agent()

    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() in {"exit", "quit"}:
            break

        answer = agent.chat(question)

        print(f"\nClaude: {answer}\n")


if __name__ == "__main__":
    main()