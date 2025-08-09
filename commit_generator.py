import random
import datetime
import time

def generate_commit_message():
    """Generates a descriptive and interesting commit message."""
    actions = ["feat", "fix", "docs", "style", "refactor", "test", "chore"]
    subjects = [
        "add new feature",
        "resolve bug",
        "update documentation",
        "format code",
        "refactor code",
        "add tests",
        "update build scripts",
        "update syntax",
        "small debug",
        "idk fixed",
        "working on ts"
    ]
    return f"{random.choice(actions)}: {random.choice(subjects)}"

def main():
    """Generates a commit message and updates a file."""
    commit_message = generate_commit_message()
    print(f"Generated commit message: {commit_message}")

    with open("data.txt", "a") as f:
        f.write(f"Update from commit_generator.py at {datetime.datetime.now()}\\n")

if __name__ == "__main__":
    i = 0
    while True:
        main()
        time.sleep(5)
        i+=1
        if i > 20:
            break