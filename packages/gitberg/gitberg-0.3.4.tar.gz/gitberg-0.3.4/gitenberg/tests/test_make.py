#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import gitenberg
from gitenberg.book import Book
from gitenberg.make import NewFilesHandler
from gitenberg.local_repo import LocalRepo

from mock import patch

class TestNewFileHandler(unittest.TestCase):

    def setUp(self):
        def here(appname):
            return os.path.join(os.path.dirname(__file__),'test_data')
        with patch.object(gitenberg.config.appdirs, 'user_config_dir', here) as path:
            with patch('github3.login') as login:
                self.login = login
                self.book = Book(1234)
        self.book.local_path = os.path.join(os.path.dirname(__file__),'test_data/1234')
        self.book.local_repo = LocalRepo(self.book.local_path)
        self.book.parse_book_metadata()
        self.file_maker = NewFilesHandler(self.book)

    def test_readme(self):
        self.file_maker.template_readme()
        self.assertTrue(
            os.path.exists(os.path.join(os.path.dirname(__file__),'test_data/1234/README.rst'))
        )
    
    @patch.object(LocalRepo, 'travis_key', new='fake_travis_key')
    def test_travis_files(self):
        #LocalRepo.travis_key = 'fake_travis_key'
        self.file_maker.travis_files()
        self.assertTrue(os.path.exists(
            os.path.join(os.path.dirname(__file__),'test_data/1234/.travis.yml')
        ))
        self.assertTrue(os.path.exists(
            os.path.join(os.path.dirname(__file__),'test_data/1234/.travis.deploy.api_key.txt')
        ))

    def tearDown(self):
        if os.path.exists(os.path.join(os.path.dirname(__file__),'test_data/1234/.git')):
            shutil.rmtree(os.path.join(os.path.dirname(__file__),'test_data/1234/.git'))
        if os.path.exists(os.path.join(os.path.dirname(__file__),'test_data/1234/README.rst')):
            os.remove(os.path.join(os.path.dirname(__file__),'test_data/1234/README.rst'))
        if os.path.exists(os.path.join(os.path.dirname(__file__),'test_data/1234/.travis.yml')):
            os.remove(os.path.join(os.path.dirname(__file__),'test_data/1234/.travis.yml'))
        if os.path.exists(os.path.join(
            os.path.dirname(__file__),'test_data/1234/.travis.deploy.api_key.txt'
        )):
            os.remove(os.path.join(
                os.path.dirname(__file__),'test_data/1234/.travis.deploy.api_key.txt'
            ))
