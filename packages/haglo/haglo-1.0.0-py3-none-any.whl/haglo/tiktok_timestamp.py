from requests import request
from datetime import datetime

def tiktok_timestamp(create_time: int) -> str:
  return datetime.fromtimestamp(create_time).date()