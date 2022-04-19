class Config:
    SECRET_KEY = (
        "009ed827052896fc6ae7426c140ea46d"  # TODO: Use .env to hide those files.
    )
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Supressing notifications
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
