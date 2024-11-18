import json
import shutil

from typing import Dict, List
from pathlib import Path

def load_prompt_file(prompt_file: Path) -> List[Dict[str, str]]:
    """Given the path to a jsonl file of prompts, load the prompts into a list of dictionaries.
    The keys of each json object are: name, language, prompt, doctests, original, prompt_terminology, tests, stop_tokens
    Will also add the key "prompt_file" to each dictionary, which is the name of the file that the prompt was loaded from.
    """
    with open(prompt_file, "r") as f:
        prompts = [json.loads(line) for line in f]
    prompts = [{**prompt, "prompt_file": str(prompt_file)} for prompt in prompts]
    return prompts

def load_prompts(prompt_dir: Path) -> List[Dict[str, str]]:
    """Given the path to a dir that contains a number of jsonl files that contain
    prompts, load all the prompts into a list of dictionaries."""
    prompt_files = list(prompt_dir.glob("*.jsonl"))
    all_prompts = []
    for prompt_file in prompt_files:
        prompts = load_prompt_file(prompt_file)
        all_prompts.extend(prompts)
    return all_prompts

def clean_dir(output_dir: Path):
    """Given a directory, remove all files in the directory, or create it if needed."""
    shutil.rmtree(output_dir, ignore_errors=True)
    output_dir.mkdir(parents=True, exist_ok=True)

def save_prompt_code_to_file(prompt: Dict[str, str], output_dir: Path):
    """Given a prompt dictionary, save the prompt code to a file."""
    prompt_file = Path(prompt["prompt_file"])
    code_file = output_dir / (prompt_file.name + f"_{prompt['name']}.ada")
    prompt_code = prompt["prompt"] + "\n   is\n   begin\n      --  todo;" + prompt["tests"]
    with open(code_file, "w+") as f:
        f.write(prompt_code)

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent
    prompt_dir = project_root / "prompts"
    output_dir = project_root / "extracted_prompts"

    clean_dir(output_dir)
    prompts = load_prompts(prompt_dir)
    for prompt in prompts:
        save_prompt_code_to_file(prompt, output_dir)
