from app.config.connection import Connection
class Alumno:
    def __init__(self):
        self.model = Connection('estudiantes')

    def get_alumnos(self, order):
        return self.model.get_all(order)

    def get_alumno(self, id_object):
        return self.model.get_by_id(id_object)

    def search_alumno(self, data):
        return self.model.get_columns(data)

    def insert_alumno(self, alumno):
        return self.model.insert(alumno)

    def update_alumno(self, id_object, data):
        return self.model.update(id_object, data)

    def delete_alumno(self, id_object):
        return self.model.delete(id_object)