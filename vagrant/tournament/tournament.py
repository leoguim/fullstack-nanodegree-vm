#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    DB = connect()
    cur = DB.cursor()
    cur.execute ("DELETE FROM matches")
    DB.commit()
    DB.close()


def deletePlayers():
    DB = connect()
    cur = DB.cursor()
    cur.execute ("DELETE FROM players")
    DB.commit()
    DB.close()

def countPlayers():
    DB = connect()
    cur = DB.cursor()
    cur.execute ("SELECT COUNT(player_id) from players")
    counts = cur.fetchone()
    return counts[0]
    DB.close()


def registerPlayer(name):
    DB = connect()
    cur = DB.cursor()
    cur.execute ("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    DB = connect()
    cur = DB.cursor()
    cur.execute("SELECT * FROM v_summary")
    record = cur.fetchall()
    DB.close()
    return record


def reportMatch(winner, loser):
    DB = connect()
    cur = DB.cursor()
    cur.execute ("INSERT INTO matches (player_win,player_lose) VALUES (%s, %s)", [winner,loser])
    DB.commit()
    DB.close()

 
def swissPairings():
    DB = connect()
    cur = DB.cursor()
    cur.execute ("SELECT * FROM v_summary")
    records = cur.fetchall()
    pairings = []
    num_players = len(records)
    for x in range (0, num_players-1, 2):
        pair = (records[x][0],records[x][1],records[x+1][0],records[x+1][1])
        pairings.append(pair)
    DB.close()
    return pairings
    


