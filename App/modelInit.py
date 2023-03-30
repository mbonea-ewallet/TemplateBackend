import databases
import orm
import psycopg2

database = databases.Database(
    "postgresql+asyncpg://postgres:CW38stnBqQnCEHe@db.vqbjlhcywjisidxeipdg.supabase.co:5432/postgres"
)
# databases = databases.Database(**args)
models = orm.ModelRegistry(database=database)
