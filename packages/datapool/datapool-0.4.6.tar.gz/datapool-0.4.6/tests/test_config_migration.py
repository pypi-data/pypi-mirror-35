#! /usr/bin/env python
# encoding: utf-8
from __future__ import print_function, division, absolute_import

# Copyright © 2018 Uwe Schmitt <uwe.schmitt@id.ethz.ch>

import shutil

from datapool.instance.config_handling import read_config


def test_from_0_4_2(data_path, monkeypatch, tmpdir):

    monkeypatch.setenv("ETC", tmpdir.strpath)

    datapool_folder = tmpdir.join("datapool")
    datapool_folder.mkdir()

    shutil.copy(
        data_path("config_0_4_2.ini"), datapool_folder.join("datapool.ini").strpath
    )

    config = read_config()
    assert config.http_server.port is not None
