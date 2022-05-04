# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductosController(BaseTestCase):
    """ProductosController integration test stubs"""

    def test_actualizar_producto(self):
        """Test case for actualizar_producto

        Actualizar un producto existente
        """
        body = Producto()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/productos',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_borrar_producto(self):
        """Test case for borrar_producto

        Borrar un producto por su id
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/productos/{idProducto}'.format(idProducto=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_buscar_producto_por_estado(self):
        """Test case for buscar_producto_por_estado

        Buscar producto por estado.
        """
        query_string = [('status', 'disponible')]
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/productos/porEstado',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_producto(self):
        """Test case for crear_producto

        Crear un nuevo producto
        """
        body = Producto()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/productos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_productos_id_producto_get(self):
        """Test case for productos_id_producto_get

        Buscar un producto por ID
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/productos/{idProducto}'.format(idProducto=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
