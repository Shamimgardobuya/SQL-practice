student@student-ThinkPad-X250:~/Desktop$ sqlite3 flight.sql
SQLite version 3.31.1 2020-01-27 19:55:54
Enter ".help" for usage hints.
sqlite> CREATE TABLE flights(
   ...>   id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>   origin TEXT NOT NULL,
   ...>   destination TEXT NOT NULL,
   ...>   duration INTEGER NOT NULL
   ...> );
sqlite> .tables
flights
sqlite> SELECT * FROM flights;
sqlite> INSERT INTO (origin,destination,duration) VALUES("Nairobi","Bungoma",400);
Error: near "(": syntax error
sqlite> INSERT INTO (origin,destination,duration):VALUES("Nairobi","Bungoma",400);
Error: near "(": syntax error
sqlite> INSERT INTO (origin,destination,duration) VALUES ("Nairobi","Bungoma", 400);
Error: near "(": syntax error
sqlite> INSERT INTO (origin,destination,duration):VALUES("Nairobi", "Bungoma", 400);
Error: near "(": syntax error
sqlite> INSERT INTO (origin,destination,duration) VALUES ("Nairobi","Bungoma", 400);
Error: near "(": syntax error
sqlite> INSERT INTO flights (origin,destination,duration) VALUES ("Nairobi","Bungoma",400);
sqlite> SELECT * FROM flights;
1|Nairobi|Bungoma|400
sqlite> INSERT INTO flights (origin,destination,duration) VALUES ("Mbagathi","Dubai",800);
sqlite> INSERT INTO flights (origin,destination,duration) VALUES ("Johannesburg","Dubai",495);
sqlite> INSERT INTO flights (origin,destination,duration) VALUES ("Bungoma","Nairobi",15);
sqlite> SELECT * FROM flights;
1|Nairobi|Bungoma|400
2|Mbagathi|Dubai|800
3|Johannesburg|Dubai|495
4|Bungoma|Nairobi|15
sqlite> .mode columns
sqlite> .headers yes
sqlite> SELECT * FROM flights;
id          origin      destination  duration  
----------  ----------  -----------  ----------
1           Nairobi     Bungoma      400       
2           Mbagathi    Dubai        800       
3           Johannesbu  Dubai        495       
4           Bungoma     Nairobi      15        
sqlite> SELECT FROM flights WHERE origin="Bungaonm";
Error: near "FROM": syntax error
sqlite> SELECT FROM flights WHERE origin="Bungoma";
Error: near "FROM": syntax error
sqlite> SELECT * FROM flights WHERE origin="Bungoma";
id          origin      destination  duration  
----------  ----------  -----------  ----------
4           Bungoma     Nairobi      15        
sqlite> SELECT * FROM flights WHERE duration>500;
id          origin      destination  duration  
----------  ----------  -----------  ----------
2           Mbagathi    Dubai        800       
sqlite> SELECT * FROM flights WHERE duration>500+1;
id          origin      destination  duration  
----------  ----------  -----------  ----------
2           Mbagathi    Dubai        800       
sqlite> SELECT * FROM flights WHERE duration>500+800;
sqlite> SELECT * FROM flights WHERE duration>500;
id          origin      destination  duration  
----------  ----------  -----------  ----------
2           Mbagathi    Dubai        800       
sqlite> SELECT * FROM flights WHERE duration>200 AND destination=='Dubai';
id          origin      destination  duration  
----------  ----------  -----------  ----------
2           Mbagathi    Dubai        800       
3           Johannesbu  Dubai        495       
sqlite> SELECT * FROM flights WHERE origin LIKE "%a%";
id          origin      destination  duration  
----------  ----------  -----------  ----------
1           Nairobi     Bungoma      400       
2           Mbagathi    Dubai        800       
3           Johannesbu  Dubai        495       
4           Bungoma     Nairobi      15        
sqlite> ^Z
[1]+  Stopped                 sqlite3 flight.sql
