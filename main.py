"""Write a one-sentence absurd invention pitch to /output/entry.txt."""

from pathlib import Path

PITCH = (
    "For the microwave that beeps until you come back, the Butler Rod is a "
    "six-metre telescopic brass arm that extends from the microwave and taps you "
    "politely on the shoulder in any room of the house."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
