"""Contains functions for displaying and retreiving info.

Does some processing, too. All using the command line, at present.
"""

from collections import OrderedDict
from time import time
from colorama import Fore, Style
from mario_battle.constants import (
    COURSE_DICTIONARY,
    MARIO_ASCII_ART,
    MAX_NAME_LENGTH,
    TIE,
)
from mario_battle.version import HOME_URL, VERBOSE_NAME


class NameEmptyError(Exception):
    """An exception for when the user leaves their name blank."""
    pass


class TooFewCoursesError(Exception):
    """An exception for when too few courses are selected."""
    pass


def print_courses(                    # pylint: disable=dangerous-default-value
        course_dict=COURSE_DICTIONARY,
        show_played=True):
    """Prints a set of Mario 64 courses.

    By default, this includes all of the courses, all listed as
    unplayed, if the course_dict argument isn't passed in.

    Args:
        course_dict: An optional dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            course number, what the name of the course is and whether it
            has already been played. Defaults to all courses, with all
            of them unplayed.
        show_played: An optional boolean specifying whether to show if a course
            was played or not. Defaults to True.
    """
    # Make sure the items are in order of course number
    course_dict = OrderedDict(sorted(course_dict.items()))

    # Print the courses
    for number, course_info in course_dict.items():
        # The course string to display
        course_string = "{number}\t".format(number=number)

        if show_played:
            course_string += "({played}) "

        course_string += "{name}".format(name=course_info['name'])

        # Dim the text if the course has already been played
        if course_info['played']:
            print(Style.DIM + course_string.format(played='x') + Style.RESET_ALL)
        else:
            print(course_string.format(played=' '))


def format_time(seconds):
    """Returns seconds as a formatted string.

    The format is "hours:minutes:seconds.millisecond".

    Arg:
        A float containing a number of seconds.

    Returns:
        A formatted string containing the time represented by the number
        of seconds passed in.
    """
    hours = seconds // 3600
    minutes = (seconds - (hours*3600)) // 60
    seconds = seconds - (hours*3600) - (minutes*60)
    time_elapsed = "{:02.0f}:{:02.0f}:{:06.3f}".format(hours, minutes, seconds)
    return time_elapsed


def display_welcome_message():
    """Displays a welcome message to the user."""
    print('-' * len(VERBOSE_NAME))
    print(Style.BRIGHT + VERBOSE_NAME + Style.RESET_ALL)
    print('-' * len(VERBOSE_NAME))
    print()
    print(MARIO_ASCII_ART)
    print("visit us at " + HOME_URL + "!")
    print()


def get_player_names():
    """Gets the player names from the user.

    Returns:
        A tuple of two strings, containing the player names.
    """
    while True:
        try:
            # Get the name
            player1 = input("Player 1: ")
            player1 = player1.strip()

            # Validate
            if not player1:
                raise NameEmptyError

            # Good
            break
        except NameEmptyError:
            print(Fore.RED
                  + "Hey you! Enter a non-blank name!"
                  + Style.RESET_ALL)

    while True:
        try:
            # Get the name
            player2 = input("Player 2: ")
            player2 = player2.strip()

            # Validate
            if not player2:
                raise NameEmptyError

            assert player2 != player1

            # Good
            break
        except NameEmptyError:
            print(Fore.RED
                  + "Hey you! Enter a non-blank name!"
                  + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yeesh! There can't be two {name}s!".format(name=player1)
                  + Style.RESET_ALL)

    # End the section with a new line
    print()

    return (player1, player2)


def get_number_of_rounds():
    """Gets the number of rounds from the user.

    The number of rounds must be odd and be no more than 15 (the number
    of courses in Mario 64).

    Returns:
        An integer specifying the number of rounds.
    """
    print("Select number of rounds (1 3 5 7 9 11 13 15):")

    while True:
        try:
            # Get the number of rounds
            number = input("> ")

            # Validate
            number = int(number)

            assert number in {1, 3, 5, 7, 9, 11, 13, 15}

            # All good
            break
        except ValueError:
            print(Fore.RED + "One integer only please!" + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yikes! Pick an allowed number of rounds!"
                  + Style.RESET_ALL)

    # Print a new line for the next section
    print()

    return number


