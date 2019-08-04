-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table california as 
  select s2, s1 from adjacencies where s2 = "CA";

-- Finds lengths of possible paths between two states
create table distances as
  with
    distance(start, end, hops) as (
      select a.s1 as start, a.s2 as end, 1 as hops
       from adjacencies as a, adjacencies as b union
      select a.s1 as start, d.end as end, hops + 1 as hops
       from adjacencies as a, distance as d where a.s2 = d.start and hops < 15
    )
  select * from distance;

create table three_hops as
  select start from distances where end = "CA" and hops = 3;
