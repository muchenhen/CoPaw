# -*- coding: utf-8 -*-

from agentscope.message import Msg

from copaw.agents.utils.message_processing import (
    sanitize_invalid_local_media_blocks_in_message,
)


def test_sanitize_invalid_local_media_image_block() -> None:
    msg = Msg(
        name="user",
        role="user",
        content=[
            {
                "type": "image",
                "source": {
                    "type": "url",
                    "url": "/tmp/copaw-missing-image.png",
                },
            },
        ],
    )

    sanitize_invalid_local_media_blocks_in_message(msg)

    assert msg.content == [
        {
            "type": "text",
            "text": "[Missing image: copaw-missing-image.png]",
        },
    ]
