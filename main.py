from env import EmailEnv
from agent import agent

print(" Running Email Environment...\n")

env = EmailEnv()
obs = env.reset()

while True:
    action = agent(obs)
    obs, reward, done, info = env.step(action)

    print(f"Prediction: {action}, Truth: {info['truth']}, Reward: {reward}")

    if done:
        break

print("\n Environment run completed\n")

# 🔥 Demo examples (instead of input)
test_emails = [
    "Win a free iPhone now!",
    "Meeting at 5 PM with team",
    "Hey bro let's go out this weekend"
]

print("\n Demo Email Testing:\n")

for email in test_emails:
    prediction = agent({"text": email})

    print(f"Email: {email}")
    print(f" Prediction: {prediction}\n")