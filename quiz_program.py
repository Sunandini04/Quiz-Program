#dictionry that stores answers
# have a variable that tracks
# loop through dictionary using the key value pairs
# display each question to the user and allow them to answer and if they are right or wrong 
#show the final result when quiz is completed

quiz = {
    "question1":
    {
        "question": "What does DeFi stand for?",
        "answer": "Decentralized Finance"
    },
    "question2":
    {
        "question": "Which blockchain is most commonly associated with DeFi projects?",
        "answer": "Ethereum"
    },
    "question3":
    {
        "question": "What is a smart contract?",
        "answer": "A self-executing contract with the terms of the agreement directly written into code"
    },
    "question4":
    {
        "question": "Name a popular DeFi lending platform.",
        "answer": "Aave or Compound"
    },
    "question5":
    {
        "question": "What is liquidity mining?",
        "answer": "Providing liquidity to a DeFi protocol and earning rewards in return"
    },
    "question6":
    {
        "question": "What is the role of a decentralized exchange (DEX)?",
        "answer": "To facilitate peer-to-peer trading of cryptocurrencies without a central authority"
    },
    "question7":
    {
        "question": "Name a popular decentralized exchange (DEX).",
        "answer": "Uniswap or SushiSwap"
    },
    "question8":
    {
        "question": "What is yield farming?",
        "answer": "The practice of staking or lending crypto assets to generate high returns or rewards"
    },
    "question9":
    {
        "question": "What is a stablecoin?",
        "answer": "A type of cryptocurrency that is pegged to a stable asset, like the US Dollar, to reduce volatility"
    },
    "question10":
    {
        "question": "What is impermanent loss?",
        "answer": "A temporary loss of funds experienced by liquidity providers due to volatility in a trading pair"
    }
}

score = 0

for key, value in quiz.items(): # loop through dictionary using the key value pairs
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score += 1
    else:
        print("That's incorrect!")
        print("Answer:", value['answer'])
        
    print("Current score:", score)
    print()  # Print a blank line for better readability between questions

print("Quiz completed! Your final score is:", score)
