# grpc-helper-api

<!-- NMK-BADGES-BEGIN -->
[![License: MPL](https://img.shields.io/github/license/dynod/grpc-helper-api)](https://github.com/dynod/grpc-helper-api/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/grpc-helper-api/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/grpc-helper-api/actions?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/grpc-helper-api)](https://pypi.org/project/grpc-helper-api/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- NMK-BADGES-END -->

Shared API files for [GRPC helpers](https://github.com/dynod/grpc-helper)

## Common API

The [common.proto](https://github.com/dynod/grpc-helper-api/blob/main/protos/grpc_helper_api/common.proto) file provides reusable API elements for other services (error codes, return status, etc)

## Server handling API

This API defines a [server handling service](https://github.com/dynod/grpc-helper-api/blob/main/doc/server.md) that can be used to fetch services/components information, and control global server behaviors.

## Config API

This API defines a [config service](https://github.com/dynod/grpc-helper-api/blob/main/doc/config.md) that handles configuration items.

## Logger API

This API defines a [logger service](https://github.com/dynod/grpc-helper-api/blob/main/doc/logger.md) that handles loggers configuration.

## Event API

This API defines an [events service](https://github.com/dynod/grpc-helper-api/blob/main/doc/events.md) that handles a generic event system.
