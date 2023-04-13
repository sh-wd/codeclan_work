1.  SELECT * FROM movies;
id |                title                | year | show_time 
----+-------------------------------------+------+-----------
  1 | Iron Man                            | 2008 | 17:00
  2 | The Incredible Hulk                 | 2008 | 23:55
  3 | Iron Man 2                          | 2010 | 18:45
  4 | Thor                                | 2011 | 15:45
  5 | Captain America: The First Avenger  | 2011 | 14:15
  6 | Avengers Assemble                   | 2012 | 14:45
  7 | Iron Man 3                          | 2013 | 21:55
  8 | Thor: The Dark World                | 2013 | 22:55
  9 | Batman Begins                       | 2005 | 13:40
 10 | Captain America: The Winter Soldier | 2014 | 18:25
 11 | Guardians of the Galaxy             | 2014 | 13:10

 2. SELECT name FROM people;
          name         
----------------------
 Homer Simpson
 Marge Simpson
 Lisa Simpson
 Maggie Simpson
 Patty Bouvier
 Selma Bouvier
 Kent Brockman
 Ned Flanders
 Barney Gumble
 Itchy
 Eric Cartman
 
 3. UPDATE people SET name = 'Krusty the Clown' WHERE name = 'Crusty the Clown';
 UPDATE 1

 4. SELECT name FROM people WHERE name = 'Homer Simpson';
     name      
---------------
 Homer Simpson
(1 row)

5. DELETE FROM movies WHERE title = 'Batman Begins';
DELETE 1

6. marvel=# INSERT INTO people (name) VALUES ('Bart Simpson');
INSERT 0 1

7. marvel=# DELETE FROM people WHERE name = 'Eric Cartman';
DELETE 1

8. INSERT INTO movies (title, year, show_time) VALUES ('Avengers: Infinity War', 2018, '00:00');
INSERT 0 1

9. SELECT show_time FROM movies WHERE title = 'Iron Man 2';
 show_time 
-----------
 18:45
(1 row)

UPDATE movies SET show_time = '20:45' WHERE title = 'Iron Man 2';
UPDATE 1

Extension
DELETE FROM movies where year BETWEEN '2000' AND '2011';
DELETE 5

DELETE FROM movies WHERE title LIKE ‘Iron Man%’;