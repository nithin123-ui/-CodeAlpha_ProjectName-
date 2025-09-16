import re
import argparse
import sys
from pathlib import Path

DEFAULT_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def extract_emails_from_text(text, pattern=DEFAULT_PATTERN):
    """Return a sorted list of unique emails found in text."""
    matches = re.findall(pattern, text, re.IGNORECASE)
    return sorted(set(matches))

def main():
    parser = argparse.ArgumentParser(description="Extract email addresses from a text file.")
    parser.add_argument("input", nargs="?", default="input.txt", help="Input text file (default: input.txt)")
    parser.add_argument("output", nargs="?", default="emails.txt", help="Output file for emails (default: emails.txt)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    if not in_path.exists():
        print(f"Input file not found: {in_path}", file=sys.stderr)
        sys.exit(1)

    # Read file
    text = in_path.read_text(encoding="utf-8")

    # Extract emails
    emails = extract_emails_from_text(text)

    # Write results
    out_path.write_text("\n".join(emails), encoding="utf-8")

    print(f" Extracted {len(emails)} unique emails and saved to '{out_path}'")

if __name__ == "__main__":
    main()
