from fastapi import FastAPI, Request
from env import EmailEnv
import yaml

app = FastAPI(title="SmartMail AI", version="1.0")

env = EmailEnv()

# Load task config once
try:
    with open("openenv.yaml", "r") as f:
        _config = yaml.safe_load(f)
except Exception:
    _config = {}

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/metadata")
def metadata():
    return {
        "name": _config.get("name", "SmartMail AI"),
        "description": _config.get("description", "Email classification environment using OpenEnv"),
    }

@app.get("/schema")
def schema():
    return {
        "action": {"type": "string", "description": "Email classification label"},
        "observation": {"type": "string", "description": "Email text content"},
        "state": {"type": "object", "description": "Current environment state"},
    }

@app.get("/state")
def state():
    return {
        "current_task": env.current_task,
        "text": env.text,
    }

@app.post("/reset")
async def reset(request: Request):
    try:
        body = await request.json()
        task_id = body.get("task_id") or body.get("task")
    except Exception:
        task_id = None

    obs = env.reset(task_id=task_id)
    return {"observation": obs}

@app.post("/step")
async def step(request: Request):
    try:
        action = await request.json()
    except Exception:
        action = {}

    act = action.get("action") or action.get("label") or "spam"

    obs, reward, done, info = env.step(act)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info,
    }

# 🔥 REQUIRED BY VALIDATOR
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

# 🔥 MUST EXIST
if __name__ == "__main__":
    main()
