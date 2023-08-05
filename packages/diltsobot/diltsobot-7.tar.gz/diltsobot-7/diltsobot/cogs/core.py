from discord.ext import commands, pages
from .defs import client, Bot, view
import datetime, time, discord, asyncio, logging
import aiofiles, os
from importlib import resources

logging.basicConfig(filename="output.log", filemode="a", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s",)

description = ""
hexa = f"<t:{(time.mktime(datetime.datetime.now().timetuple()))}:R>".replace(".0", "")


class Core(commands.Cog):
	def __init__(self, bot: Bot):
		self.bot = bot
		logging.info(f"{__name__} cog loaded")
		self.hooks = bot.hooks

	def cog_unload(self):
		logging.info(f"{__name__} cog unloaded")

	@commands.Cog.listener('on_ready')
	async def ready(self):
		print("Online")
		q = discord.Webhook.from_url(self.hooks.debughook, session=client.session2)
		await self.bot.change_presence(activity=discord.Game(name="with frogs"))
		logging.info(f"Logged in!")
		await q.edit_message(message_id=1047667970555519036, content="", attachments=[], file=discord.File(fp='output.log', filename="log.py"))
		await q.send(username=self.bot.user.name, avatar_url=self.bot.user.avatar.url, content="Online")
	
	admin = discord.SlashCommandGroup("admin", "Admin commands")
	owner = discord.SlashCommandGroup("bot", "Advanced bot commands")
	@admin.command(description="Makes the bot say something")
	@commands.has_any_role(1000205572173471744, 1008027971694633060, 1047327417338957945)
	async def say(self,
					ctx: discord.ApplicationContext,
					message: discord.Option(description="Message to send") = "",
					media: discord.Option(discord.Attachment) = None,
					channel: discord.Option(discord.TextChannel, description="Channel to send the message to"
											) = None,
					delete_after: discord.Option(float, description="How long (in seconds) you want the message to delete after")=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000.0
					):
		if channel == None:
			if media != None:
				file = await media.to_file()
				await ctx.send(message, allowed_mentions=discord.AllowedMentions.none(), file=file, delete_after=delete_after)
			else:
				await ctx.send(message, allowed_mentions=discord.AllowedMentions.none(), delete_after=delete_after)
			await ctx.respond(f"Command executed.", ephemeral=True)
		else:
			if media != None:
				file = await media.to_file()
				await channel.send(message, allowed_mentions=discord.AllowedMentions.none(), file=file, delete_after=delete_after)
			else:
				await channel.send(message, allowed_mentions=discord.AllowedMentions.none(), delete_after=delete_after)
			await ctx.respond("Sent whatever you wanted me to...")


	flag = discord.SlashCommandGroup("flag")
	@flag.command(description="Sets whether you want moderators to be arrested for doing more than 1 mod action per minute")
	@commands.is_owner()
	async def toggle(self, ctx: discord.ApplicationContext, uwu: discord.Option(name="toggle", description="Figure it out yourself", choices=[discord.OptionChoice("Enable", "OwO"), discord.OptionChoice("Disable", "UwU")])):
		async with aiofiles.open('toggle.txt', 'w') as f:
			await f.write(uwu)
		await ctx.respond("Done")


	@owner.command(description="Shows basic bot information")
	@commands.is_owner()
	async def debug(self, ctx: discord.ApplicationContext):
		await ctx.respond(f"Bot last restarted {hexa}.\nOwners:\n<@" + ">\n<@".join(str(owner) for owner in self.bot.owner_ids) + f">\n{len(self.bot.cogs)}/4 cogs loaded.", file=await client.File(discord.File), allowed_mentions=discord.AllowedMentions.none())


	@owner.command(description="Puts something in output.log")
	@commands.is_owner()
	async def log(self, ctx: discord.ApplicationContext, message: discord.Option(description="Log message to put in output.log")):
		logging.info(message)
		await asyncio.sleep(1)
		await ctx.respond(file=discord.File('output.log', filename="log.py"), ephemeral=True)

	@owner.command(description="Manages the bot's systems")
	@commands.is_owner()
	async def manage(self, ctx: discord.ApplicationContext, action: discord.Option(int, description="What to do", choices=[discord.OptionChoice("Shutdown", 1), discord.OptionChoice("Clear cache", 2)])):
		q = discord.Webhook.from_url(self.hooks.debughook, session=client.session2)
		await q.edit_message(message_id=1047667970555519036, content=None, attachments=[], file=discord.File(fp='output.log', filename="log.py"), )
		if action == 1:
			await q.send(username=self.bot.user.name, avatar_url=self.bot.user.avatar.url, content=f"Shut down by {ctx.author}")
			await ctx.respond("Shutting down...")
			logging.info("Shutting down...")
			await asyncio.sleep(7)
			await self.bot.close()
		elif action == 2:
			await q.send(username=self.bot.user.name, avatar_url=self.bot.user.avatar.url, content=f"Cache cleared by {ctx.author}")
			await ctx.respond("Clearing...")
			logging.info("Clearing cache...")
			await self.bot.clear()

	@owner.command(description="Shows info of every member")
	@commands.is_owner()
	async def servers(self, ctx: discord.ApplicationContext):
		e = []
		async for user in ctx.guild.fetch_members():
			date_format = "%a, %d %b %Y %I:%M %p"
			embed = discord.Embed(colour=user.colour, description=user.mention)
			embed.set_author(name=str(user), icon_url=user.display_avatar)
			embed.set_thumbnail(url=user.display_avatar)
			embed.add_field(
				name="Joined", value=user.joined_at.strftime(date_format))
			members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
			embed.add_field(name="Join position",
							value=str(members.index(user) + 1))
			embed.add_field(name="Registered",
							value=f"<t:{(time.mktime(user.created_at.timetuple()))}:R>".replace(".0", ""))
			if len(user.roles) > 1:
				role_string = " ".join([r.mention for r in user.roles][1:])
				embed.add_field(
					name=f"Roles [{len(user.roles) - 1}]",
					value=role_string,
					inline=False,
				)
			perm_string = ", ".join(
				[
					str(p[0]).replace("_", " ").title()
					for p in user.guild_permissions
					if p[1]
				]
			)
			embed.add_field(name="Guild permissions",
							value=perm_string, inline=False)
			embed.set_footer(text="ID: " + str(user.id))
			e.append(embed)
		else:
			pag = pages.Paginator(e, loop_pages=True, custom_view=view())
			await pag.respond(ctx.interaction, ephemeral=True)


def setup(bot: commands.Bot):
	bot.add_cog(Core(bot))