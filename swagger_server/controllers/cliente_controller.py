import connexion
import six

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server.models.empleado import Empleado  # noqa: E501
from swagger_server import util


def actualizar_cliente(idCliente, body):  # noqa: E501
    """actualizar un cliente

     # noqa: E501

    :param idCliente: ID delcliente a actualizar
    :type idCliente: int
    :param body: Objeto cliente actualizado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Cliente.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def borrar_cliente(idCliente):  # noqa: E501
    """Borrar cliente

     # noqa: E501

    :param idCliente: ID del cliente a borrar
    :type idCliente: int

    :rtype: None
    """
    return 'do some magic!'


def buscar_cliente_por_id(idCliente):  # noqa: E501
    """buscar un Cliente por ID

     # noqa: E501

    :param idCliente: ID del cliente a buscar
    :type idCliente: int

    :rtype: Cliente
    """
    return 'do some magic!'


def crear_cliente(body):  # noqa: E501
    """Crear un cliente

     # noqa: E501

    :param body: Objeto cliente a crear
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Empleado.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
