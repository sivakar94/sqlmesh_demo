MODEL (
  name sqlmesh_example.rainfall_full,
  kind FULL
);

SELECT
  *,
  'test' AS dummy
FROM sqlmesh_example.rainfall_source


CREATE USER SQLMESH_ADMIN
PASSWORD = 'Ilovevarna01!'