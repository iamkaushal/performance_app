create database `dbtester`;
CREATE  TABLE `dbtester`.`users` (

  `id` INT NOT NULL ,

  `username` VARCHAR(45) NOT NULL ,

  `password` VARCHAR(45) NULL ,

  `creation_date` DATETIME NULL ,

  PRIMARY KEY (`id`, `username`) );

CREATE  TABLE `dbtester`.`log_details` (

  `id` BIGINT NOT NULL ,

  `file_path` VARCHAR(500) NULL ,

  `creation_date` DATETIME NULL ,

  `insert_date` DATETIME NULL ,

  `agent_version` VARCHAR(100) NULL ,

  `dlp_family` VARCHAR(200) NULL ,

  `system_number` VARCHAR(200) NULL ,

  `srx_date` VARCHAR(200) NULL ,

  `figr` VARCHAR(200) NULL ,

  `cache_type` VARCHAR(200) NULL ,

  `process_type` VARCHAR(100) NULL ,

  `iserver_address` VARCHAR(150) NULL ,

  `iserver_version` VARCHAR(200) NULL ,

  `mmm_method` VARCHAR(150) NULL ,

  `log_date` DATETIME NULL ,

  `cache_slss` VARCHAR(150) NULL ,

  `program_version` VARCHAR(150) NULL ,

  `working` INT NULL ,

  `gone_bit` INT NULL ,

  `errors` INT NULL ,

  `warnings` INT NULL ,

  `file_name` VARCHAR(100) NULL ,

  PRIMARY KEY (`id`) );

