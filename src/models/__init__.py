from sqlalchemy.ext.declarative import declarative_base
from src.models.models_db import SourceDocument  # Import the updated SQLAlchemy model

# Define the SQLAlchemy Base
Base = declarative_base()

# List of models to be included in database migrations or schema generation
db_models = [SourceDocument]

# Optional: If you're using Alembic for migrations, you can export the Base
all = ["Base", "SourceDocument", "db_models"]