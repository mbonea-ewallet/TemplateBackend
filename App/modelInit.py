import databases
import orm
import psycopg2

# database = databases.Database(
#     "postgresql+asyncpg://postgres:CW38stnBqQnCEHe@db.vqbjlhcywjisidxeipdg.supabase.co:5432/postgres"
# )
database = databases.Database(
    "postgresql+asyncpg://user:password@db:5432/mydatabase"
)

# databases = databases.Database(**args)
models = orm.ModelRegistry(database=database)
