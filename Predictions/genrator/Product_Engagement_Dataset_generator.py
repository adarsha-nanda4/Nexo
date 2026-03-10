import pandas as pd
import numpy as np
import random
import uuid

# Configuration
NUM_ROWS = 20000
NUM_PRODUCTS = 300
NUM_SESSIONS = 5000

# Generate product IDs
product_ids = [f"P{str(i).zfill(4)}" for i in range(1, NUM_PRODUCTS + 1)]

# Generate session IDs
session_ids = [str(uuid.uuid4()) for _ in range(NUM_SESSIONS)]

data = []

for _ in range(NUM_ROWS):
    session_id = random.choice(session_ids)
    product_id = random.choice(product_ids)

    # Watch duration in seconds (realistic student behavior)
    watch_duration = np.random.exponential(scale=40)
    watch_duration = round(min(watch_duration, 300), 2)  # cap at 5 minutes

    data.append([session_id, product_id, watch_duration])

df1 = pd.DataFrame(data, columns=[
    "session_id",
    "product_id",
    "watch_duration"
])

df1.to_csv("/data/student_product_engagement.csv", index=False)

print("Dataset 1 generated successfully!")