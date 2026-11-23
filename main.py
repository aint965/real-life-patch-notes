import os
import sys

ENTRY = "v5.1.3: fixed a bug where the pinky toe detected furniture in the dark with 100% accuracy."


def validate_entry(text):
    if not text or not text.strip():
        return "entry must not be empty or only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be exactly one line"
    if len(text) > 160:
        return "entry is %d characters, over the 160-character limit" % len(text)
    return None


def main():
    error = validate_entry(ENTRY)
    if error is not None:
        sys.exit("invalid entry: " + error)
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
