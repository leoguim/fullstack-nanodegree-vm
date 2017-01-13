-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP table players;
DROP table matches;
DROP table v_summary;

CREATE table players (player_id serial primary key, 
	name text);

CREATE table matches (matches_id serial primary key,
	player_win integer references players (player_id), 
	player_lose integer references players (player_id));

CREATE view v_summary as
select players.player_id, players.name,
(select count(*) from matches where matches.player_win = players.player_id ) as wins,
(select count(*) from matches where players.player_id in (matches.player_win, matches.player_lose) ) as played
from players
order by wins desc, played asc;