import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://diary_user:diary123@postgres:5432/diary")
