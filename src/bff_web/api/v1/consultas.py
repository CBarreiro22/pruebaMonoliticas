
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    reservas: typing.List[Propiedad] = strawberry.field(resolver=obtener_propiedades)