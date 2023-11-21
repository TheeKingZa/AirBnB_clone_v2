/*
 * setup_mysql_test.sql
 * This script prepares a MySQL server for the testing environment of the AirBnB_clone_v2 project.
 */

-- Create or use the database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or use the user hbnb_test
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
