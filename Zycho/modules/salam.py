from time import sleep

from Zycho import ALIVE_NAME
from Zycho import CMD_HANDLER as cmd
from Zycho import CMD_HELP, bot
from Zycho.events import Zycho_cmd


@bot.on(Zycho_cmd(outgoing=True, pattern="p(?: |$)(.*)"))
async def _(event):
    await event.edit("**Assalamualaikum...**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"pe(?: |$)(.*)"))
async def _(event):
    await event.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@bot.on(Zycho_cmd(outgoing=True, pattern="P(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**Assalamualaikum...**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"l(?: |$)(.*)"))
async def _(event):
    await event.edit("**Wa'alaikumsalam...**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"a(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Haii Salken Saya {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**Assalamualaikum**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"j(?: |$)(.*)"))
async def _(event):
    await event.edit("**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await event.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"k(?: |$)(.*)"))
async def _(event):
    await event.edit(f"**Hallo KIMAAKK SAYA {ALIVE_NAME}**")
    sleep(2)
    await event.edit("**LU SEMUA NGENTOT 🔥**")


@bot.on(Zycho_cmd(outgoing=True, pattern=r"assalam(?: |$)(.*)"))
async def _(event):
    await event.edit("**Salam Dulu Biar Sopan**")
    sleep(2)
    await event.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\n  •  **Syntax :** `{cmd}p`\
        \n  •  **Function : **Assalamualaikum Dulu Biar Sopan..\
        \n\n  •  **Syntax :** `{cmd}pe`\
        \n  •  **Function : **salam Kenal dan salam\
        \n\n  •  **Syntax :** `{cmd}l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `{cmd}ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `{cmd}semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `{cmd}ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `{cmd}sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `{cmd}k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `{cmd}j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
    "
    }
)
