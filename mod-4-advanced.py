'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

"""
Sample data for Relationship Status below:
"""

social_graph = {
    "@jheadmd": {
        "first_name": "Jhea",
        "last_name": "Delgado",
        "following": ["@katlyn", "@frannyc", "@sofhieee"],
    },
    "@katlyn": {
        "first_name": "Katlyn",
        "last_name": "Cua",
        "following": ["@jheadmd", "@frannyc"],
    },
    "@sofhieee": {
        "first_name": "Sofhia",
        "last_name": "Chan",
        "following": ["@katlyn", "@jheadmd", "@alexandra", "@frannyc"],
    },
    "@frannyc": {
        "first_name": "Franny",
        "last_name": "Cutaran",
        "following": [
            "@jheadmd",
            "@sofhieee",
            "@alexandra",
        ],
    },
    "@alexandra": {
        "first_name": "Alexandra",
        "last_name": "Jabez",
        "following": [
            "@franny",
        ],
    },
}


def relationship_status(from_member, to_member, social_graph):
    """Relationship Status.
    15 points.


    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.


    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.


    This function describes the relationship that two users have with each other.


    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.


    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data


    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    """
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    follower = False
    followed = False
    from_member_following = social_graph.get(from_member).get("following")
    to_member_following = social_graph.get(to_member).get("following")

    if to_member in from_member_following:
        follower = True
    if from_member in to_member_following:
        followed = True

    if follower and followed:
        return "friends"
    elif follower and not followed:
        return "follower"
    elif not follower and followed:
        return "followed"
    else:
        return "no relationship"


from_member = str(input("Person 1: "))
to_member = str(input("Person 2: "))

print(relationship_status(from_member, to_member, social_graph))

board1 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board2 = [["O", "X", "X"],
          ["X", "O", "X"],
          ["O", "O", "X"],
          ]

board3 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board4 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board5 = [["X", "X", "O"],
          ["O", "O", "X"],
          ["X", "O", "X"],
          ]

board6 = [["O", "O", "O"],
          ["O", "X", "O"],
          ["O", "O", "X"],
          ]


def tic_tac_toe(board):
    '''Tic Tac Toe.
    15 points.


    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.


    This function evaluates a tic tac toe board and returns the winner.


    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.


    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists


    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if all(not row for row in board):
        return "NO WINNER"
    
    for row in board:
        if all(x == row[0] for x in row):
            return row[0]

    for col in range(len(board)):
        if all(board[i][col] == board[0][col] for i in range(len(board))):
            return board[0][col]

    if all(board[i][i] == board[0][0] for i in range(len(board))):
        return board[0][0]
    if all(board[i][len(board) - i - 1] == board[0][len(board) - 1] for i in range(len(board))):
        return board[0][len(board) - 1]

    return "NO WINNER"


winner = tic_tac_toe(board2)
print(winner)

legs = {
    ("upd", "admu"): {"travel time mins": 10},
    ("admu", "dlsu"): {"travel time mins": 35},
    ("dlsu", "upd"): {"travel time mins": 55},
}


def eta(first_stop, second_stop, route_map):
    '''ETA.
    20 points.


    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.


    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.


    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.


    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes


    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # return legs.get((from_place, to_place)).get("travel time mins")
    return route_map[(first_stop, second_stop)].get("travel time mins")


from_place = str(input("From: "))
to_place = str(input("To: "))
print(eta(from_place, to_place, legs), "mins")
