import connexion
import six

from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server import util


def borrar_pedido(idPedido):  # noqa: E501
    """Borrar pedido por Id

     # noqa: E501

    :param idPedido: ID del pedido a borrar
    :type idPedido: int

    :rtype: None
    """
    return 'do some magic!'


def crear_un_pedido(body):  # noqa: E501
    """Crea un pedido

     # noqa: E501

    :param body: pedido realizado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pedido.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def obtener_inventario():  # noqa: E501
    """Muestra el inventario de los productos por estado

     # noqa: E501


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def obtener_pedido_por_id(idPedido):  # noqa: E501
    """Busca un pedido por su ID

     # noqa: E501

    :param idPedido: ID del pedido a buscar
    :type idPedido: int

    :rtype: Pedido
    """
    return 'do some magic!'
