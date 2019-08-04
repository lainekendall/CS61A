
-- Locations of each cafe
create table cafes as
  select "nefeli" as name, 2 as location union
  select "brewed"        , 8             union
  select "hummingbird"   , 6;

-- Menu items at each cafe
create table menus as
  select "nefeli" as cafe, "espresso" as item union
  select "nefeli"        , "bagels"           union
  select "brewed"        , "coffee"           union
  select "brewed"        , "bagels"           union
  select "brewed"        , "muffins"          union
  select "hummingbird"   , "muffins"          union
  select "hummingbird"   , "eggs";

-- All locations on the block
create table locations as
  with locations(n) as (
    select 1 union
    select n+1 from locations where n < 10
  )
  select * from locations;

-- Locations without a cafe
create table open_locations as
  select n from locations, cafes where n not in (select location from cafes) group by n;



  -- with all_spaces(n, l1, l2, l3) as (
  --   select n, a.location, b.location, c.location from locations, cafes as a, cafes as b, cafes as c where a.location != b.location and b.location != c.location and c.location != a.location group by n
  -- )
  -- select n from all_spaces where n <> l1 and n <> l2 and n <> l3;

-- select * from open_locations where n >= 5;
-- Expected output:
--   5
--   7
--   9
--   10

-- Items that could be placed on a menu at an open location
create table allowed as
  with item_locations(item, location) as (
    select item, location from cafes, menus where name = cafe
  ),
      not_allowed(n, list) as (
        select n, n || ", " || item from item_locations, locations where location-2 <= n and n <= location+2
    )
  select n, item from locations, menus where n || ", " || item not in (select list from not_allowed);

-- select * from allowed where n >= 5;
-- Expected output:
--   5|bagels
--   5|coffee
--   5|espresso
--   6|espresso
--   7|espresso
--   8|espresso
--   9|eggs
--   9|espresso
--   10|eggs
--   10|espresso

-- Open locations and their maximum-length menus
create table full as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

-- select n, items from full where n >= 5;
-- Expected output:
--   5|bagels, coffee, espresso
--   7|espresso
--   9|eggs, espresso
--   10|eggs, espresso

