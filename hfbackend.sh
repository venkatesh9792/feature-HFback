docker-compose build
docker-compose up -d
sleep 10
docker exec -it featurehfback-database-1  psql -U postgres -f /dataSetupScripts.sql

