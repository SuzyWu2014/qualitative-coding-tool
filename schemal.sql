CREATE DATABASE IF NOT EXISTS DB_CODES;

USE DB_CODES;

DROP TABLE IF EXISTS goals;
CREATE TABLE goals (
    goal_id INT(5) NOT NULL AUTO_INCREMENT,
    goal VARCHAR(10) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (goal_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS roles;
CREATE TABLE roles (
    role_id INT(5) NOT NULL AUTO_INCREMENT,
    role VARCHAR(10) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (role_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS notations;
CREATE TABLE notations (
    notation_id INT(5) NOT NULL AUTO_INCREMENT,
    notation VARCHAR(10) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (notation_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS auxiliaries;
CREATE TABLE auxiliaries (
    auxiliary_id INT(5) NOT NULL AUTO_INCREMENT,
    auxiliary VARCHAR(10) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (auxiliary_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS explanations;
CREATE TABLE explanations (
    explanation_id INT(5) NOT NULL AUTO_INCREMENT,
    explanation VARCHAR(10) NOT NULL,
    source_link VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (explanation_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS codes;
CREATE TABLE codes (
    code_id INT(5) NOT NULL AUTO_INCREMENT,
    explanation_id INT(5) NOT NULL,
    goal_id INT(5) NOT NULL,
    role_id INT(5) NOT NULL,
    auxiliary_id INT(5) DEFAULT NULL,
    position INT(5) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (code_id)
) ENGINE=InnoDB;

