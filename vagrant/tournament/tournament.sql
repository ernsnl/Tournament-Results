-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP Database if exists tournament;

Create database tournament;

\connect tournament

Create Table Player(
  ID serial primary key,
  Name text
);

Create Table Match(
  ID serial primary key,
  Winner_Player_ID int,
  Loser_Player_ID int,
  Foreign Key(Winner_Player_ID) References Player(ID),
  Foreign Key(Loser_Player_ID) References Player(ID)
);

CREATE VIEW Standing AS
SELECT P.ID as Player_ID,
SELECT P.Name as Player_Name,
(SELECT count(*) FROM Match WHERE Match.Winner_Player_ID = P.ID) as Won,
(SELECT count(*) FROM Match WHERE P.ID in (Winner_Player_ID, Loser_Player_ID)) as Played
FROM Player as P
GROUP BY P.ID
ORDER BY Won DESC;
