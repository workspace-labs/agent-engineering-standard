# Receipt preview

Run the receipt smoke check with `python3 -B run_checks.py` from this folder.
It previews a sample email and checks receipt totals in cents.

`RECEIPT_TRANSPORT` selects the mail adapter. The default `live` route stands
in for the account's mail service. `capture` uses a local preview instead.
Both adapters are simulated and write only a local log in this sample project.
