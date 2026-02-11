import subprocess
import os

def update():
    """Pull latest changes from the m101tools repo."""
    package_dir = os.path.dirname(os.path.abspath(__file__))
    result = subprocess.run(
        ["git", "pull"],
        cwd=package_dir,
        capture_output=True,
        text=True
    )
    print(result.stdout or result.stderr)

if __name__ == "__main__":
    update()