class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245D'
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:root@localhost/python_ams'
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SESSION_TYPE = 'memcached'
    # https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