def get_courses(min_number_of_courses):
    """Gets the courses to select from from the user.

    Arg:
        min_number_of_courses: An integer specifying the minimum number
            of courses that must be selected.

    Returns:
        A dictionary (following the schema of COURSE_DICTIONARY from
        constants.py) specifying for each course number, what the name
        of the course is and whether it has already been played. In this
        case, all the courses will be unplayed.
    """
    # The default set of courses
    DEFAULT_COURSE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    print("Select which courses are eligible to be played")
    print("(defaults to 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15):")
    print("--------------------------------------------------")
    print_courses(show_played=False)

    print()

    while True:
        try:
            # Get the courses to choose from
            course_numbers_string = input("> ")

            # Figure out whether to use the default courses
            if not course_numbers_string.strip():
                course_numbers = DEFAULT_COURSE_LIST
                break

            course_numbers = list(set(
                [int(i) for i in course_numbers_string.split()]))

            # Validate
            allowed_course_numbers = COURSE_DICTIONARY.keys()

            for course_number in course_numbers:
                assert course_number in allowed_course_numbers

            if len(course_numbers) < min_number_of_courses:
                raise TooFewCoursesError

            # We're good
            break
        except ValueError:
            print(Fore.RED + "Integers only please!" + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yikes! Pick an allowed course number!"
                  + Style.RESET_ALL)
        except TooFewCoursesError:
            print(Fore.RED
                  + "Hey! Pick at least {number} courses!".format(
                      number=min_number_of_courses)
                  + Style.RESET_ALL)

    # Print an empty line to end this section
    print()

    # Now filter which courses we want to include
    filtered_courses = {}

    for course_number in course_numbers:
        filtered_courses[course_number] = COURSE_DICTIONARY[course_number]

    return filtered_courses


def display_round_welcome_message(round_):
    """Displays a welcome message for the round.

    Arg:
        round_: An integer specifying the round number.
    """
    message = "ROUND {round_}".format(round_=round_)
    print()
    print('-' * len(message))
    print(Style.BRIGHT + message + Style.RESET_ALL)
    print('-' * len(message))
    print()


def get_course(course_selection, player, last_round=False):
    """Asks player which course they want to choose.

    If it's the last round, the players pick or ban collectively.

    Args:
        course_selection: A dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            selected course number, what the name of the course is and
            whether it has already been played.
        player: A string containing the name of the player who is
            selecting the course.
        last_round: An optional boolean specifying if it's the last
            round.

    Returns:
        A two-tuple containing an integer and a string. The integer
        specifies the course number and the string is the course name.
    """
    # Prompt the player to select a course
    if last_round:
        prompt_msg = (
            Style.BRIGHT
            + "Sudden death!"
            + Style.RESET_ALL
            + " Collectively choose an available course!")

        # Using len on prompt_msg gives incorrect results
        prompt_msg_length = len("Sudden death! "
                                "Collectively choose an available course!")
    else:
        prompt_msg = (Style.BRIGHT
                      + player
                      + Style.RESET_ALL
                      + "! Select an available course!")

        # Using len on prompt_msg gives incorrect results
        prompt_msg_length = len(player + "! Select an available course!")

    print(prompt_msg)
    print('-' * prompt_msg_length)
    print_courses(course_selection)
    print()

    # Get the input and validate
    while True:
        try:
            # Get the courses to choose from
            course_number_string = input("(choose a course number)\n> ")
            course_number = int(course_number_string)

            # Validate
            allowed_course_numbers = (
                [number for number, info in course_selection.items()
                 if not info['played']])
            assert course_number in allowed_course_numbers

            # We're good
            break
        except ValueError:
            print(Fore.RED + "Integers only please!" + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yikes! Pick an allowed course number!"
                  + Style.RESET_ALL)

    # End section with an empty line
    print()

    return (course_number, COURSE_DICTIONARY[course_number]['name'])


