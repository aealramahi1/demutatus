# import discord
from discord.ext import commands
from bot_token import TOKEN

# Commands will be called by typing: !cmdname
bot = commands.Bot(command_prefix="!")

# All existing codes in this project
all_cogs = ["Binary"]

# Currently loaded cogs
current_cogs = ["Binary"]


@bot.event
async def on_ready():
    """
    Triggered when demutatus.py is executed
    """
    print("Demutatus is online!")

# TODO: Add a help embed


@bot.command(aliases=["load", "loadcog"])
@commands.has_permissions(manage_messages=True)
async def load_cog(ctx, ext):
    """
    Loads the cog passed in, if it exists.

    Parameters:
        ctx (Context): The required context
        ext (str): The name of the cog (without the file extension)
    """
    try:
        # Check to make sure we actually need to load this cog
        if ext not in current_cogs:
            # All cogs are in the cogs folder
            bot.load_extension("cogs.%s" % ext)
            current_cogs.append(ext)

            # Add this cog to all_cogs if it isn't in there already
            if ext not in all_cogs:
                all_cogs.append(ext)
            await ctx.send("Cog loaded successfully!")
        elif ext in current_cogs:
            await ctx.send("This cog is already loaded")
    except IOError:
        # if the cog doesn't exist, it will throw an IOError
        await ctx.send("This cog does not exist.")


@bot.command(aliases=["unload", "unloadcog"])
@commands.has_permissions(manage_messages=True)
async def unload_cog(ctx, ext):
    """
    Unloads the cog if it had already been loaded

    Parameters:
        ctx (Context): The required context
        ext (str): The name of the cog (without the file extension)
    """
    # Check to make sure this cog is loaded so we can unload it
    if ext in current_cogs:
        bot.unload_extension("cogs.%s" % ext)
        current_cogs.remove(ext)
        await ctx.send("Cog unloaded successfully!")
    elif ext not in current_cogs:
        await ctx.send("This cog is not loaded or doesn't exist.")


@bot.command(aliases=["reload", "reloadcog"])
@commands.has_permissions(manage_messages=True)
async def reload_cog(ctx, ext):
    """
    Unloads the cog and loads it again. Useful when the code of a cog is
    updated

    Parameters:
        ctx (Context): The required context
        ext (str): The name of the cog (without the file extension)
    """
    bot.reload_extension("cogs.%s" % ext)
    await ctx.send("Cog successfully reloaded!")


@bot.command(aliases=["view", "viewcogs"])
async def view_cogs(ctx):
    """
    Shows a list of all the currently loaded cogs

    Parameters:
        ctx (Context): The required context
    """
    if len(current_cogs) != 0:
        await ctx.send("Currently loaded cogs:")
        for the_cog in current_cogs:
            await ctx.send("-%s\n" % the_cog)
    else:
        await ctx.send("No currently loaded cogs.")


@bot.command(aliases=["stop", "end"])
@commands.has_permissions(manage_messages=True)
async def halt(ctx):
    """
    Halts the execution of the bot from within the Discord guild

    Parameters:
        ctx (Context): The required context
    """
    await ctx.send("Shutting down...")
    await bot.logout()


# Automatically load in all the cogs when the program is executed
for cog in all_cogs:
    bot.load_extension("cogs.%s" % cog)

# Bring the bot online
bot.run(TOKEN)
