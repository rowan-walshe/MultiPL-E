from pathlib import Path
from safe_subprocess import run
from generic_eval import main


LANG_NAME = "Ada"
LANG_EXT = ".adb"

def eval_script(path: Path):
    basename = ".".join(str(path).split(".")[:-1])
    build_result = run(["gnatmake", "-gnatW8", path, "-o", basename])
    if build_result.exit_code != 0:
        return {
            "status": "SyntaxError",
            "exit_code": build_result.exit_code,
            "stdout": build_result.stdout,
            "stderr": build_result.stderr,
        }

    status = "OK"
    run_result = run([basename])

    if run_result.timeout:
        status = "Timeout"
    elif run_result.exit_code != 0:
        status = "Exception"

    return {
        "status": status,
        "exit_code": run_result.exit_code,
        "stdout": run_result.stdout,
        "stderr": run_result.stderr,
    }


if __name__ == "__main__":
    main(eval_script, LANG_NAME, LANG_EXT)
