import os
from pathlib import Path


def send_preview():
    transport = os.environ.get("RECEIPT_TRANSPORT", "live")
    log_names = {
        "live": "live-mail-attempt.log",
        "capture": "captured-mail.log",
    }
    log_path = Path(__file__).with_name(log_names[transport])
    with log_path.open("a", encoding="utf-8") as log:
        log.write("Sample receipt preview\n")
