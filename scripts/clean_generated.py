import argparse

from research_system import clean_generated


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--yes", action="store_true", help="Actually remove generated bootstrap artifacts.")
    args = parser.parse_args()
    raise SystemExit(clean_generated(args.yes))
