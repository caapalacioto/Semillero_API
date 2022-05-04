# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.empleado import Empleado  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEmpleadoController(BaseTestCase):
    """EmpleadoController integration test stubs"""

    def test_actualizar_empleado(self):
        """Test case for actualizar_empleado

        actualizar un empleado
        """
        body = Empleado()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/empleado/{idEmpleado}'.format(idEmpleado=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_buscar_empleado_por_id(self):
        """Test case for buscar_empleado_por_id

        buscar un empleado por ID
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/empleado/{idEmpleado}'.format(idEmpleado=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_empleado(self):
        """Test case for crear_empleado

        Crear un empleado
        """
        body = Empleado()
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/empleado',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Borrar empleado
        """
        response = self.client.open(
            '/caapalacioto/CoffeeAPI/1.0.0/empleado/{idEmpleado}'.format(idEmpleado=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
