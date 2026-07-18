import argparse

from research_system import run_loop


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="dry-run")
    parser.add_argument("--max-iterations", type=int, default=1)
    args = parser.parse_args()
    run_loop(args.mode, args.max_iterations)
