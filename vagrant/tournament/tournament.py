#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

query_delete_match = "DELETE FROM Match"
query_delete_player = "DELETE FROM Player"
query_count_player = "SELECT Count(*) FROM Player"
query_insert_player = "INSERT INTO Player (Name) Values (%s)"
query_report_matches = "INSERT INTO Match (Winner_Player_ID,
Loser_Player_ID) Values (%s, %s)"
query_standing = "SELECT * FROM Standing"
query_matches = "SELECT * FROM Match"


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def non_return_query(conn, query, params=None):
    """Executing queries that has no return value"""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except Exception as e:
        print e
    finally:
        conn.close()


def return_query(conn, query, params=None):
    """Executing queries that has a return value"""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as e:
        print e
        return None
    finally:
        conn.close()


def deleteMatches():
    """Remove all the match records from the database."""
    non_return_query(connect(), query_delete_match)


def deletePlayers():
    """Remove all the player records from the database."""
    non_return_query(connect(), query_delete_player)


def countPlayers():
    """Returns the number of players currently registered."""
    return_value = return_query(connect(), query_count_player)
    return return_value[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    Args:
      name: the player's full name (need not be unique).
    """
    params = []
    params.append(bleach.clean(name))
    non_return_query(connect(), query_insert_player, params)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return return_query(connect(), query_standing)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    params = []
    params.append(winner)
    params.append(loser)
    non_return_query(connect(), query_report_matches, params)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    winners = standings[::2]
    losers = standings[1::2]
    if len(winners) > len(losers):
        winners = winners[-1]
    elif len(winners) < len(losers):
        losers = losers[-1]

    swiss_pair = []
    for _number in range(0, len(winners)):
        swiss_pair.append(
            (winners[0][0], winners[0][1], losers[0][0], losers[0][1]))

    return swiss_pair
