import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'it_is_my_service'
