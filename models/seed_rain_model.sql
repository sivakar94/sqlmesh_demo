MODEL (
  name sqlmesh_example.rainfall_source,
  kind SEED (
    path '../seeds/rainfall_data.csv'
  ),
  columns (
    Year TIMESTAMPNTZ,
    Month INT,
    Day INT,
    Humidity FLOAT,
    Humidity_2 FLOAT,
    Temperature FLOAT,
    Precipitation FLOAT
  ),
  grain [Year, Month, Day]
);