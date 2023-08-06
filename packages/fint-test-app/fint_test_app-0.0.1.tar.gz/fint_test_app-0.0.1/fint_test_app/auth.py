#  Copyright (c) 2023 actfint
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/8

from importlib_metadata import entry_points

from fint_test_app.logger import logger

auth = {ep.name: ep.load() for ep in entry_points(group="fint_auth")}

try:
    User = auth["User"]
    current_user = auth["current_user"]
    update_user = auth["update_user"]
    websocket_auth = auth["websocket_auth"]
    logger.info("auth plugin loaded")

except KeyError:
    logger.info("No auth plugin found, using default noauth")
    from fint_core.auth import (
        User,
        current_user,
        update_user,
        websocket_auth,
    )
