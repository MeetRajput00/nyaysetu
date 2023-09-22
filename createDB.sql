CREATE TABLE Prisoner_dashboard (
	Id int not null,
	Case_filed int NOT NULL,
	lawyer int NOT NULL,
	legal_information int NOT NULL,
	Case_status int NOT NULL,
	Rehabilatation_schedule datetime NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Case_Filed (
	Id int not null,
	Name_of_prisoner int NOT NULL,
	Case_type TEXT NOT NULL,
	Court_name TEXT NOT NULL,
	Stage TEXT NOT NULL,
	Name_of_party TEXT NOT NULL,
	Year INT NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Legal_information (
	Id int not null,
	Name TEXT NOT NULL,
	Case_type TEXT NOT NULL,
	Case_no numeric NOT NULL,
	Name_of_party TEXT NOT NULL,
	court_name datetime NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Case_status (
	Id int not null,
	case_progress TEXT NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Lawyer (
	Id int not null,
	search_lawyer TEXT NOT NULL,
	Insert_lawyer_data TEXT NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Registration (
	Id int not null,
	Undertrial_prisoner int NOT NULL,
	Legal_Aid int NOT NULL,
	Prison_authority int NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Undertrial_prisoner (
	Id int not null,
	Name TEXT NOT NULL,
	Username TEXT NOT NULL,
	password TEXT NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Legal_aid (
	Id int not null,
	Name TEXT NOT NULL,
	Govt_id TEXT NOT NULL,
	Phone_no TEXT NOT NULL,
	select_role TEXT NOT NULL,
	PRIMARY KEY (Id)
);

CREATE TABLE Prison_authority (
	Id int not null,
	Name TEXT NOT NULL,
	Govt_id TEXT NOT NULL,
	Phone_no TEXT NOT NULL,
	select_role TEXT NOT NULL,
	PRIMARY KEY (Id)
);

ALTER TABLE Prisoner_dashboard ADD CONSTRAINT CaseFiledId FOREIGN KEY (Case_filed) REFERENCES Case_Filed(Id);

ALTER TABLE Prisoner_dashboard ADD CONSTRAINT LawyerId FOREIGN KEY (lawyer) REFERENCES Lawyer(Id);

ALTER TABLE Prisoner_dashboard ADD CONSTRAINT Legal_informationId FOREIGN KEY (legal_information) REFERENCES Legal_information(Id);

ALTER TABLE Prisoner_dashboard ADD CONSTRAINT Case_statusId FOREIGN KEY (Case_status) REFERENCES Case_status(Id);

ALTER TABLE Registration ADD CONSTRAINT Undertrial_prisonerId FOREIGN KEY (Undertrial_prisoner) REFERENCES Undertrial_prisoner(Id);

ALTER TABLE Registration ADD CONSTRAINT Legal_aidId FOREIGN KEY (Legal_Aid) REFERENCES Legal_aid(Id);

ALTER TABLE Registration ADD CONSTRAINT Prison_authorityId FOREIGN KEY (Prison_authority) REFERENCES Prison_authority(Id);

-- drop table dbo.Case_Filed;
-- drop table dbo.Case_status;
-- drop table dbo.Lawyer;
-- drop table dbo.Legal_aid;
-- drop table dbo.Legal_information;
-- drop table dbo.Prison_authority;
-- drop table dbo.Prisoner_dashboard;
-- drop table dbo.Undertrial_prisoner;
-- drop table dbo.Registration;
