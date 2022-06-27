from typing import List

from wcwidth import wcswidth
from prompt_tookit.style import Style
from noneprompt import Choice, ListPrompt

from .emoji import emojis


def main():
    default_style = Style.from_dict(
        {
            "questionmark": "fg:#673AB7 bold",
            "question": "",
            "sign": "",
            "unsign": "",
            "selected": "",
            "pointer": "bold",
            "annotation": "",
            "answer": "bold",
        }
    )

    src_choices: List[Choice[str]] = [
        Choice(
            f"{emoji.emoji}{' '*(4-wcswidth(emoji.emoji))}- {emoji.description}",
            emoji.name,
        )
        for emoji in emojis
    ]
    print(
        ListPrompt("Where to store the plugin?", src_choices)
        .prompt(style=default_style)
        .data
    )