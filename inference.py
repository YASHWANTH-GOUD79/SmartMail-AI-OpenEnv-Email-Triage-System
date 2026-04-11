import yaml

def run_inference():
    print("[START]")

    from env import EmailEnv
    from agent import agent

    # Load tasks from openenv.yaml so the validator sees all 3 graded tasks
    try:
        with open("openenv.yaml", "r") as f:
            config = yaml.safe_load(f)
        task_ids = [t["id"] for t in config.get("tasks", [])]
    except Exception:
        task_ids = ["easy_task", "medium_task", "hard_task"]

    env = EmailEnv()
    total = 0.0
    steps = 0

    for task_id in task_ids:
        obs = env.reset(task_id=task_id)

        result = agent(obs)
        action = result.get("label", "spam")

        obs, reward, done, info = env.step(action)

        if reward is None:
            reward = 0.1

        reward = float(reward)

        if reward >= 1.0:
            reward = 0.99
        elif reward <= 0.0:
            reward = 0.01

        print(f"[STEP] task={task_id}, action={action}, reward={reward}")

        total += reward
        steps += 1

    print(f"[END] score={total / max(steps, 1)}")


if __name__ == "__main__":
    run_inference()
