"""Check that your computer is ready for the course.

Run it from your project folder:
    python check_environment.py

Every line should say ok. A line that says FIX tells you what to do.
"""

import shutil
import subprocess
import sys

problems = 0

def report(passed, text, hint):
    global problems
    if passed:
        print(f"  ok   {text}")
    else:
        problems += 1
        print(f"  FIX  {text}")
        print(f"       {hint}")

def git_setting(name):
    result = subprocess.run(["git", "config", name], capture_output=True, text=True)
    return result.stdout.strip()

# 1. Python is new enough. The course's libraries need 3.12 or later.
version = sys.version_info
report(
    version >= (3, 12),
    f"Python {version.major}.{version.minor}.{version.micro}",
    "The course needs Python 3.12 or later. Install Python 3.14.",
)

# 2. A virtual environment is active. Inside one, sys.prefix is not the same as sys.base_prefix.
report(
    sys.prefix != sys.base_prefix,
    "a virtual environment is active",
    "Activate it: source .venv/bin/activate (Mac, Linux) or source .venv/Scripts/activate (Windows).",
)

# 3. Git is installed and knows who you are.
git_path = shutil.which("git")
report(git_path is not None, "Git is installed", "Install Git from git-scm.com.")
if git_path:
    user_name = git_setting("user.name")
    report(bool(user_name), "Git knows your name", 'Run: git config --global user.name "First Last"')
    user_email = git_setting("user.email")
    report(bool(user_email), "Git knows your email address", 'Run: git config --global user.email "you@example.com"')

print()
if problems:
    things = "thing" if problems == 1 else "things"
    print(f"{problems} {things} to fix. Run the script again when you are done.")
    sys.exit(1)
print("All done. Your computer is ready.")
