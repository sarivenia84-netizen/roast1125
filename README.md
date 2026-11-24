# Roast Your Own Agent — Entry

A single-file Python 3.13 (stdlib only) entry that writes a self-roasting one-liner to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Run

```bash
mkdir -p /output
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
cat /output/entry.txt
```

Output: one UTF-8 line, 1–200 chars, no extra newlines.