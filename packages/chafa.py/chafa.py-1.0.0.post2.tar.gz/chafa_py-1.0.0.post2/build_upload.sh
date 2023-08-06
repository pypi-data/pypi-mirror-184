#! /bin/sh
#
# build_upload.sh
# Copyright (C) 2023 kenzie <kenzie@willowroot>
#
# Distributed under terms of the MIT license.
#


python -m build &&
    rename chafa_py chafa.py dist/*
