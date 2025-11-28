from logging.config import fileConfig
import os
import sys
from dotenv import load_dotenv

from sqlalchemy import engine_from_config, pool
from alembic import context

# ------------------------------
# Load environment variables
# ------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# ------------------------------
# Add project root to sys.path
# ------------------------------
# So 'from models import Base' works
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ------------------------------
# Import your models
# ------------------------------
from models import Base  # Make sure models.py is in project root

# ------------------------------
# Alembic Config
# ------------------------------
config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata  # Metadata used for autogenerate

# ------------------------------
# Run migrations offline
# ------------------------------
def run_migrations_offline():
    """Run migrations without a DB connection (generates SQL)."""
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is not set in .env")
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True
    )
    with context.begin_transaction():
        context.run_migrations()

# ------------------------------
# Run migrations online
# ------------------------------
def run_migrations_online():
    """Run migrations with a DB connection."""
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is not set in .env")

    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = DATABASE_URL

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

# ------------------------------
# Choose offline or online mode
# ------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
