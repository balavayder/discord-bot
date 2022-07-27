import discord
from discord.ext import commands
import random
import praw
from cfg.cfg import client_id, user_agent, password, username, client_secret

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)


class Subreddity(commands.Cog):
    @commands.command()
    async def memes(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []

        top = subreddit.hot(limit=100)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name)
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    async def news(self, ctx):
        subreddit = reddit.subreddit("news")
        all_subs = []

        top = subreddit.hot(limit=100)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name)

        await ctx.send(embed=em)

    @commands.command()
    async def polskawpz(self, ctx):
        subreddit = reddit.subreddit("Polska_wpz")
        all_subs = []

        top = subreddit.hot(limit=100)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name)
        em.set_image(url=url)

        await ctx.send(embed=em)

