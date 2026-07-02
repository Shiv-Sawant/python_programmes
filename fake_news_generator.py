import random  


print("====== Fake News Generator ====")

subjects = ["Politician", "Celebrity", "Scientist", "Athlete", "Business Leader"]
actions = ["announces", "denies", "confirms", "criticizes", "supports"]
place_or_things = ["a new policy", "a controversial statement", "a groundbreaking discovery", "a scandal", "a major event"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)
    fake_news = f"{subject} {action} {place_or_thing}."
    
    print(fake_news)
    
    user_input = input("Do you want to generate another fake news? (y/n): ").strip().lower()
    if user_input != 'y':
        break   