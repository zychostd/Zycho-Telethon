import requests

from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, bot
from Zycho.events import Zycho_cmd
from Zycho.utils import edit_or_reply


@bot.on(Zycho_cmd(outgoing=True, pattern="truth$"))
async def tede_truth(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Truth**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


@bot.on(Zycho_cmd(outgoing=True, pattern="dare$"))
async def tede_dare(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Dare**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


CMD_HELP.update(
    {
        "truthdare": f"**Plugin : **`truthdare`\
        \n\n  •  **Syntax :** `{cmd}truth`\
        \n  •  **Function : **Untuk tantangan.\
        \n\n  •  **Syntax :** `{cmd}dare`\
        \n  •  **Function : **Untuk kejujuran.\
    "
    }
)
