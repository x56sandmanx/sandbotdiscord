import discord
from discord.ext import commands
from datetime import datetime

class Kick(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.has_any_role("Mod", "SandKnight (Admin)", "Sandman")
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    if not reason:
        await ctx.send("Please provide a reason")
        return
    await member.kick(reason=reason)
    channel = discord.utils.get(member.guild.channels, name="command-logs📚")
    embed=discord.Embed(title="Kick", color=0xc2b280,timestamp=datetime.utcnow())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(Kick(client))