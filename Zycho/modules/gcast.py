import asyncio
import os

import heroku3
from telethon.errors import FloodWaitError

from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME, GCAST_BLACKLIST
from Zycho.utils import edit_delete, edit_or_reply, Zycho_cmd

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("GCAST_BLACKLIST") or ""

@Zycho_cmd(pattern="blchat$")
async def sudo(event):
    blch = "True" if GCAST_BLACKLIST else "False"
    blc = blchat
    list = blc.replace(" ", "\nā¢ ")
    if blch == "True":
        await edit_or_reply(
            event,
            f"š« **GCast Blacklist :** `Enabled`\n\nš ** Blacklist Group :**\nā¢ `{list}`\n\nKetik `.addblacklist` di grup untuk menambahkan ke Blacklist.",
        )
    else:
        await edit_delete(event, "š« **GCast Blacklis :** `Disabled`")
        

@Zycho_cmd(pattern="addblacklist(?:\s|$)([\s\S]*)")
async def add(event):
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "GCAST_BLACKLIST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blchat = f"{GCAST_BLACKLIST} {gc}"
    nenwbl = blchat.replace("{", "")
    nenwbl = nenwbl.replace("}", "")
    blcht = nenwbl.replace(",", "")
    gcastblc = blcht.replace("[", "")
    gcid = gcastblc.replace("]", "")
    gcast_blc = gcid.replace("set() ", "")
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{gc}` **ke Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = gcast_blc
    
    
@Zycho_cmd(pattern="delblacklist(?:\s|$)([\s\S]*)")
async def _(event):
    xxx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        nenwbl = blchat.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari Daftar GCast Blacklist.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "GCAST_BLACKLIST"
        heroku_Config[var] = nenwbl
    else:
        await edit_delete(
            xxx, "**Pengguna ini tidak ada dalam Daftar GCast Blacklist.**", 45
        )


@Zycho_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Mengirim Pesan Siaran...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except FloodWaitError as e:
                if chat not in GCAST_BLACKLIST:
                    await asyncio.sleep(e.x)
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await kk.edit(
        f"ā Berhasil Terkirim Ke {done} Grup\nā Gagal Mengirim Ke {er} Grup"
    )


@Zycho_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Mengirim Pesan Siaran...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except FloodWaitError as e:
                if chat not in DEVS:
                    await asyncio.sleep(e.x)
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await kk.edit(
        f"ā Berhasil Terkirim Ke {done} Obrolan\nā Gagal Mengirim Ke {er} Obrolan"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  ā¢  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  ā¢  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  ā¢  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  ā¢  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)

CMD_HELP.update(
    {
        "setgcast": f"**Plugin : **`gcast`\
        \n\n  ā¢  **Syntax :** `{cmd}blchat`\
        \n  ā¢  **Function : **Untuk Mengecek informasi Gcast Blacklist.\
        \n\n  ā¢  **Syntax :** `{cmd}addblacklist`\
        \n  ā¢  **Function : **Untuk Menambahkan grup tersebut ke Gcast blacklist.\
        \n\n  ā¢  **Syntax :** `{cmd}delblacklist`\
        \n  ā¢  **Function : **Untuk Menghapus grup tersebut dari Gcast blacklist.\
        \n  ā¢  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)