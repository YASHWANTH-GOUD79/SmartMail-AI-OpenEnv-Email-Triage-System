def grade(observation, action, info):
    if info is None:
        info = {}
    truth = info.get("truth")
    
    if isinstance(action, dict):
        action = action.get("label", action.get("category", action.get("action", "")))

    if truth is None:
        return 0.1

    return 0.9 if action == truth else 0.1
