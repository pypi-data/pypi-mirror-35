"""Contains a function to generate a summary of the battle."""

from datetime import datetime
from mario_battle.version import PYPI_NAME, VERBOSE_NAME


def generate_markdown_summary(battle_results):
    """Generates a Markdown summary of the battle to a file.

    Args:
        battle_results: A MarioBattle object.
    """
    file_path = (
        str(datetime.now().date())
        + "_"
        + PYPI_NAME
        + ".md")

    print("Saving summary to {}".format(file_path))

    with open(file_path, 'w') as f:
        # Print title
        print("# " + VERBOSE_NAME, file=f)
        print(file=f)

        # Print the game's stats
        print("## Battle Settings", file=f)

        print("Players:", file=f)
        print("+ " + battle_results.player1, file=f)
        print("+ " + battle_results.player2, file=f)
