docker pull pgvector/pgvector:pg16
docker run --name postgres-phidata -d -p 5432:5432 -e POSTGRES_PASSWORD=12345aA pgvector/pgvector:pg16