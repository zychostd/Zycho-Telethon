# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from Zycho import ALIVE_NAME
from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, bot
from Zycho.events import Zycho_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(Zycho_cmd(outgoing=True, pattern=r"fgban(?: |$)(.*)"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"**Warning!! User ππ½πΌππππΏ By** {DEFAULTUSER}\n"
    await event.edit("**Summoning out the mighty gban hammer β οΈ**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for _ in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1036951071:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 6969$ to my master__ [Heyworld](tg://user?id=1036951071) __to release your account__π"
            )
        else:
            jnl = (
                "**Warning!!**"
                "[{}](tg://user?id={})"
                f"** ππ½πΌππππΏ By** {DEFAULTUSER}\n\n"
                "**Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                no_reason = "**Reason: **`Jamet`"
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = f"**Warning!! User ππ½πΌππππΏ By** {DEFAULTUSER} \n**Reason:** `Jamet` "
        await event.reply(mention)
    await event.delete()


CMD_HELP.update(
    {
        "fakegban": f"**Plugin : **`fakegban`\
        \n\n  β’  **Syntax :** `{cmd}fgban` <reply> <reason>\
        \n  β’  **Function : **Untuk melakukan aksi Fake global banned , just for fun\
    "
    }
)
