import random
import subprocess
from datetime import datetime

def update_file():
    """Appends a new line with the current timestamp and a random number to data.txt."""
    with open("data.txt", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_number = random.randint(1, 1000)
        f.write(f"Update at {now} with random number: {random_number}\\n")

def git_push():
    """Adds, commits, and pushes changes to the GitHub repository."""
    try:
        subprocess.run(["git", "add", "data.txt"], check=True)
        commit_message = f"Automated commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "--set-upstream", "origin", "main"], check=True)
        print("Successfully pushed changes to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the git process: {e}")
    except FileNotFoundError:
        print("Git command not found. Please ensure Git is installed and in your PATH.")

if __name__ == "__main__":
    update_file()
    git_push()
