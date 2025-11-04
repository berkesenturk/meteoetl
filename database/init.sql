-- database/init.sql
-- Initialize base schema for the MeteoETL project

-- Create the main schema if it doesn't exist
CREATE SCHEMA IF NOT EXISTS meteoetl;

-- Switch to that schema
SET search_path TO meteoetl;

-- Create a sample table for demonstration
CREATE TABLE IF NOT EXISTS weather_measurements (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(50) NOT NULL,
    measurement_time TIMESTAMP NOT NULL DEFAULT NOW(),
    temperature_celsius DECIMAL(5,2),
    humidity_percent DECIMAL(5,2),
    pressure_hpa DECIMAL(6,2)
);

-- Insert a test record
INSERT INTO weather_measurements (station_id, temperature_celsius, humidity_percent, pressure_hpa)
VALUES ('STATION-001', 21.5, 45.2, 1013.6);

-- Print confirmation for the Docker logs
\echo '✅ PostgreSQL initialization complete — sample schema "meteoetl" created.'
