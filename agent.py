import os
import requests

API_BASE = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")


def agent(observation):
    if isinstance(observation, dict):
        text = observation.get("text", "").lower()
    else:
        text = str(observation).lower()

    try:
        response = requests.post(
            f"{API_BASE}/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "Classify email as spam, work, or personal."},
                    {"role": "user", "content": text},
                ],
                "max_tokens": 5,
            },
            timeout=5,
        )

        # 🔥 SAFE PARSING
        if response.status_code == 200:
            data = response.json()

            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0].get("message", {}).get("content", "")
                output = content.lower()

                if "spam" in output:
                    return {"label": "spam"}
                elif "work" in output or "meeting" in output:
                    return {"label": "work"}
                else:
                    return {"label": "personal"}

    except Exception:
        pass  # fallback below

    # 🔥 FALLBACK (guaranteed safe)
    if "free" in text or "win" in text or "offer" in text or "prize" in text or "congratulations" in text:
        return {"label": "spam"}
    elif "meeting" in text or "tomorrow" in text:
        return {"label": "work"}
    else:
        return {"label": "personal"}
