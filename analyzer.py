def detect_betting_transactions(statement_text):
    keywords = ['bet', 'sportpesa', 'odibets', '1xbet', 'betika', 'parlay', 'aviator', 'paripesa', 'stake']
    lines = statement_text.splitlines()
    betting_lines = [line for line in lines if any(k in line.lower() for k in keywords)]
    return betting_lines


def analyze_progress(betting_lines):
    if not betting_lines:
        return "✅ Great job! No betting activity detected.", "good"
    elif len(betting_lines) < 3:
        return "⚠️ You're doing better, but stay alert.", "partial"
    else:
        return "❌ Warning: You might be relapsing. Let’s work on this.", "chronic"
