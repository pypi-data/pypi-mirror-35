#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `beamformer` package."""


import unittest
from click.testing import CliRunner

from beamformer import beamformer
from beamformer import cli


class TestBeamformer(unittest.TestCase):
    """Tests for `beamformer` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.beamformer = beamformer.Beamformer()

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_array_response(self):
        self.assertEqual(self.beamformer.get_array_response(), 0)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'beamformer.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
