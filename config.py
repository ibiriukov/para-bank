import os
from dotenv import load_dotenv
load_dotenv()


CONFIG = {
    "ssi": os.getenv("PARA_BANK_SSI", ""),
    "password": os.getenv("PARA_BANK_PASSWORD", ""),
    "base_url": os.getenv("PARA_BANK_BASE_URL", ""),
}

if not CONFIG["base_url"]:
    raise ValueError("Missing PARA_BANK_BASE_URL in environment")


