import pybase64

from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, bot
from Zycho.utils import Zycho_cmd, edit_delete, edit_or_reply

@Zycho_cmd(pattern="enc(?: |$)(.*)")
async def endecrypt(query):
    xx = query.pattern_match.group(1)
    if xx:
        msg = xx
    elif query.is_reply:
        msgs = await query.get_reply_message()
        msg = msgs.message
    else:
        return await edit_delete(query, "**Berikan Sebuah Pesan atau Reply**")
    lething = str(pybase64.b64encode(bytes(f"{msg}", "utf-8")))[2:]
    await query.edit("`" + lething[:-1] + "`")
    
        
@Zycho_cmd(pattern="dec(?: |$)(.*)")
async def endecrypt(query):
    xx = query.pattern_match.group(1)
    if xx:
        msg = xx
    elif query.is_reply:
        msgs = await query.get_reply_message()
        msg = msgs.message
    else:
        return await edit_delete(query, "**Berikan Sebuah Pesan atau Reply**")
    lething = str(pybase64.b64decode(bytes(f"{msg}", "utf-8"), validate=True))[2:]
    await query.edit("`" + lething[:-1] + "`")
        

CMD_HELP.update(
    {
        "encrypt": f"**Plugin : **`base64`\
        \n\n  •  **Syntax :** `{cmd}enc`\
        \n  •  **Function : **Enkripsi pesan dengan base64.**\
        \n\n  •  **Syntax :** `{cmd}dec`\
        \n  •  **Function : **Mentranslate dari Kode base64.**\
    "
    }
)