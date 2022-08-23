from marshmallow import Schema, fields, validate


class UserCreateSchema(Schema):
    username = fields.String(
        required=True, allow_none=False, validate=[validate.Length(3, 100)])
    email = fields.Email(
        required=True, allow_none=False, validate=[validate.Length(max=250)])
    password = fields.String(
        required=True, allow_none=False, validate=[validate.Length(8, 250)])


class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
