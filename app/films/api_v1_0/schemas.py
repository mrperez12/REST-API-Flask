from marshmallow import fields

from app.ext import ma 

class FilmSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    length = fields.Integer()
    year = fields.Integer()
    director = fields.String()
    actors = fields.Nested('ActorSchema', many=True)

class ActorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

# dump_only=true hara que solo se tenga en cuenta este campo
# a la hora de serializar el objeto (y no en la carga)

# actors en FilmSchema se define como 'nested', esto indica que 
# el esquema contiene varios (many=true) elementos de tipo ActorSchema