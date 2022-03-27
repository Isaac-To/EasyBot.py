# DisQuest

The DisQuest cog contain 3 versions: the original version, a orm-based version (more secure) that uses a local database, and a PostgreSQL version. The original version is marked as `disquest.py`, whille the other 2 are marked as `disquest-orm.py` and `disquest-postgres.py`. `disquest-orm.py` is a rewritten version that uses an ORM (Object Relational Mapper) to store the data, while `disquest-postgres.py` is a rewritten version that relies on a PostgreSQL database.

## DisQuest and DisQuest-ORM 

Both do not need any setup. Make sure to create a folder called `disquest` and that's it

## DisQuest-Postgres

This version is meant for production use, where high read/write speeds are needed. SQLite3 frequently locks up when having tons of connections, thus making it not suitable for production use. To get started, download the [PostgreSQL Server](https://www.postgresql.org/) and if you wish, [pgAdmin4](https://www.pgadmin.org/) and psql (if you are using an installer, both pgAdmin4 and psql would be included if you selected them). Alternatively, you can use the Docker version [here](https://hub.docker.com/_/postgres). 

Once installed, open up a query console and run this query: 

```sql
CREATE DATABASE disquest;
```

Make sure to also go to the `disquest-postgres.py` file, and make a `.env file`. Add the following: `Postgres_Password`, `Postgres_Server_IP`, and `Postgres_Username`. The password and username is the account that you are going to use to access the database, and the server ip address can be either set as a IPv4 address, or if you are hosting it locally, `127.0.0.1`. Note that if you hosting the database somewhere else (like on AWS, Azure, or GCP), you will need to set the server ip address to the public ip address of the server.

Once done, that's it. The cog will take care of the rest. And also as a side note, DisQuest-Postgres is the exact same version used by [Rin](https://github.com/No767/Rin) and [Kumiko](https://github.com/No767/Kumiko)