import connexion
import six

from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server import util


def actualizar_producto(body):  # noqa: E501
    """Actualizar un producto existente

    Actulziar un producto # noqa: E501

    :param body: Objeto producto que debe agregarse a la tienda
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Producto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def borrar_producto(idProducto):  # noqa: E501
    """Borrar un producto por su id

     # noqa: E501

    :param idProducto: ID del producto a borrar
    :type idProducto: int

    :rtype: None
    """
    return 'do some magic!'


def buscar_producto_por_estado(status):  # noqa: E501
    """Buscar producto por estado.

     # noqa: E501

    :param status: Valores de estado que deben tenerse en cuenta para el filtro
    :type status: List[str]

    :rtype: List[Producto]
    """
    return 'do some magic!'


def crear_producto(body):  # noqa: E501
    """Crear un nuevo producto

    Crea un producto # noqa: E501

    :param body: Objeto producto que debe agregarse a la tienda
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Producto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def productos_id_producto_get(idProducto):  # noqa: E501
    """Buscar un producto por ID

    Permite buscar un producto por su ID # noqa: E501

    :param idProducto: ID del producto a buscar
    :type idProducto: int

    :rtype: Producto
    """
    return 'do some magic!'
