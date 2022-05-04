import connexion
import six

from swagger_server.models.empleado import Empleado  # noqa: E501
from swagger_server import util


def actualizar_empleado(idEmpleado, body):  # noqa: E501
    """actualizar un empleado

     # noqa: E501

    :param idEmpleado: ID del empleado a actualizar
    :type idEmpleado: int
    :param body: Objeto empleado actualizado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Empleado.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def buscar_empleado_por_id(idEmpleado):  # noqa: E501
    """buscar un empleado por ID

     # noqa: E501

    :param idEmpleado: ID del empleado a buscar
    :type idEmpleado: int

    :rtype: Empleado
    """
    return 'do some magic!'


def crear_empleado(body):  # noqa: E501
    """Crear un empleado

     # noqa: E501

    :param body: Objeto empleado a crear
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Empleado.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user(idEmpleado):  # noqa: E501
    """Borrar empleado

     # noqa: E501

    :param idEmpleado: ID del empleado a borrar
    :type idEmpleado: int

    :rtype: None
    """
    return 'do some magic!'
