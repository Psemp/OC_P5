-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Project5_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Project5_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Project5_db` DEFAULT CHARACTER SET utf8 ;
USE `Project5_db` ;

-- -----------------------------------------------------
-- Table `Project5_db`.`Category_table`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Project5_db`.`Category_table` ;

CREATE TABLE IF NOT EXISTS `Project5_db`.`Category_table` (
  `Category_id` INT UNSIGNED NOT NULL,
  `Category_name` VARCHAR(50) NOT NULL,
  `Translated_name` VARCHAR(45) NULL,
  PRIMARY KEY (`Category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Project5_db`.`Product_table`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Project5_db`.`Product_table` ;

CREATE TABLE IF NOT EXISTS `Project5_db`.`Product_table` (
  `Product_id` BIGINT(13) UNSIGNED NOT NULL,
  `Product_name` VARCHAR(100) NOT NULL,
  `Brand` VARCHAR(100) NULL,
  `Stores` VARCHAR(100) NULL,
  `Nutriscore` ENUM('A', 'B', 'C', 'D', 'E') NOT NULL,
  `Category_id` INT UNSIGNED NOT NULL,
  `Shortdesc` TEXT NULL,
  `PicUrl` TEXT NULL,
  PRIMARY KEY (`Product_id`),
  UNIQUE INDEX `Product_id_UNIQUE` (`Product_id` ASC) VISIBLE,
  INDEX `fk_category_id` (`Category_id` ASC) VISIBLE,
  CONSTRAINT `fk_category_id`
    FOREIGN KEY (`Category_id`)
    REFERENCES `Project5_db`.`Category_table` (`Category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Project5_db`.`Saved_searches`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Project5_db`.`Saved_searches` ;

CREATE TABLE IF NOT EXISTS `Project5_db`.`Saved_searches` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Result_id` BIGINT(13) UNSIGNED NOT NULL,
  `Origin_id` BIGINT(13) UNSIGNED NOT NULL,
  `Date_saved` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Saved_result_id` (`Result_id` ASC) INVISIBLE,
  INDEX `fk_Saved_origin_id` (`Origin_id` ASC) VISIBLE,
  CONSTRAINT `fk_Saved_result_id`
    FOREIGN KEY (`Result_id`)
    REFERENCES `Project5_db`.`Product_table` (`Product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Saved_origin_id`
    FOREIGN KEY (`Origin_id`)
    REFERENCES `Project5_db`.`Product_table` (`Product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
