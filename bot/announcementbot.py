import nextcord
from nextcord.ext import commands
from os import system 
from colorama import Fore
from time import sleep
	


guild_id = 000
owner = 000
prefixs = "/" # Optional Cas it uses Slash Command LOLS
token = ""
          
class Announce(nextcord.ui.Modal):

    def __init__(self):
        super().__init__(
            title="Make An Announce",
            custom_id="persistent_modal:feedback",
            timeout=None,
        )

        self.b = nextcord.ui.TextInput(
            label="Header",
            custom_id="persistent_modal:b",
        )
        self.add_item(self.b)

        self.d = nextcord.ui.TextInput(
              label="Description",
              max_length=100000,
              custom_id="persistent_modal:d",
           )
        self.add_item(self.d)
      
        self.a = nextcord.ui.TextInput(
              label="Footer",
              custom_id="persistent_modal:a",
            )
        self.add_item(self.a)

        self.s = nextcord.ui.TextInput(
              label="IMG link",
              custom_id="persistent_modal:s",
            )
        self.add_item(self.s)

    async def callback(self, interaction: nextcord.Interaction):
      embedsucceed = nextcord.Embed(title=self.b.value, description=self.d.value,color=0xfffff)
      embedsucceed.set_image(url=self.s.value)
      embedsucceed.set_footer(text=self.a.value)
      await interaction.send(embed=embedsucceed)
      
      
        


      



class Bot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_modals_added = False

    async def on_ready(self):
        if not self.persistent_modals_added:
            self.add_modal(Announce())
            self.persistent_modals_added = True
            print(f'\n > {bot.user}')
    
bot = Bot(command_prefix=prefixs)

@bot.slash_command(
    name="announce",
    description="announce",
    guild_ids=[guild_id],
)
async def announce (interaction: nextcord.Interaction):
    if (interaction.user.id == owner):
      await interaction.response.send_modal(Announce())



bot.run(token)

