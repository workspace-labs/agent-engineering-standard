import argparse
from pathlib import Path
import tomllib


def main():
    parser = argparse.ArgumentParser(description="Print a report heading.")
    parser.add_argument("settings", type=Path)
    arguments = parser.parse_args()
    with arguments.settings.open("rb") as settings_file:
        report = tomllib.load(settings_file)["report"]
    print(report["title"])


if __name__ == "__main__":
    main()
