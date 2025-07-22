import random

# Step 1: Ask user their name
name = input("Welcome, agent. What's your name? ")

# Step 2-3: Create lists of adjectives and animals
adjectives = ["Sneaky", "Clever", "Silent", "Swift", "Brave", "Mysterious"]
animals = ["Otter", "Falcon", "Panther", "Fox", "Hawk", "Wolf"]

# Step 5: Randomly generate codename
codename = f"{random.choice(adjectives)} {random.choice(animals)}"

# Step 6: Randomly choose lucky number
lucky_number = random.randint(1, 99)

# Step 7: Display result
print(f"\nAgent {name}, your codename is: **{codename}**")
print(f"Your lucky number is: **{lucky_number}**")
