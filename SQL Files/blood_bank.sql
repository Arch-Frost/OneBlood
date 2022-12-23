-- CREATE SCHEMA IF NOT EXISTS University;
Use blood_bank;



CREATE TABLE  IF NOT EXISTS  `Medical_History` (
  `DonorID` INT,
  `Donation_Date` DATE,
  `HIV Positve` BOOLEAN,
  `Malaria` BOOLEAN,
  `Cancer` BOOLEAN,
  `Leukemia` BOOLEAN,
  `Heart Problems` BOOLEAN,
  `Lung Problems` BOOLEAN,
  `Hepatitis` BOOLEAN
);

CREATE TABLE  IF NOT EXISTS  `User` (
  `UserID` INT AUTO_INCREMENT,
  `Name` VARCHAR(20),
  `date_of_birth` date  NOT NULL,
  `Gender` VARCHAR(1),
  `Phone Number` VARCHAR(11),
  `Blood Group` VARCHAR(3),
  `Address` VARCHAR(40),
  PRIMARY KEY (`UserID`)
);

CREATE TABLE  IF NOT EXISTS  `Donor` (
  `DonorID` INT AUTO_INCREMENT,
  `UserID` INT,
  `Last Donation` DATE,
  PRIMARY KEY (`DonorID`)
);

CREATE TABLE  IF NOT EXISTS  `Patient` (
  `PatientID` INT AUTO_INCREMENT,
  `UserID` INT,

  PRIMARY KEY (`PatientID`)
);

CREATE TABLE  IF NOT EXISTS  `Donor_Transaction` (
  `DonationID` INT AUTO_INCREMENT,
  `BloodBagID` INT,
  `DonorID` INT,
  `Blood Group` VARCHAR(3),
  `Donation_Date` DATE  NOT NULL,
  PRIMARY KEY (`DonationID`)
);

CREATE TABLE  IF NOT EXISTS  `Inventory` (
  `BloodBagID` INT AUTO_INCREMENT,
  `DonationDate` DATE  NOT NULL,
  `ExpirationDate` DATE  NOT NULL,
  `DonationID` INT,
  `Blood Group` VARCHAR(3),
  `infected`  bool,
  PRIMARY KEY (`BloodBagID`)
  
);

CREATE TABLE  IF NOT EXISTS  `Patient_Transaction` (
  `RequestID` INT AUTO_INCREMENT,
  `BloodBagID` INT,
  `PatientID` INT,
  `Blood Group` VARCHAR(3),
  `Request Date` DATE,
  PRIMARY KEY (`RequestID`)
);

ALTER TABLE Donor
ADD CONSTRAINT donor_user_fk FOREIGN KEY (UserID) REFERENCES User(UserID);
ALTER TABLE Patient
ADD  CONSTRAINT patient_user_fk FOREIGN KEY (UserID) REFERENCES User(UserID);
ALTER TABLE Donor_Transaction
ADD CONSTRAINT dt_bag_fk FOREIGN KEY (BloodBagID) REFERENCES Inventory(BloodBagID);
ALTER TABLE Donor_Transaction
ADD CONSTRAINT dt_donor_fk FOREIGN KEY (DonorID) REFERENCES Donor(DonorID);
-- ALTER TABLE Medical_History
-- ADD  CONSTRAINT mh_dd_fk FOREIGN KEY (Donation_Date) REFERENCES Donor_Transaction(Donation_Date);

ALTER TABLE Patient_Transaction
ADD CONSTRAINT pt_bag_fk FOREIGN KEY (BloodBagID) REFERENCES Inventory(BloodBagID);
ALTER TABLE Patient_Transaction
ADD CONSTRAINT pt_patient_fk FOREIGN KEY (PatientID) REFERENCES Patient(PatientID);
ALTER TABLE Inventory
ADD CONSTRAINT IV_DI_fk FOREIGN KEY (DonationID) REFERENCES Donor_Transaction(DonationID);