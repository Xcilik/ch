# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="Channel", url="https://t.me/+tkyOQ3Sv7mplMjc1"),
            ],            
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink2),
            ],            
            [
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 :
        buttons = [
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink3),
            ],            
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel", url="https://t.me/+tkyOQ3Sv7mplMjc1"),
            ],                        
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink2),
            ],          
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 :
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel", url="https://t.me/borbay"),
            ],            
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
