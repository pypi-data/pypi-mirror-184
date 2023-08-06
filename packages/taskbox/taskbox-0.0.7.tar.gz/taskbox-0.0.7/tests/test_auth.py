#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from sqlite3 import connect
from unittest import main
from unittest import TestCase

from flask import session

from taskbox import create_app


class AuthTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._resources = Path(__file__).parent
        path = cls._resources / "preload.sql"
        with open(path, mode="r", encoding="utf-8") as f:
            cls._preload = f.read()

    def setUp(self):
        self.db = "file::memory:?cache=shared"
        self.app = create_app({"TESTING": True, "DATABASE": self.db})
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.app.test_cli_runner().invoke(args=["init-db"])

    def tearDown(self):
        self.ctx.pop()

    def test_register_get(self):
        response = self.client.get("/auth/register")
        self.assertEqual(response.status_code, 200)

    def test_register_post(self):
        response = self.client.post(
            "/auth/register", data={"username": "user1", "password": "pass1"}
        )
        self.assertEqual(response.headers["location"], "/auth/login")

    def test_register_flash(self):
        db = connect(self.db)
        db.executescript(self._preload)
        parameters = [
            ("", "", b"Username is required."),
            ("user1", "", b"Password is required."),
            ("test", "test", b"already registered"),
        ]
        for parameter in parameters:
            with self.subTest(parameter=parameter):
                username, password, message = parameter
                response = self.client.post(
                    "/auth/register",
                    data={"username": username, "password": password},
                    follow_redirects=True,
                )
                self.assertIn(message, response.data)

    def test_login_get(self):
        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        db = connect(self.db)
        db.executescript(self._preload)
        response = self.client.post(
            "/auth/login", data={"username": "test", "password": "test"}
        )
        self.assertEqual(response.headers["location"], "/")

    def test_login_flash(self):
        db = connect(self.db)
        db.executescript(self._preload)
        parameters = [
            ("test1", "test", b"Incorrect username or password."),
            ("test", "test1", b"Incorrect username or password."),
        ]
        for parameter in parameters:
            with self.subTest(parameter=parameter):
                username, password, message = parameter
                response = self.client.post(
                    "/auth/login",
                    data={"username": username, "password": password},
                    follow_redirects=True,
                )
                self.assertIn(message, response.data)
