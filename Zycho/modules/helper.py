""" Userbot module for other small commands. """
from Zycho import ALIVE_NAME
from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, bot
from Zycho.events import Zycho_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(Zycho_cmd(outgoing=True, pattern=r"ihelp$"))
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Group Support :** [UNREALBABIES](t.me/HCMutualism)\n"
        f"✣ **Channel :** [Zycho Projects](t.me/zldprojects)\n"
        f"✣ **Owner :** [Lord Zycho](t.me/UnrealZlda)\n"
        f"✣ **Repo :** [Zycho USERBOT](https://github.com/zychostd/Zycho-Userbot)\n"
    )


@bot.on(Zycho_cmd(outgoing=True, pattern=r"listvar$"))
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://telegra.ph/List-Variabel-Heroku-untuk-Zycho USERBOT-09-22)"
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Zycho USERBOT.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Zycho USERBOT.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Zycho USERBOT.\
    "
    }
)
