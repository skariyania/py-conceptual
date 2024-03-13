```shell
docker pull postgres
docker run --name pgsql-dev -e POSTGRES_PASSWORD=locapi -p 5432:5432 postgres
psql -h localhost --u postgres
```



```sql
INSERT INTO public.reservation(reservation_key) VALUES('1_13');
```