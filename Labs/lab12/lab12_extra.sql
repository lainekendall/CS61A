-- Requires the contents of file states.sql to be loaded first.
.read states.sql

-- Tables in states.sql:
--   states(state):       US States + DC - HI - AK
--   landlocked(state):   Table of landlocked (not adjacent to ocean) states
--   adjacencies(s1, s2): States that are adjacent to each other

create table alphabetical_paths as
with
  paths(s, n, last) as (
    select s1 || "," || s2 as s, 2 as n, s2 as last 
      from adjacencies where s1 < s2 union
    select p.s || "," || a.s2 as s, n + 1 as n, a.s2 as last from adjacencies as a, paths as p where p.last = a.s1 and p.last < a.s2
  )
select s from paths where n > 6 order by -n;

-- Lengths of possible paths between two states that enter only
-- landlocked states along the way.
create table inland_distances as
  with
    inland(start, end, hops) as (
      select a.s1 as start, a.s2 as end, 1 as hops
       from adjacencies as a, landlocked as l where a.s2 = l.state union
      select a.s1 as start, d.end as end, hops + 1 as hops
       from adjacencies as a, distance as d where a.s2 = d.start and hops < 10
    )
  -- REPLACE THIS LINE
  select "CA" as start, "WA" as end, 3 as hops;
