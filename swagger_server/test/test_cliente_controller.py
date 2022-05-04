# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cliente import Cliente  # noqa: E501
from swagger_server.models.empleado import Empleado  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClienteController(BaseTestCase):
    """ClienteController integration test stubs"""

    def test_actualizar_cliente(self):
        """Test case for actualizar_cliente

        actualizar un cliente
        """
        body = Cliente()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/cliente/{idCliente}'.format(idCliente=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_borrar_cliente(self):
        """Test case for borrar_cliente

        Borrar cliente
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/cliente/{idCliente}'.format(idCliente=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_buscar_cliente_por_id(self):
        """Test case for buscar_cliente_por_id

        buscar un Cliente por ID
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/cliente/{idCliente}'.format(idCliente=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_cliente(self):
        """Test case for crear_cliente

        Crear un cliente
        """
        body = Empleado()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/cliente',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
