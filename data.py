DATA = [
    # EASY (spam vs not spam)
    {"text": "Congratulations! You won a $1000 gift card. Click now!", "label": "spam", "priority": "low"},
    {"text": "Your bank account needs urgent verification", "label": "spam", "priority": "high"},
    {"text": "Team meeting scheduled at 3 PM today", "label": "work", "priority": "high"},
    {"text": "Lunch tomorrow?", "label": "personal", "priority": "low"},

    # MEDIUM (multi-class classification)
    {"text": "Submit the project report before deadline", "label": "work", "priority": "high"},
    {"text": "Limited time offer! Buy now and save big", "label": "spam", "priority": "low"},
    {"text": "Happy anniversary! Have a great day!", "label": "personal", "priority": "low"},
    {"text": "Client meeting rescheduled to Monday", "label": "work", "priority": "high"},

    # HARD (intent + priority)
    {"text": "URGENT: Server is down. Fix immediately!", "label": "work", "priority": "high"},
    {"text": "Reminder: Pay electricity bill today", "label": "personal", "priority": "high"},
    {"text": "Win cash prizes instantly by registering here", "label": "spam", "priority": "low"},
    {"text": "Please review the attached document and respond ASAP", "label": "work", "priority": "high"},

    # EDGE CASES (for better scoring)
    {"text": "Hey bro, send me the notes ASAP", "label": "personal", "priority": "high"},
    {"text": "Security alert: suspicious login detected", "label": "work", "priority": "high"},
    {"text": "Cheap medicines available online!!!", "label": "spam", "priority": "low"},
    {"text": "Let's catch up this weekend", "label": "personal", "priority": "low"}
]
DATA = [
    {"text": "Hello", "label": "work", "priority": "low"}
]