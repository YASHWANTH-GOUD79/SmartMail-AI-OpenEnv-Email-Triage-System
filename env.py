class EmailEnv:
    def __init__(self):
        self.current_task = "easy_task"
        self.text = ""
        self.truth = ""

    def reset(self, *, task_id=None):
        # 🔥 OpenEnv sends task_id here
        self.current_task = task_id
        
        if task_id == "easy_task":
            self.text = "Win a FREE iPhone now!!!"
            self.truth = "spam"

        elif task_id == "medium_task":
            self.text = "Meeting scheduled at 10 AM tomorrow"
            self.truth = "work"

        elif task_id == "hard_task":
            self.text = "Congratulations! You have been selected for an exclusive limited-time offer"
            self.truth = "spam"

        else:
            # fallback (important)
            self.text = "Hello"
            self.truth = "personal"

        return self.text

    def step(self, action):
        info = {"truth": self.truth}

        try:
            if self.current_task == "easy_task":
                from email_tasks.easy.grader import grade
                reward = grade(self.text, action, info)
            elif self.current_task == "medium_task":
                from email_tasks.medium.grader import grade
                reward = grade(self.text, action, info)
            elif self.current_task == "hard_task":
                from email_tasks.hard.grader import grade
                reward = grade(self.text, action, info)
            else:
                reward = 0.5
        except Exception as e:
            reward = 0.1

        done = True
        return "", float(reward), done, info