def time_player(player, course_name):
    """Times the user during their course run.

    Confirms with the user that the time stoppage was intentional

    Args:
        player: A string containing the player name.
        course_name: A string containing the course name.

    Returns:
        A float specifying the player's course time in seconds.
    """
    # Loop part of this function in case the player wants to reset
    while True:
        # Use this to break out of nested loops
        is_done = False

        # Tell the player it's their turn
        print(
            Style.BRIGHT
            + player
            + Style.RESET_ALL
            + ", it's your turn!")
        print()

        # Prompt to start
        while True:
            answer = input("Start run [y, ?]? ")

            if answer == "y":
                # Start!
                break
            else:
                # Print help
                print(Style.BRIGHT
                      + "y - start the run\n"
                      + "? - print help"
                      + Style.RESET_ALL)

        start_time = time()
        print()

        # Prompt to stop
        while True:
            answer = input("Finish run [y, p, r, t, ?]? ")

            if answer == "y":
                # Stop!
                is_done = True
                break
            elif answer == "p":
                # Pause!
                start_of_pause = time()

                # Prompt to unpause
                while True:
                    unpause_answer = input("Unpause [y, t, ?]? ")

                    if unpause_answer == "y":
                        # Unpause. Give the player back the paused time.
                        start_time += time() - start_of_pause
                        break
                    elif unpause_answer == "t":
                        print(format_time(start_of_pause - start_time))
                    else:
                        # Print help
                        print(Style.BRIGHT
                              + "y - unpause the run\n"
                              + "t - show elapsed time for the run\n"
                              + "? - print help"
                              + Style.RESET_ALL)
            elif answer == "r":
                # Reset!
                print("Resetting")
                print()
                break
            elif answer == "t":
                # Print elapsed time
                print(format_time(time() - start_time))
            else:
                # Print help
                print(Style.BRIGHT
                      + "y - finish the run\n"
                      + "p - pause the run\n"
                      + "r - reset the run\n"
                      + "t - show elapsed time for the run\n"
                      + "? - print help"
                      + Style.RESET_ALL)

        # Break out of the reset loop if we're truly done
        if is_done:
            break

    # Out of the loop. Print the player's time
    total_time = time() - start_time

    print()
    print(
        Style.BRIGHT
        + player
        + Style.RESET_ALL
        + "'s time for "
        + Style.BRIGHT
        + course_name
        + Style.RESET_ALL
        + ":")
    print(
        Style.BRIGHT
        + format_time(total_time)
        + Style.RESET_ALL)
    print()

    return total_time


def round_summary(this_round, mario_battle):
    """Print round summary.

    Summary includes current round times, overall player times, and
    updated score.

    Args:
        this_round: A Round object containing the round results.
        mario_battle: A MarioBattle object containing overall battle
            results.
    """
    # Title
    title = "ROUND {} SUMMARY".format(this_round.round_number)

    print('-' * len(title))
    print(Style.BRIGHT + title + Style.RESET_ALL)
    print('-' * len(title))
    print()

    # Round time
    print(
        Style.BRIGHT
        + this_round.course_name
        + " time"
        + Style.RESET_ALL)
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.winner,
        format_time(this_round.winner_time)))
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.loser,
        format_time(this_round.loser_time)))
    print()

    if this_round.was_tie:
        print(Style.BRIGHT
              + "Round {}: TIE".format(this_round.round_number)
              + Style.RESET_ALL)
    else:
        print(
            Style.BRIGHT
            + "{} won round {} by {}!".format(
                this_round.winner,
                this_round.round_number,
                format_time(this_round.loser_time - this_round.winner_time))
            + Style.RESET_ALL)

    print()

    # Total time
    print(Style.BRIGHT + "Total time" + Style.RESET_ALL)
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.winner,
        format_time(mario_battle.get_player_total_time(this_round.winner))))
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.loser,
        format_time(mario_battle.get_player_total_time(this_round.loser))))
    print()

    # Score
    print(Style.BRIGHT + "Score" + Style.RESET_ALL)
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.winner,
        mario_battle.get_player_score(this_round.winner)))
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        this_round.loser,
        mario_battle.get_player_score(this_round.loser)))
    print()


def final_summary(game_results):
    """Print final battle summary.

    Arg:
        game_results: A MarioBattle object containing the results of the game.
    """
    # Title
    title = "FINAL SUMMARY"

    print('-' * len(title))
    print(Style.BRIGHT + title + Style.RESET_ALL)
    print('-' * len(title))
    print()

    # Get winner and loser
    winner = game_results.get_winning_player()
    loser = game_results.get_losing_player()

    if winner == TIE:
        print(
            Style.BRIGHT
            + "A tie! Rejoice in your shared victory!"
            + Style.RESET_ALL)

        # Randomly assign winners and loser variables so we can use them
        # later
        winner = game_results.player1
        loser = game_results.player2
    else:
        print(
            Style.BRIGHT
            + "{} won {}!".format(winner, VERBOSE_NAME)
            + Style.RESET_ALL)

    # Final Score
    print()
    print(Style.BRIGHT + "Final Score" + Style.RESET_ALL)
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        winner,
        game_results.get_player_score(winner)))
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        loser,
        game_results.get_player_score(loser)))
    print()

    # Total time
    print(Style.BRIGHT + "Total time" + Style.RESET_ALL)
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        winner,
        format_time(game_results.get_player_total_time(winner))))
    print(("{:" + str(MAX_NAME_LENGTH) + "}\t{}").format(
        loser,
        format_time(game_results.get_player_total_time(loser))))
    print()
