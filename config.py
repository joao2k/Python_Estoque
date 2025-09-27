class Config:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.db = "projetopython"
        self.usuario = "root"
        self.senha = ""

    def get_ip(self):
        return self.ip

    def get_db(self):
        return self.db

    def get_usuario(self):
        return self.usuario

    def get_senha(self):
        return self.senha