
CREATE SCHEMA IF NOT EXISTS `coolcalculator`;
USE `coolcalculator`;

DROP TABLE IF EXISTS `coolcalculator`;
CREATE TABLE IF NOT EXISTS `operations` (
	`id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`expression` VARCHAR(100) NOT NULL,
	`result` VARCHAR(10) NOT NULL
) ENGINE=InnoDB;