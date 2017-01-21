CREATE DATABASE IF NOT EXISTS DB_CODES;

USE DB_CODES;

DROP TABLE IF EXISTS goals;
CREATE TABLE goals (
    goal_id INT(8) NOT NULL AUTO_INCREMENT,
    goal VARCHAR(16) NOT NULL,
    description VARCHAR(256) DEFAULT NULL,
    PRIMARY KEY (goal_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS roles;
CREATE TABLE roles (
    role_id     INT(8) NOT NULL AUTO_INCREMENT,
    role        VARCHAR(16) NOT NULL,
    description VARCHAR(256) DEFAULT NULL,
    PRIMARY KEY (role_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS notations;
CREATE TABLE notations (
    notation_id INT(8) NOT NULL AUTO_INCREMENT,
    notation    VARCHAR(16) NOT NULL,
    description VARCHAR(256) DEFAULT NULL,
    PRIMARY KEY (notation_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS explanations;
CREATE TABLE explanations (
    explanation_id  INT(8) NOT NULL AUTO_INCREMENT,
    explanation     VARCHAR(16) NOT NULL,
    source_link     VARCHAR(256) DEFAULT NULL,
    evernote_link   VARCHAR(256) DEFAULT NULL,
    description     VARCHAR(256) DEFAULT NULL,
    PRIMARY KEY (explanation_id)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS codes;
CREATE TABLE codes (
    code_id         INT(8) NOT NULL AUTO_INCREMENT,
    explanation_id  INT(8) NOT NULL,
    position        INT(8) NOT NULL,
    goal_id         INT(8) NOT NULL,
    role_id         INT(8) NOT NULL,
    notation_id     INT(8) NOT NULL,
    is_partial      BOOLEAN DEFAULT FALSE,
    is_emphasized   BOOLEAN DEFAULT FALSE,
    has_many        BOOLEAN DEFAULT FALSE,
    description     VARCHAR(256) DEFAULT NULL,
    PRIMARY KEY (code_id)
) ENGINE=InnoDB;

