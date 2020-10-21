CREATE TABLE Actors(
    FirstName VARCHAR(20),
    SecondName VARCHAR(20),
    Dob DATE,
    Gender ENUM('Male', 'Female', 'Transgender'),
    MaritalStatus ENUM('Married', 'Divorced', 'Single'),
    NetworthInMillions DECIMAL
);


CREATE TABLE New_Actors (
Id INT AUTO_INCREMENT,
FirstName VARCHAR(20) NOT NULL,
SecondName VARCHAR(20) NOT NULL,
DoB DATE NOT NULL,
Gender ENUM('MALE', 'Female', 'Transgender') NOT NULL,
MaritalStatus ENUM('Married', 'Divorced', 'Single', 'Unknown') DEFAULT "Unknown",
NetWorthInMillions DECIMAL NOT NULL,
PRIMARY KEY(Id)
);

CREATE TEMPORARY TABLE ActorName (FirstName CHAR(20));

-- insert into the sql file

INSERT INTO Actors(
    FirstName, 
    SecondName,
    DoB,
    Gender,
    MaritalStatus,
    NetWorthInMillions
) VALUES ("Brad", "Pitt", "1963-12-18", "Male", "Single", 240.00)



INSERT INTO Actors (
    FirstName, SecondName, DoB, Gender, MaritalStatus, NetWorthInMillions)
VALUES
("Jennifer", "Aniston", "1969-11-02", "Female", "Single", 240.00),
("Angelina", "Jolie", "1975-06-04", "Female", "Single", 100.00),
("Johnny", "Depp", "1963-06-09", "Male", "Single", 200.00);



INSERT INTO Actors 
VALUES (DEFAULT, "Dream", "Actress", "9999-01-01", "Female", "Single", 000.00);


INSERT INTO Actors SET DoB="1950-12-12", FirstName="Rajnikanth", SecondName="",  Gender="Male", NetWorthInMillions=50,  MaritalStatus="Married";

-- query the data

SELECT FirstName, SecondName, NetWorthInMillions FROM Actors ORDER BY NetWorthInMillions DESC LIMIT 3, 4;

-- delete the data

DELETE FROM Actors WHERE FirstName = "priyanka";

DELETE FROM Actors WHERE Gender = "Male";

DELETE FROM Actors ORDER by NetWorthInMillions DESC LIMIT 3;

DELETE FROM Actors;

-- delete all the data

TRUNCATE Actors;

-- update 

UPDATE Actors SET NetWorthInMillions = 1;

-- query
UPDATE Actors SET NetWorthInMillions = 5 ORDER BY FirstName LIMIT 3;



./DataJek/Lessons/15lesson.sh
USE MovieIndustry;


ALTER TABLE Actors CHANGE FirstName Frist_Name var(120);

ALTER TABLE Actors MODIFY Frist_Name varchar(20) DEFAULT "Anonymous";

ALTER TABLE Actors CHANGE First_Name First_Name varchar(20) DEFAULT "Anonymous";

ALTER TABLE Actors MODIFY First_Name INT;

ALTER TABLE Actors DROP MiddleName;

ALTER TABLE Actors ADD MiddleName varchar(100) FIRST;

ALTER TABLE Actors ADD MiddleName varchar(100) AFTER DoB;

ALTER TABLE Actors DROP MiddleName, ADD Middle_Name varchar(100);

ALTER TABLE Actors RENAME actors;

SELECT FirstName AS PopularName from Actors;

SELECT CONCAT(FirstName, ' ', SecondName) AS FullName FROM Actors;

SELECT COUNT(*) FROM Actors;

SELECT Gender, COUNT(*) FROM Actors GROUP BY Gender;

SELECT Gender FROM Actors GROUP BY Gender;

SELECT Gender FROM Actors GROUP BY Gender;

SELECT MaritalStatus, AVG(NetWorthInMillions) FROM Actors GROUP BY MaritalSTATUS order by MaritalStatus ASC;

SELECT Gender FROM Actors GROUP BY Gender;

SELECT MaritalStatus, AVG(NetWorthInMillions) AS NetWorthInMillions
FROM Actors
GROUP BY MaritalStatus
HAVING NetWorth > 450 OR NetWorth < 250;

SELECT MaritalStatus, AVG(NetWorthInMillions) AS NetWorth
FROM Actors
GROUP BY MaritalStatus
HAVING MaritalStatus = 'Married';


-- Join 

SELECT * FROM Actors a INNER JOIN Actors b;

-- Query 2

SELECT * FROM Actors a INNER JOIN Actors b USING (FirstName);

-- Query 3
SELECT * FROM Actors a INNER JOIN Actors b USING (NetWorthInMillions);

-- query
SELECT FirstName, SecondName, AssetType, URL 
FROM Actors
LEFT JOIN DigitalAssets
ON Actors.Id = DigitalAssets.ActorID;


-- Nested query
SELECT FirstName
FROM Actors 
WHERE (Id, MONTH(DoB), DAY(DoB))
IN ( SELECT ActorId, MONTH(LastUpdatedOn), DAY(LastUpdatedOn)
    FROM DigitalAssets);



