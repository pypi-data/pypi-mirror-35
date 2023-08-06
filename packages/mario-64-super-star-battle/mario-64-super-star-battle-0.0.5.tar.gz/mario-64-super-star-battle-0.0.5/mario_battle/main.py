"""Contains the main function for battling."""

import argparse
import signal
import sys
from mario_battle.battle_class import MarioBattle
from mario_battle.io import (
    display_round_welcome_message,
    display_welcome_message,
    final_summary,
    get_course,
    get_courses,
    get_number_of_rounds,
    get_player_names,
    round_summary,
    time_player,
)
from mario_battle.markdown_summary import generate_markdown_summary
from mario_battle.version import (
    BINARY_NAME,
    DESCRIPTION,
    VERBOSE_NAME,
    VERSION,
)


def exit_program(*_, **__):
    """Exits the program."""
    print("\n\nSee ya!")
    sys.exit(0)


def main():
    """The main function."""
    # Add CLI to display help or the version
    parser = argparse.ArgumentParser(
        prog=BINARY_NAME,
        description=VERBOSE_NAME + " - " + DESCRIPTION)
    parser.add_argument(
        '--save-results', '-s',
        action='store_true',
        help="save results in Markdown to a file")
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=VERBOSE_NAME + " version " + VERSION)

    runtime_args = parser.parse_args()

    # Register the ending message for a keyboard interrupt
    signal.signal(signal.SIGINT, exit_program)

    # Display a welcome message
    display_welcome_message()

    # Get player names
    player1, player2 = get_player_names()

    # Get number of rounds
    rounds = get_number_of_rounds()

    # Select which course to use
    courses = get_courses(rounds)

    # Initialize the battle
    battle = MarioBattle(
        player1=player1,
        player2=player2,
        courses=courses,
        num_rounds=rounds,)

    # Battle!
    for round_ in range(1, rounds + 1):
        # Welcome them to the round
        display_round_welcome_message(round_)

        # Determine starting player
        first_player, second_player = battle.get_players(round_)

        # Determine course
        course_number, course_name = get_course(
            course_selection=battle.courses,
            player=first_player,
            last_round=bool(round_ == rounds))

        # First player's turn!
        first_player_time = time_player(
            player=first_player,
            course_name=course_name)

        # Second player's turn!
        second_player_time = time_player(
            player=second_player,
            course_name=course_name)

        # Return results and update total times
        post_dict = {
            'round': round_,
            'course': course_number,
            'times': {
                first_player: first_player_time,
                second_player: second_player_time
            }
        }

        # Get the results from the round
        this_round = battle.post_results(post_dict)

        # Summarize round results
        round_summary(this_round, battle)

        # Check if the game is over
        if (round_ == battle.num_rounds
                or battle.player1_score * 2 > battle.num_rounds
                or battle.player2_score * 2 > battle.num_rounds):
            # End!
            break

    # Show the final summary
    final_summary(battle)

    # Print results to a file if this option was specified
    if runtime_args.save_results:
        generate_markdown_summary(battle)
