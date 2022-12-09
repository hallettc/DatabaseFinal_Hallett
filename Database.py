import sqlite3
import pandas as pd
import os

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
os.remove('test.db')
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor


query = """
    CREATE TABLE Clinic(
    clinicNo INT NOT NULL UNIQUE 
        CHECK (clinicNo BETWEEN 0 and 999999),
    clinicName VARCHAR(100) NOT NULL ,
    clinicAddress VARCHAR(100) NOT NULL ,
    clinicTele VARCHAR(10) NOT NULL ,
    managerNo INT CHECK (managerNo BETWEEN 0 and 999999),
    PRIMARY KEY(clinicNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Staff(
    staffNo INT NOT NULL UNIQUE 
        CHECK (staffNo BETWEEN 0 and 999999),
    staffName VARCHAR(100) NOT NULL ,
    staffAddress VARCHAR(100) NOT NULL ,
    staffTele VARCHAR(10) NOT NULL ,
    staffDOB DATE NOT NULL 
        CHECK(staffDOB < CURRENT_DATE),
    position VARCHAR(100) NOT NULL ,
    salary DOUBLE PRECISION NOT NULL ,
    clinicNo INT NOT NULL 
        CHECK (clinicNo BETWEEN 0 and 999999),
    PRIMARY KEY(staffNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic 
    
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)



query = """
    CREATE TABLE Owner(
    ownerNo INT NOT NULL UNIQUE 
        CHECK (ownerNo BETWEEN 0 and 999999),
    ownerName VARCHAR(100) NOT NULL ,
    ownerAddress VARCHAR(100) NOT NULL ,
    ownerTele VARCHAR(10) NOT NULL ,
    clinicNo INT 
        CHECK (clinicNo BETWEEN 0 and 999999),
    FOREIGN KEY (clinicNo) REFERENCES Clinic ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY(ownerNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Pet(
    petNo INT NOT NULL UNIQUE 
        CHECK (petNo BETWEEN 0 and 999999),
    petName VARCHAR(100) NOT NULL ,
    petDOB DATE NOT NULL 
        CHECK(petDOB < CURRENT_DATE),
    species VARCHAR(100) NOT NULL ,
    breed VARCHAR(100) NOT NULL ,
    color VARCHAR(100) NOT NULL ,
    ownerNo INT NOT NULL 
        CHECK (ownerNo BETWEEN 0 and 999999),
    clinicNo INT
        CHECK (clinicNo BETWEEN 0 and 999999),
    FOREIGN KEY (ownerNo) REFERENCES Owner ON DELETE NO ACTION ON UPDATE CASCADE,
    FOREIGN KEY (clinicNo) REFERENCES Clinic ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY(petNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

query = """
    CREATE TABLE Exam(
    examNo INT NOT NULL UNIQUE 
        CHECK (examNo BETWEEN 0 and 999999),
    complaint VARCHAR(250) NOT NULL ,
    description VARCHAR(250) NOT NULL ,
    dateSeen DATE NOT NULL ,
    actions VARCHAR(250) NOT NULL ,
    petNo INT NOT NULL 
        CHECK (petNo BETWEEN 0 and 999999),
    staffNo INT NOT NULL 
        CHECK (staffNo BETWEEN 0 and 999999),
    PRIMARY KEY(examNo),
    FOREIGN KEY (petNo) REFERENCES Pet ON DELETE NO ACTION ON UPDATE CASCADE
    FOREIGN KEY (staffNo) REFERENCES Staff ON DELETE NO ACTION ON UPDATE CASCADE
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# FILL CLINIC
query = """
    INSERT INTO Clinic
    VALUES (0001, "Happy Pets", "111 Pet Haven Rd. Miami, FL", "0019909807", NULL);
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic
    VALUES (0003, "Happy Dogs", "123 PetTopia Rd. Miami, FL", "1219880907", NULL);
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic
    VALUES (0040, "Happy Cats", "238 Purr Rd. Miami, FL", "0017899807", 3490);
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic
    VALUES (0006, "Happy Birds", "1111 Chirp Rd. Miami, FL", "0010949807", NULL);
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic
    VALUES (0011, "Happy Lizzards", "1121 Scale Rd. Miami, FL", "0019348807", 3456);
    """
cursor.execute(query)

# Select data
query = """
    SELECT *
    FROM Clinic
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print("\nClinic Table \n\n" , df)

# FILL STAFF
query = """
    INSERT INTO Staff
    VALUES (3456, "John Smith", "1249 Some St. Miami, FL", "0019009807", 20021023, "Manager", 99999, 0011);
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES (3490, "Jane Smith", "134 A St. Miami, FL", "0019068907", 20020921, "Manager", 99999, 0040);
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES (3426, "Sam Wang", "34 Long St. Miami, FL", "2367009807", 20011223, "Greeter", 38000, 0011);
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES (9087, "Sally Johannson", "145 Tongue St. Miami, FL", "0015890807", 19981013, "Trainer", 106000, 3456);
    """
cursor.execute(query)

query = """
    INSERT INTO Staff
    VALUES (2347, "Thomas France", "1 Short St. Miami, FL", "0019009807", 19610121, "Surgeon", 200000, 0011);
    """
cursor.execute(query)
# Select data
query = """
    SELECT *
    FROM Staff
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print("\nStaff Table \n\n" , df)

# FILL OWNER
query = """
    INSERT INTO Owner
    VALUES (3698, "Ankica Godric", "7966 Logan Road Miami, FL 33172", "0096709807", 0011);
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
    VALUES (9856, "Kamila Paulus", "958 S. Acacia Rd. Fort Lauderdale, FL 33334", "8956768907", 0040);
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
    VALUES (2348, "Savitr Valerius", "8724 Chapel St. North Miami Beach, FL 33160", "9987609807", 0011);
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
    VALUES (87349, "Sabīne Sherali", "9751 Whitemarsh Rd. Miami, FL 33161", "0745610807", 003);
    """
cursor.execute(query)

query = """
    INSERT INTO Owner
    VALUES (9855, "Kyōko Peace", "9906 E. Liberty Drive Hialeah, FL 33015", "0109689807", 6);
    """
cursor.execute(query)
# Select data
query = """
    SELECT *
    FROM Owner
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print("\nOwner Table \n\n" , df)
#print(df.columns)


# FILL Pet
query = """
    INSERT INTO Pet
    VALUES (7789, "Valentinas", 20170918, "DOG", "SHEEPADOODLE", "BLACK/BROWN", 3698, 11 );
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
    VALUES (0923, "Dionysius", 20160815, "DOG", "WHEATEN TERRIER", "TAN", 9856, 40);
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
    VALUES (9783, "Mattanyahu", 20100118, "RABBIT", "HOPPING", "WHITE", 2348, 11);
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
    VALUES (2234, "Iudris", 20190309, "BIRD", "PARROT", "RAINBOW", 87349, 3);
    """
cursor.execute(query)

query = """
    INSERT INTO Pet
    VALUES (2291, "Mina", 20210901, "CAT", "LION", "TAN", 9855, 6);
    """
cursor.execute(query)
# Select data
query = """
    SELECT *
    FROM Pet
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print("\nPet Table \n\n" , df)


# FILL EXAM
query = """
    INSERT INTO Exam
    VALUES (3346, "Biting", "Will not stop biting owner", 20221207, "Suggested relocating to Zoo",  2291, 9087);
    """
cursor.execute(query)

query = """
    INSERT INTO Exam
    VALUES (4467, "Fleas", "Constantly itchy", 20221206, "Bath, flea treatment",2234,  2347);
    """
cursor.execute(query)

query = """
    INSERT INTO Exam
    VALUES (3347, "Limping", "Fell off of a bed", 20221201, "Put in cast", 9783, 2347);
    """
cursor.execute(query)

query = """
    INSERT INTO Exam
    VALUES (9813, "Panting", "Seems constantly thirsty/hot", 20221203, "IV fluids", 923, 3490);
    """
cursor.execute(query)

query = """
    INSERT INTO Exam
    VALUES (4597, "Deaf?", "Not responding to audio/voices", 20221128, "Confirmed deaf, sent patient with literature", 7789, 3456);
    """
cursor.execute(query)
# Select data
query = """
    SELECT *
    FROM Exam
    """
cursor.execute(query)
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print("\nExam Table \n\n" , df)
# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
