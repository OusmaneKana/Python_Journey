create table Student(
student_id SMALLINT NOT NULL,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
date_of_birth DATE NOT NULL,
R_A VARCHAR(40) NOT NULL,
room_number SMALLINT NOT NULL,
PRIMARY KEY (student_id)
);

-- creating tables for Signing in processes
create table Sign_In(
student_id SMALLINT NOT NULL,
signInt_date DATE NOT NULL,

FOREIGN KEY (student_id) REFERENCES Student(student_id)

);

-- creating tables for signing out processes 
create table Sign_Out(
student_id SMALLINT NOT NULL,
signOut_date DATE NOT NULL,

FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

