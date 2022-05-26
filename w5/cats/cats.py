"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    list_res = list()
    for paragraph in paragraphs:
        if select(paragraph):
            list_res.append(paragraph)
    if k >= len(list_res):
        return ''
    return list_res[k]


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2
    for i in range(len(topic)):
        topic[i] = lower(topic[i])

    def select(paragraph):
        paragraph = lower(paragraph)
        for s in split(paragraph):
            if remove_punctuation(s) in topic:
                return True
        return False
    return select


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3
    counts = len(typed_words)
    if counts == 0:
        return 0.0
    count = 0
    for i in range(counts):
        if i < len(reference_words) and typed_words[i] == reference_words[i]:
            count += 1
        elif i == len(reference_words):
            break
    return count / counts * 100


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    return len(typed) * 12 / elapsed


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    if user_word in valid_words:
        return user_word
    min_diff = 999999999
    index = -1
    for i, valid_word in enumerate(valid_words):
        diff = diff_function(user_word, valid_word, limit)
        if min_diff > diff:
            min_diff = diff
            if diff <= limit:
                index = i
    if index == -1:
        return user_word
    return valid_words[index]


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # END PROBLEM 6
    def helper(start, goal, limit, diff):
        if len(start) == 0:
            return diff + len(goal)
        if len(goal) == 0:
            return diff + len(start)
        if diff > limit:
            return diff
        if start[0] != goal[0]:
            diff += 1
        return helper(start[1:], goal[1:], limit, diff)
    return helper(start, goal, limit, 0)


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    def helper(start, goal, limit, diff):
        if len(start) == 0 or len(goal) == 0:  # Fill in the condition
            # BEGIN
            "*** YOUR CODE HERE ***"
            return max(len(goal) + diff, len(start) + diff)
            # END

        elif start[0] == goal[0]:  # Feel free to remove or add additional cases
            # BEGIN
            "*** YOUR CODE HERE ***"
            return helper(start[1:], goal[1:], limit, diff)
            # END
        elif diff > limit:
            return diff
        else:
            diff += 1
            # Fill in these lines
            add_diff = helper(start, goal[1:], limit, diff)
            remove_diff = helper(start[1:], goal, limit, diff)
            substitute_diff = helper(start[1:], goal[1:], limit, diff)
            return min(add_diff, remove_diff, substitute_diff)
            # BEGIN
            "*** YOUR CODE HERE ***"
            # END
    return helper(start, goal, limit, 0)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8
    length = len(prompt)
    count = 0
    for i, x in enumerate(typed):
        if x == prompt[i]:
            count += 1
        else:
            break

    send({'id': user_id, 'progress': count/length})
    return count/length


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for i in range(len(times_per_player)):
        times.append([])
        for j in range(len(times_per_player[i]) - 1):
            times[i].append(times_per_player[i][j + 1] - times_per_player[i][j])

    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game))
                           )  # contains an *index* for each player
    # contains an *index* for each word
    word_indices = range(len(all_words(game)))
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    result = [[] for i in player_indices]
    for i in word_indices:
        min_time = time(game, 0, i)
        index = 0
        for j in player_indices:
            cur_time = time(game, j, i)
            if cur_time < min_time:
                min_time = cur_time
                index = j
        result[index].append(word_at(game, i))
    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]
               ), 'words should be a list of strings'
    assert all([type(t) == list for t in times]
               ), 'times should be a list of lists'
    assert all([isinstance(i, (int, float))
               for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]
               ), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    def select(p): return True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
