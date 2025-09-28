"""
Small utility helpers used by the agent.
"""

from typing import Tuple


def normalize_command(command: str) -> str:
    """
    Strip, collapse multiple spaces into one, and return the cleaned string.
    """
    if not isinstance(command, str):
        return ""
    return " ".join(command.strip().split())


def extract_prefix(command: str) -> Tuple[str, str]:
    """
    Split a command into (prefix, rest).
    Example:
      "summarize The quick brown" -> ("summarize", "The quick brown")
      "hello" -> ("hello", "")
    The prefix is lowercased.
    """
    n = normalize_command(command)
    if not n:
        return ("", "")
    parts = n.split(" ", 1)
    if len(parts) == 1:
        return (parts[0].lower(), "")
    return (parts[0].lower(), parts[1].strip())
 
