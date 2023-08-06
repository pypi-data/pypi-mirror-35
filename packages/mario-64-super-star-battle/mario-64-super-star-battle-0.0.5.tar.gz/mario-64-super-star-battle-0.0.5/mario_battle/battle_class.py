"""Contains an object to keep track of battle results."""

import random
from mario_battle.constants import TIE


class MarioBattle:
    """Class to store battle results.

    Attributes:
        player1: A string containing the name of the first player.
        player2: A string containing the name of the second player.
        player1_score: An integer specifying the score of the first
            player.
        player2_score: An integer specifying the score of the second
            player.
        player1_total_time: A float specifying the total time (in
            seconds) taken by the first player.
        player2_total_time: A float specifying the total time (in
            seconds) taken by the second player.
        courses: A dictionary containing the courses that are eligible
            to be played. This, following the schema of
            COURSE_DICTIONARY from constants.py, specified for each
            course number, what the name of the course is and whether it
            has already been played.
        num_rounds: An integer specifying the total number of rounds.
        results: A list containing Round objects representing the
            results of each round.
    """
    def __init__(self, player1, player2, courses, num_rounds):
        """Initialize the battle.

        Initialize player names, number of rounds, and the courses chosen to play.

        Args:
            player1: A string containing the name of the first player.
            player2: A string containing the name of the second player.
            courses: A dictionary (following the schema of
                COURSE_DICTIONARY from constants.py) specifying for each
                selected course number, what the name of the course is
                and whether it has already been played.
            num_rounds: An integer specifying the total number of rounds.
        """
        self.player1 = random.choice([player1, player2])
        self.player2 = player2 if self.player1 == player1 else player1
        self.player1_score = 0
        self.player2_score = 0
        self.player1_total_time = 0
        self.player2_total_time = 0
        self.courses = courses
        self.num_rounds = num_rounds
        self.results = []

    def get_winning_player(self):
        """Returns the player in the lead.

        Returns:
            A string containing the winning player's name, or
            constants.TIE if it's currently a tie.
        """
        if self.player1_score == self.player2_score:
            return TIE
        elif self.player1_score > self.player2_score:
            return self.player1
        return self.player2

    def get_losing_player(self):
        """Returns the player not in the lead.

        Returns:
            A string containing the losing player's name, or
            constants.TIE if it's currently a tie.
        """
        if self.player1_score == self.player2_score:
            return TIE
        elif self.player1_score < self.player2_score:
            return self.player1
        return self.player2

    def get_player_score(self, player_name):
        """Returns the score of a player.

        Arg:
            player_name: A string containing the player name to get
                the score for.

        Returns:
            An integer specifying the player's score.
        """
        if player_name == self.player1:
            return self.player1_score

        return self.player2_score

    def get_player_total_time(self, player_name):
        """Returns the total time of a player.

        Arg:
            player_name: A string containing the player name to get
                the time for.

        Returns:
            A float specifying the player's total time.
        """
        if player_name == self.player1:
            return self.player1_total_time

        return self.player2_total_time

    def get_players(self, round_):
        """Returns players in order of whose turn it is.

        The players alternate being the first and second player.

        Arg:
            round_: An integer specifying which round it is.

        Returns:
            A tuple of two strings, containing the first and second
            players' names.
        """
        # Alternate first player every round
        if round_ % 2 == 1:
            return (self.player1, self.player2)
        return (self.player2, self.player1)

    def post_results(self, post_dict):
        """Stores round results into results list and updates total times.

        Arg:
            post_dict: A dictionary specifying the results of the round.
                For example,

                {'round': 1,
                 'course': 5,
                 'times': {'Matt': 420.69,
                           'Branko': 69.420}}

        Returns:
            A Round object representing the results of the round.
        """
        # Determine the winner and loser
        winner = min(post_dict["times"], key=post_dict["times"].get)
        loser = max(post_dict["times"], key=post_dict["times"].get)

        # Determine whether the round was a tie
        is_tie = bool(
            post_dict["times"][winner] == post_dict["times"][loser])

        # Record the results
        this_round = Round(
            winner=winner,
            loser=loser,
            winner_time=post_dict["times"][winner],
            loser_time=post_dict["times"][loser],
            course_name=(
                self.courses[post_dict["course"]]["name"]),
            round_number=post_dict["round"],
            was_tie=is_tie)

        self.results.append(this_round)

        # Update the total time
        self.update_total_times(post_dict["times"])

        # Update the players' scores
        self.update_scores(post_dict["times"])

        # Mark the course just played as played
        self.courses[post_dict["course"]]["played"] = True

        # Return the Round object
        return this_round

    def update_scores(self, times):
        """Update the players' scores after a round.

        Arg:
            times: A dictionary containing the round times of the
                players. For example,

                 {'times': {'Matt': 69.420,
                            'Branko': 420.69}}
        """
        if times[self.player1] < times[self.player2]:
            self.player1_score += 1
        elif times[self.player1] > times[self.player2]:
            self.player2_score += 1
        else:
            # Tie!
            pass

    def update_total_times(self, times):
        """Add round times to the total times.

        Arg:
            times: A dictionary containing the round times of the
                players. For example,

                 {'times': {'Matt': 69.420,
                            'Branko': 420.69}}
        """
        self.player1_total_time += times[self.player1]
        self.player2_total_time += times[self.player2]


class Round:
    """Class to store battle results.

    Attributes:
        winner: A string containing the name of the player who won the
            round.
        loser: A string containing the name of the player who lost the
            round.
        winner_time: A float specifying the number of seconds taken by
            the winner.
        loser_time: A float specifying the number of seconds taken by
            the loser.
        course_name: A string containing the name of the course.
        round_number: An integer specifying which around it is.
        was_tie: A boolean specifying whether the round was a tie.
    """
    def __init__(
            self,
            winner,
            loser,
            winner_time,
            loser_time,
            course_name,
            round_number,
            was_tie=False):
        """Store the round information.

        Args:
            winner: A string containing the name of the player who won
                the round.
            loser: A string containing the name of the player who lost
                the round.
            winner_time: A float specifying the number of seconds taken
                by the winner.
            loser_time: A float specifying the number of seconds taken
                by the loser.
            course_name: A string containing the name of the course.
            round_number: An integer specifying which around it is.
            was_tie: An optional boolean specifying whether the round
                was a tie. Defaults to False.
        """
        self.winner = winner
        self.loser = loser
        self.winner_time = winner_time
        self.loser_time = loser_time
        self.course_name = course_name
        self.round_number = round_number
        self.was_tie = was_tie
