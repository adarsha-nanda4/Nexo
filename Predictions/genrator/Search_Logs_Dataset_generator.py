import pandas as pd
import numpy as np
import random
import uuid

NUM_ROWS = 20000
NUM_SESSIONS = 5000

session_ids = [str(uuid.uuid4()) for _ in range(NUM_SESSIONS)]

campus_keywords = [
    "DSA book", "COA notes", "second hand laptop", "hostel chair",
    "scientific calculator", "lab coat", "AI textbook",
    "cheap cycle", "room heater", "engineering drawing kit",
    "python programming book", "exam notes", "mini fridge",
    "power bank", "graphics card", "maths guide",
    "digital electronics book", "used monitor", "router",
    "backpack for college"
]

data = []

for _ in range(NUM_ROWS):
    session_id = random.choice(session_ids)
    searched_text = random.choice(campus_keywords)

    # Simulate page watch duration based on search type
    if "book" in searched_text or "notes" in searched_text:
        page_watch_duration = np.random.normal(loc=60, scale=20)
    elif "laptop" in searched_text or "graphics" in searched_text:
        page_watch_duration = np.random.normal(loc=90, scale=25)
    else:
        page_watch_duration = np.random.normal(loc=40, scale=15)

    page_watch_duration = max(5, round(page_watch_duration, 2))

    data.append([session_id, searched_text, page_watch_duration])

df2 = pd.DataFrame(data, columns=[
    "session_id",
    "searched_text",
    "page_watch_duration"
])

df2.to_csv("data/student_search_logs.csv", index=False)

print("Dataset 2 generated successfully!")