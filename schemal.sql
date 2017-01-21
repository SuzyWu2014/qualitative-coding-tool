CREATE DATABASE IF NOT EXISTS DB_CODES;

USE DB_CODES;

CREATE TABLE IF NOT EXISTS goals (
    goal_id INT(5) NOT NULL AUTO_INCREMENT,
    goal VARCHAR(10) DEFAULT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (goal_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS roles (
    role_id INT(5) NOT NULL AUTO_INCREMENT,
    role VARCHAR(10) DEFAULT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (role_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS notations (
    notation_id INT(5) NOT NULL AUTO_INCREMENT,
    notation VARCHAR(10) DEFAULT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (notation_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS auxiliaries (
    auxiliary_id INT(5) NOT NULL AUTO_INCREMENT,
    auxiliary VARCHAR(10) DEFAULT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (auxiliary_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS explanations (
    explanation_id INT(5) NOT NULL AUTO_INCREMENT,
    explanation VARCHAR(10) DEFAULT NULL,
    source VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (explanation_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS codes (
    code_id INT(5) NOT NULL AUTO_INCREMENT,
    explanation_id INT(5) NOT NULL,
    goal_id INT(5) NOT NULL,
    role_id INT(5) NOT NULL,
    auxiliary_id INT(5) DEFAULT NULL,
    position INT(5) NOT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (code_id)
) ENGINE=InnoDB;

