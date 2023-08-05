#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `omniconverter` package."""

import unittest

from click.testing import CliRunner

from omniconverter import omniconverter
from omniconverter import cli

from omniconverter import Converter


class TestOmniconverter(unittest.TestCase):
    """Tests for `omniconverter` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_string_to_array(self):
        converter = Converter()
        assert converter.string_to_array("test") == ["t", "e", "s", "t"]
        
    def test_array_to_string(self):
        converter = Converter()
        assert converter.array_to_string([1,2,3,"abc",7,5,4]) == "123abc754"

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'omniconverter.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
