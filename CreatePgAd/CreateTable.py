def createOwnersTable(cursor):
	cursor.execute("""
  					DROP TABLE IF EXISTS Owners CASCADE;
                    CREATE TABLE Owners(
	                    idOwner SERIAL PRIMARY KEY,
	                    emailOr VARCHAR(50) NOT NULL, 
	                    passwordOr VARCHAR(255) NOT NULL,
	                    UNIQUE (emailOr, passwordOr));
                    """)
def createUsersTable(cursor):
    cursor.execute("""
  				DROP TABLE IF EXISTS Users CASCADE;
                CREATE TABLE Users (
 	                idUs SERIAL PRIMARY KEY,
	                emailUs VARCHAR(100) UNIQUE NOT NULL,
 	                passwordUs INT UNIQUE NOT NULL,
 	                accessUs BOOL NOT NULL,
 	                idOwner INT NOT NULL,
 	                FOREIGN KEY(idOwner)
 	                REFERENCES Owners (idOwner));
                    """)
def createUrlTable(cursor):
    cursor.execute("""
  				 DROP TABLE IF EXISTS URL CASCADE;
                 CREATE TABLE URL (
 	                idURL SERIAL PRIMARY KEY,
 	                nameURL VARCHAR(100) NOT NULL,
 	                err VARCHAR(10),
 	                waf VARCHAR(15) NOT NULL,
	                idUs INT NOT NULL,
	                idOwner INT NOT NULL,
	                nameCert VARCHAR(100) default NULL,
	                dateCert timestamp   default NULL,
 	                FOREIGN KEY(idUs)
 	                REFERENCES Users (idUs),
	                FOREIGN KEY(idOwner)
 	                REFERENCES Owners (idOwner));
                    """)
