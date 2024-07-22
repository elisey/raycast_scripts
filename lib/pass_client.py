import subprocess


def get_pass(account: str) -> str:
    result = subprocess.run(['pass', account], stdout=subprocess.PIPE)
    return result.stdout.decode(encoding="UTF-8").strip()
