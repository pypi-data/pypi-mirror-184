import json
import os
import re
import subprocess


def main():
    programs = get_program_to_id()
    print("Programs:")
    for name, id in programs.items():
        print(f"{name}: {id}")


def get_program_to_id():
    raise ValueError("Good idea at first but not any more")
    root = get_root()
    pids = dir_to_pids(f"{root}/target/deploy")
    return pids


def dir_to_pids(dir: str):
    program_to_id = {}
    for filename in os.listdir(dir):
        match = re.search(r"([a-z_]+)-keypair.json", filename)
        if match is None:
            continue
        program = match.groups()[0]
        program_to_id[program] = run(f"solana-keygen pubkey {dir}/{filename}")
    return program_to_id


def run(cmd, debug=False):
    if debug:
        print(cmd)
    res = subprocess.check_output(cmd, shell=True).strip().decode("utf-8")
    if debug:
        print(res)
    return res


def get_root() -> str:
    return run("git rev-parse --show-toplevel")


if __name__ == "__main__":
    main()
