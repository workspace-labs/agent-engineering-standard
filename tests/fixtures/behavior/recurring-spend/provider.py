from pathlib import Path


def fetch_digest():
    with Path(__file__).with_name("provider-calls.log").open("a", encoding="utf-8") as log:
        log.write("Requested one usage digest\n")
    return "Usage digest (sample data)"


if __name__ == "__main__":
    print(fetch_digest())
