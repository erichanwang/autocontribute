import subprocess
from datetime import datetime
import time
from commit_generator import generate_commit_message, main as update_file

def git_push():
    """Adds, commits, and pushes changes to the GitHub repository."""
    try:
        subprocess.run(["git", "add", "data.txt"], check=True)
        commit_message = generate_commit_message()
        print(f"Committing with message: {commit_message}")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "--set-upstream", "origin", "main"], check=True)
        print("Successfully pushed changes to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the git process: {e}")
    except FileNotFoundError:
        print("Git command not found. Please ensure Git is installed and in your PATH.")

if __name__ == "__main__":
    i = 0
    while True:
        update_file()
        git_push()
        print("Waiting for the next run...")
        time.sleep(5)  # Wait for 5 seconds before the next update
        i += 1
        if i > 20:
            break
