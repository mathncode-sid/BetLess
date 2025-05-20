import json
import os

DATA_FILE = "data/scores.json"

def load_scores():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_scores(scores):
    with open(DATA_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def update_score(username, result_type):
    scores = load_scores()
    change = {"positive": 10, "neutral": 0, "negative": -15}.get(result_type, 0)
    if username not in scores:
        scores[username] = 0
    scores[username] += change
    save_scores(scores)

def get_leaderboard():
    scores = load_scores()
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:5]
