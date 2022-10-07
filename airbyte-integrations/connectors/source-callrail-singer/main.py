#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch

from source_callrail_singer import SourceCallrailSinger

if __name__ == "__main__":
    source = SourceCallrailSinger()
    launch(source, sys.argv[1:])
