import databases
import orm
import psycopg2

# HOST=aws.connect.psdb.cloud
# USERNAME=kn9rzjlad1tw8bvojqg9
# PASSWORD=pscale_pw_hSBO8rcekvnQp74bezC9gjnShhAWgkJYUS8GjGdrBKn
# DATABASE=movie-website


database = databases.Database(
    "postgresql+asyncpg://postgres:CW38stnBqQnCEHe@db.vqbjlhcywjisidxeipdg.supabase.co:5432/postgres"
)
# database = databases.Database(
#     "postgresql+asyncpg://user:password@db:5432/mydatabase"
# )

# #mysql
# database = databases.Database(
#     'mysql+asyncmy://kn9rzjlad1tw8bvojqg9:pscale_pw_hSBO8rcekvnQp74bezC9gjnShhAWgkJYUS8GjGdrBKn@aws.connect.psdb.cloud/movie-website'
# ,)


# databases = databases.Database(**args)
models = orm.ModelRegistry(database=database)
