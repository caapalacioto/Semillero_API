# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_borrar_pedido(self):
        """Test case for borrar_pedido

        Borrar pedido por Id
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/admin/pedido/{idPedido}'.format(idPedido=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_un_pedido(self):
        """Test case for crear_un_pedido

        Crea un pedido
        """
        body = Pedido()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/admin/compras',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_inventario(self):
        """Test case for obtener_inventario

        Muestra el inventario de los productos por estado
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/admin/inventorio',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_pedido_por_id(self):
        """Test case for obtener_pedido_por_id

        Busca un pedido por su ID
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/admin/pedido/{idPedido}'.format(idPedido=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
