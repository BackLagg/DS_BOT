import discord
from discord import utils


import config



intents = discord.Intents.all()
intents.members = True


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.POST_ID:
            channel = self.get_channel(payload.channel_id)  # получаем объект канала
            message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
            member = utils.get(message.guild.members,
                               id=payload.user_id)  # получаем объект пользователя который поставил реакцию

            try:
                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)

                if (len([i for i in member.roles if i and i.id not in config.EXCROLES])<= config.MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('Пользователю {0.display_name} выдана роль {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('Слишком много ролей для пользователя {0.display_name}'.format(member))

            except KeyError:
                print('KeyError, no role found for ' + emoji)

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = utils.get(message.guild.members,
                           id=payload.user_id)  # получаем объект пользователя который поставил реакцию

        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)

            await member.remove_roles(role)
            print('Роль {1.name} удалена пользователю {0.display_name}'.format(member, role))

        except KeyError:
            print('KeyError, no role found for ' + emoji)





client = discord.Client(intents=intents)
client = MyClient(intents=discord.Intents.all())


client.run(config.TOKEN)

