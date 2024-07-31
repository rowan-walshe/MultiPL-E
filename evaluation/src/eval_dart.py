from pathlib import Path
from safe_subprocess import run


def eval_script(path: Path):
    r = run(["dart", "analyze", "--no-fatal-warnings", str(path)], timeout_seconds=15)
    if r.exit_code != 0:
        return {
            "status": "SyntaxError",
            "exit_code": r.exit_code,
            "stdout": r.stdout,
            "stderr": r.stderr,
        }

    # todo: scrape for the various errors in stderr, stdout
    r = run(["dart", str(path)], timeout_seconds=15)
    if r.timeout:
        status = "Timeout"
    elif r.exit_code == 0:
        status = "OK"
    elif "ERR_ASSERTION" in r.stderr:
        status = "AssertionError"
    elif "SyntaxError" in r.stderr:
        status = "SyntaxError"
    elif "ReferenceError" in r.stderr:
        status = "ReferenceError"
    else:
        status = "Exception"
    return {
        "status": status,
        "exit_code": r.exit_code,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }
