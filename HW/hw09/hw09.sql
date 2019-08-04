create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select dogs.name as name, sizes.size as size from dogs, sizes where dogs.height <= sizes.max and dogs.height > sizes.min;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select child from parents, dogs where parents.parent = dogs.name order by -height;


-- Sentences about siblings that are the same size
create table sentences as
  with 
    siblings(first, second) as (
      select a.child, b.child from parents as a, parents as b where a.parent = b.parent and a.child < b.child
      )
  select first || " and " || second || " are " || s1.size || " siblings" from siblings, size_of_dogs as s1, size_of_dogs as s2 where first = s1.name and second = s2.name and s1.size = s2.size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with 
    helper(list, last_dog, n, height) as (
      select d1.name || ", " || d2.name, d2.name, 2, d2.height + d1.height from dogs as d1, dogs as d2 where d1.height < d2.height union
      select list || ", " || d2.name, d2.name, n+1, helper.height + d2.height from dogs as d1, dogs as d2, helper where last_dog = d1.name and d1.height < d2.height
      )
select list, height from helper where height >= 170 and n = 4 order by helper.height;


create table tallest as
select max(height), name from dogs group by height/10 having count(*)>1;


-- All non-parent relations ordered by height difference
create table non_parents as
  with 
    grand(grandchild, height1, grandparent, height2) as (
      select a.child, c.height, b.parent, d.height from parents as a, parents as b, dogs as c, dogs as d where a.parent = b.child and c.name = a.child and d.name=b.parent

  ),
    great(great1, height1, great2, height2) as (
      select parent, height, grandchild, height2 from grand, parents, dogs where dogs.name = parent and child = grandparent
),
    together(dog1, height1, dog2, height2) as (
      select * from grand union
      select grandparent, height2, grandchild, height1 from grand union
      select * from great union
      select great2, height2, great1, height1 from great
      )
select dog1, dog2 from together;
