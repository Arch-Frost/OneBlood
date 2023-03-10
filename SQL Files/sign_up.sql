CREATE SCHEMA IF NOT EXISTS login;
USE login;

CREATE TABLE  IF NOT EXISTS  `Sign_Up` (
  `UserID` INT AUTO_INCREMENT,
  `Username` VARCHAR(15) NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  `Website` VARCHAR(255) NOT NULL,
  `City` VARCHAR(40) NOT NULL,
  `Email` VARCHAR(100),
  `Phone_Number` VARCHAR(11) NOT NULL,
  `Creation Date`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`),
  CONSTRAINT signup_un_uk UNIQUE(Username)
);

CREATE TABLE  IF NOT EXISTS  `Registered_Accounts` (
  `UserID` INT,
  `Username` VARCHAR(15),
  `Password` VARCHAR(255),
  `Email` VARCHAR(100),
  PRIMARY KEY (`UserID`),
  CONSTRAINT RA_user_fk FOREIGN KEY (`UserID`) REFERENCES Sign_Up(`UserID`)
);

CREATE TABLE  IF NOT EXISTS  `Sessions` (
  `SessionID` INT AUTO_INCREMENT,
  `UserID` INT,
  `Login Date` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`SessionID`),
  CONSTRAINT sess_user_fk FOREIGN KEY (UserID) REFERENCES Registered_Accounts(UserID)  
);
