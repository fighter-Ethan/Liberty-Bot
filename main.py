import discord
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os
import json
import requests
import random

client = commands.Bot(command_prefix="=")
member = discord.Member

client.remove_command('help')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the United States | =help"))
  print('Bot is ready fool')
  
@client.command()
async def speak (ctx, * , resp = "Hey"):
  await ctx.channel.purge(limit = 1)
  await ctx.send(resp)
  
@client.command()
async def whois(ctx , * , who = "NA"):
  if who == "NA":
    await ctx.send("You must specify a person!")
    return
  elif who == "President":
    embed = discord.Embed(title = "**President of the United States**" , description = "*Joseph R. Biden*" , color = discord.Color.blue())
    embed.add_field(name = "**Party**" , value = "Democratic" , inline = True)
    embed.add_field(name = "**Years**" , value = "2021-" , inline = True)
    embed.set_footer(text = "For more information, visit www.whitehouse.gov/")
    embed.set_thumbnail(url = "https://img.odishatv.in/wp-content/uploads/2020/11/US-President-joe-Biden.jpg")
    await ctx.send(embed=embed)
  elif who == "Vice President":
    embed = discord.Embed(title = "**Vice President of the United States**" , description = "*Kamala D. Harris*" , color = discord.Color.blue())
    embed.add_field(name = "**Party**" , value = "Democratic" , inline = True)
    embed.add_field(name = "**Years**" , value = "2021-" , inline = True)
    embed.set_footer(text = "For more information, visit www.whitehouse.gov/")
    embed.set_thumbnail(url = "https://www.democracynow.org/images/headlines/18/54118/full_hd/h1-kamala-harris-accepts-vice-presidential-nomination.jpg")
    await ctx.send(embed=embed)
  elif who == "Speaker of the House":
    embed = discord.Embed(title = "**Speaker of the House of Representatives**" , description = "*Nancy P. Pelosi*" , color = discord.Color.blue())
    embed.add_field(name = "**Party**" , value = "Democratic" , inline = True)
    embed.add_field(name = "**Years**" , value = "2007-2011" + "\n\u200b" + "2019-" , inline = True)
    embed.set_footer(text = "For more information, visit www.whitehouse.gov/")
    embed.set_thumbnail(url = "https://compote.slate.com/images/1f61ac5e-b5ee-4016-a777-1ab718eb9ec3.jpeg?width=780&height=520&rect=1560x1040&offset=0x0")
    await ctx.send(embed=embed)
  elif who == "Tempore":
    embed = discord.Embed(title = "**President Pro-Tempore of the Senate**" , description = "*Patrick Leahy*" , color = discord.Color.blue())
    embed.add_field(name = "**Party**" , value = "Democratic"  , inline = True)
    embed.add_field(name = "**Years**" , value = "2012-2015" + "\n\u200b" + "2021-" , inline = True)
    embed.set_thumbnail(url = "https://tse2.mm.bing.net/th?id=OIP.lf35_qVHfg2sQ5iGXC4YWwHaEA&pid=Api&P=0&w=326&h=177")
    embed.set_footer(text = "For more information, visit www.whitehouse.gov/")
    await ctx.send(embed=embed)

@client.command(aliases = ["Twitter"])
async def twitter(ctx , * , content = "Blank message"):
  if content == "Blank message":
    await ctx.send("You must enter a message!")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=2)
  else:
    embed = discord.Embed(title = "**Tweet**" , description = ctx.author.mention , color = discord.Color.blue())
    embed.add_field(name = "\n\u200b" , value = content)
    embed.set_thumbnail(url = "https://qtxasset.com/2016-08/twitter-bird-1366218_960_720.png?x6nGu8psCjvHEeWeKgH9vEX.VkvO8cuI")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@client.command(aliases = ["Reply" , "reply"])
async def r(ctx , user : discord.Member , * , content = "Blank message"):
  if content == "Blank message":
    await ctx.send("You must enter a message!")
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=2)
  else:
    embed = discord.Embed(title = "**Tweet (Replying to " + user.mention + ")**" , description = ctx.author.mention , color = discord.Color.blue())
    embed.add_field(name = "\n\u200b" , value = content)
    embed.set_thumbnail(url = "https://qtxasset.com/2016-08/twitter-bird-1366218_960_720.png?x6nGu8psCjvHEeWeKgH9vEX.VkvO8cuI")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = embed)

@client.command()
async def yapms(ctx):
  await ctx.send("https://www.yapms.com/")

@client.command()
async def amendment(ctx):
  await ctx.send("Please specify the amendment!")

@client.command()
async def amendmenti(ctx):
  embed = discord.Embed(title = "First Amendment to the Constitution of the United States" , description = "Ratified December 15, 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentii(ctx):
  embed = discord.Embed(title = "Second Amendment to the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)
  
@client.command()
async def amendmentiii(ctx):
  embed = discord.Embed(title = "Third Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentiv(ctx):
  embed = discord.Embed(title = "Fourth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.*" , inline = False)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentv(ctx):
  embed = discord.Embed(title = "Fifth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentvi(ctx):
  embed = discord.Embed(title = "Sixth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)


@client.command()
async def amendmentvii(ctx):
  embed = discord.Embed(title = "Seventh Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentviii(ctx):
  embed = discord.Embed(title = "Eighth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentix(ctx):
  embed = discord.Embed(title = "Ninth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)


@client.command()
async def amendmentx(ctx):
  embed = discord.Embed(title = "Tenth Amendment To the Constitution of the United States" , description = "Ratified in 1791" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxi(ctx):
  embed = discord.Embed(title = "Eleventh Amendment To the Constitution of the United States" , description = "Ratified February 7, 1795" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or Subjects of any Foreign State.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxii(ctx):
  embed = discord.Embed(title = "Twelfth Amendment To the Constitution of the United States" , description = " Ratified June 15, 1804" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The Electors shall meet in their respective states and vote by ballot for President and Vice-President, one of whom, at least, shall not be an inhabitant of the same state with themselves; they shall name in their ballots the person voted for as President, and in distinct ballots the person voted for as Vice-President, and they shall make distinct lists of all persons voted for as President, and of all persons voted for as Vice-President, and of the number of votes for each, which lists they shall sign and certify, and transmit sealed to the seat of the government of the United States, directed to the President of the Senate;*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

  await ctx.send("*-- the President of the Senate shall, in the presence of the Senate and House of Representatives, open all the certificates and the votes shall then be counted; -- The person having the greatest number of votes for President, shall be the President, if such number be a majority of the whole number of Electors appointed; and if no person have such majority, then from the persons having the highest numbers not exceeding three on the list of those voted for as President, the House of Representatives shall choose immediately, by ballot, the President. But in choosing the President, the votes shall be taken by states, the representation from each state having one vote; a quorum for this purpose shall consist of a member or members from two-thirds of the states, and a majority of all the states shall be necessary to a choice. [And if the House of Representatives shall not choose a President whenever the right of choice shall devolve upon them, before the fourth day of March next following, then the Vice-President shall act as President, as in case of the death or other constitutional disability of the President. --]* The person having the greatest number of votes as Vice-President, shall be the Vice-President, if such number be a majority of the whole number of Electors appointed, and if no person have a majority, then from the two highest numbers on the list, the Senate shall choose the Vice-President; a quorum for the purpose shall consist of two-thirds of the whole number of Senators, and a majority of the whole number shall be necessary to a choice. But no person constitutionally ineligible to the office of President shall be eligible to that of Vice-President of the United States.*")

@client.command()
async def amendmentxiii(ctx):
  embed = discord.Embed(title = "Thirteenth Amendment To the Constitution of the United States" , description = "Ratified December 6, 1865" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States, or any place subject to their jurisdiction.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxiv(ctx):
  embed = discord.Embed(title = "Fourteenth Amendment To the Constitution of the United States" , description = "Ratified December 6, 1865" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Section 1.*" + "\n\u200b" + "*All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside. No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.*" + "\n\u200b" + "\n\u200b" + "*Section 2.*" + "\n\u200b" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)
  await ctx.send("*Representatives shall be apportioned among the several States according to their respective numbers, counting the whole number of persons in each State, excluding Indians not taxed. But when the right to vote at any election for the choice of electors for President and Vice-President of the United States, Representatives in Congress, the Executive and Judicial officers of a State, or the members of the Legislature thereof, is denied to any of the male inhabitants of such State, being twenty-one years of age,* and citizens of the United States, or in any way abridged, except for participation in rebellion, or other crime, the basis of representation therein shall be reduced in the proportion which the number of such male citizens shall bear to the whole number of male citizens twenty-one years of age in such State.*" + "\n\u200b" + "\n\u200b" + "*Section 3.*" + "\n\u200b" + "*No person shall be a Senator or Representative in Congress, or elector of President and Vice-President, or hold any office, civil or military, under the United States, or under any State, who, having previously taken an oath, as a member of Congress, or as an officer of the United States, or as a member of any State legislature, or as an executive or judicial officer of any State, to support the Constitution of the United States, shall have engaged in insurrection or rebellion against the same, or given aid or comfort to the enemies thereof.*")
  await ctx.send("*But Congress may by a vote of two-thirds of each House, remove such disability.*" + "\n\u200b" + "\n\u200b" + "*Section 4.*" + "\n\u200b" + "*The validity of the public debt of the United States, authorized by law, including debts incurred for payment of pensions and bounties for services in suppressing insurrection or rebellion, shall not be questioned. But neither the United States nor any State shall assume or pay any debt or obligation incurred in aid of insurrection or rebellion against the United States, or any claim for the loss or emancipation of any slave; but all such debts, obligations and claims shall be held illegal and void.*" + "\n\u200b" + "\n\u200b" + "*Section 5.*" + "\n\u200b" + "*The Congress shall have the power to enforce, by appropriate legislation, the provisions of this article.*")

@client.command()
async def amendmentxv(ctx):
  embed = discord.Embed(title = "Fifteenth Amendment To the Constitution of the United States" , description = "Ratified February 3, 1870" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of race, color, or previous condition of servitude.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxvi(ctx):
  embed = discord.Embed(title = "Sixteenth Amendment To the Constitution of the United States" , description = "Ratified February 3, 1913" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The Congress shall have power to lay and collect taxes on incomes, from whatever source derived, without apportionment among the several States, and without regard to any census or enumeration.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxvii(ctx):
  embed = discord.Embed(title = "Seventeenth Amendment To the Constitution of the United States" , description = "Ratified April 8, 1913" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof, for six years; and each Senator shall have one vote. The electors in each State shall have the qualifications requisite for electors of the most numerous branch of the State legislatures. When vacancies happen in the representation of any State in the Senate, the executive authority of such State shall issue writs of election to fill such vacancies: Provided, That the legislature of any State may empower the executive thereof to make temporary appointments until the people fill the vacancies by election as the legislature may direct. This amendment shall not be so construed as to affect the election or term of any Senator chosen before it becomes valid as part of the Constitution.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxviii(ctx):
  embed = discord.Embed(title = "Eighteenth Amendment To the Constitution of the United States" , description = "Ratified January 16, 1919; Later Repealed By the Twenty First Amendment." , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*After one year from the ratification of this article the manufacture, sale, or transportation of intoxicating liquors within, the importation thereof into, or the exportation thereof from the United States and all territory subject to the jurisdiction thereof for beverage purposes is hereby prohibited.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxix(ctx):
  embed = discord.Embed(title = "Nineteenth Amendment To the Constitution of the United States" , description = "Ratified August 18, 1920" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of sex.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxx(ctx):
  embed = discord.Embed(title = "Twentieth Amendment To the Constitution of the United States" , description = "Ratified January 23, 1933" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Section 1.*" + "\n\u200b" + "*The terms of the President and the Vice President shall end at noon on the 20th day of January, and the terms of Senators and Representatives at noon on the 3d day of January, of the years in which such terms would have ended if this article had not been ratified; and the terms of their successors shall then begin.*" + "\n\u200b" + "\n\u200b" + "*Section 2.*" + "\n\u200b" + "*The Congress shall assemble at least once in every year, and such meeting shall begin at noon on the 3d day of January, unless they shall by law appoint a different day.*" + "\n\u200b" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)
  await ctx.send("*Section 3.*" + "\n\u200b" + "*If, at the time fixed for the beginning of the term of the President, the President elect shall have died, the Vice President elect shall become President. If a President shall not have been chosen before the time fixed for the beginning of his term, or if the President elect shall have failed to qualify, then the Vice President elect shall act as President until a President shall have qualified; and the Congress may by law provide for the case wherein neither a President elect nor a Vice President shall have qualified, declaring who shall then act as President, or the manner in which one who is to act shall be selected, and such person shall act accordingly until a President or Vice President shall have qualified.*" + "\n\u200b")
  await ctx.send("*Section 4.*" + "\n\u200b" + "*The Congress may by law provide for the case of the death of any of the persons from whom the House of Representatives may choose a President whenever the right of choice shall have devolved upon them, and for the case of the death of any of the persons from whom the Senate may choose a Vice President whenever the right of choice shall have devolved upon them.*" + "\n\u200b" + "*Section 5.*" + "\n\u200b" + "*Sections 1 and 2 shall take effect on the 15th day of October following the ratification of this article.*" + "\n\u200b")
  await ctx.send("*Section 6.*" + "\n\u200b" + "*This article shall be inoperative unless it shall have been ratified as an amendment to the Constitution by the legislatures of three-fourths of the several States within seven years from the date of its submission.*")

@client.command()
async def amendmentxxi(ctx):
  embed = discord.Embed(title = "Twenty-First Amendment To the Constitution of the United States" , description = "Ratified December 5, 1933" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The eighteenth article of amendment to the Constitution of the United States is hereby repealed.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxxii(ctx):
  embed = discord.Embed(title = "Twenty-Second Amendment To the Constitution of the United States" , description = "Ratified February 27, 1951" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*No person shall be elected to the office of the President more than twice, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of President more than once. But this Article shall not apply to any person holding the office of President when this Article was proposed by Congress, and shall not prevent any person who may be holding the office of President, or acting as President, during the term within which this Article becomes operative from holding the office of President or acting as President during the remainder of such term.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxxiii(ctx):
  embed = discord.Embed(title = "Twenty-Third Amendment To the Constitution of the United States" , description = "Ratified August 18, 1920" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The District constituting the seat of Government of the United States shall appoint in such manner as Congress may direct: A number of electors of President and Vice President equal to the whole number of Senators and Representatives in Congress to which the District would be entitled if it were a State, but in no event more than the least populous State; they shall be in addition to those appointed by the States, but they shall be considered, for the purposes of the election of President and Vice President, to be electors appointed by a State; and they shall meet in the District and perform such duties as provided by the twelfth article of amendment.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxxiv(ctx):
  embed = discord.Embed(title = "Twenty-Fourth Amendment To the Constitution of the United States" , description = "Ratified January 23, 1964" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The right of citizens of the United States to vote in any primary or other election for President or Vice President, for electors for President or Vice President, or for Senator or Representative in Congress, shall not be denied or abridged by the United States or any State by reason of failure to pay poll tax or other tax.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxxv(ctx):
  embed = discord.Embed(title = "Twenty-Fifth Amendment To the Constitution of the United States" , description = "Ratified December 5, 1933" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*Section 1.*" + "\n\u200b" + "*In case of the removal of the President from office or of his death or resignation, the Vice President shall become President.*" + "\n\u200b" + "*Section 2.*" + "\n\u200b" + "*Whenever there is a vacancy in the office of the Vice President, the President shall nominate a Vice President who shall take office upon confirmation by a majority vote of both Houses of Congress.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)
  await ctx.send("*Section 3.*" + "\n\u200b" + "*Whenever the President transmits to the President pro tempore of the Senate and the Speaker of the House of Representatives his written declaration that he is unable to discharge the powers and duties of his office, and until he transmits to them a written declaration to the contrary, such powers and duties shall be discharged by the Vice President as Acting President.*")
  await ctx.send("\n\u200b" + "*Section 4.*" + "\n\u200b" + "*Whenever the Vice President and a majority of either the principal officers of the executive departments or of such other body as Congress may by law provide, transmit to the President pro tempore of the Senate and the Speaker of the House of Representatives their written declaration that the President is unable to discharge the powers and duties of his office, the Vice President shall immediately assume the powers and duties of the office as Acting President.*")
  await ctx.send("*Thereafter, when the President transmits to the President pro tempore of the Senate and the Speaker of the House of Representatives his written declaration that no inability exists, he shall resume the powers and duties of his office unless the Vice President and a majority of either the principal officers of the executive department or of such other body as Congress may by law provide, transmit within four days to the President pro tempore of the Senate and the Speaker of the House of Representatives their written declaration that the President is unable to discharge the powers and duties of his office. Thereupon Congress shall decide the issue, assembling within forty-eight hours for that purpose if not in session. If the Congress, within twenty-one days after receipt of the latter written declaration, or, if Congress is not in session, within twenty-one days after Congress is required to assemble, determines by two-thirds vote of both Houses that the President is unable to discharge the powers and duties of his office, the Vice President shall continue to discharge the same as Acting President; otherwise, the President shall resume the powers and duties of his office.*")

@client.command()
async def amendmentxxvi(ctx):
  embed = discord.Embed(title = "Twenty-Sixth Amendment To the Constitution of the United States" , description = "Ratified July 1, 1971" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*The right of citizens of the United States, who are eighteen years of age or older, to vote shall not be denied or abridged by the United States or by any State on account of age.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def amendmentxxvii(ctx):
  embed = discord.Embed(title = "Twenty-Seventh Amendment To the Constitution of the United States" , description = "Ratified May 7, 1992" , color = discord.Color.green())
  embed.add_field(name = "\n\u200b" , value = "*No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of representatives shall have intervened.*" , inline = True)
  embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbaxw9R4sSVjebcCirRujyLxTFMhseMI-7yA&s")
  await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=813598756326604810&permissions=8&scope=bot")

@client.command()
async def whatis(ctx , * , content = "NA"):
  if content == "Plessy v Ferguson":
    embed = discord.Embed(title = "**Plessy v Ferguson**" , description = "May 18, 1896" , color = discord.Color.green())
    embed.add_field(name = "\n\u200b" , value = "With the cooperation of the East Louisiana Railroad, on June 7, 1892, Homer Plessy, a mulatto (7/8 white), seated himself in a white compartment, was challenged by the conductor, and was arrested and charged with violating the state law. In the Criminal District Court for the Parish of Orleans, Tourgée argued that the law requiring “separate but equal accommodations” was unconstitutional. When Judge John H. Ferguson ruled against him, Plessy applied to the State Supreme Court for a writ of prohibition and certiorari. Although the court upheld the state law, it granted Plessy’s petition for a writ of error that would enable him to appeal the case to the Supreme Court." , inline = True)
    embed.set_thumbnail(url = "https://otb.cachefly.net/wp-content/uploads/2013/06/law-gavel-flag.jpg")
    await ctx.send(embed=embed)
    return
  elif content == "Brown v Board of Education":
    embed = discord.Embed(title = "**Brown v Board of Education**" , description = "1954" , color = discord.Color.green())
    embed.add_field(name = "\n\u200b" , value =  "State-sanctioned segregation of public schools was a violation of the 14th amendment and was therefore unconstitutional. This historic decision marked the end of the ´separate but equal´ precedent set by the Supreme Court nearly 60 years earlier in  and served as a catalyst for the expanding civil rights movement during the decade of the 1950s." , inline = True)
    embed.set_thumbnail(url = "https://otb.cachefly.net/wp-content/uploads/2013/06/law-gavel-flag.jpg")
    embed.set_footer(text = "Read more at https://www.ourdocuments.gov/doc.php?flash=false&doc=87")
    await ctx.send(embed=embed)
    return
  elif content == "Roe v Wade":
    embed = discord.Embed(title = "**Roe v Wade**" , description = "1972" , color = discord.Color.green())
    embed.add_field(name = "\n\u200b" , value = "Ruling that declaratory, though not injunctive, relief was warranted, the court declared the abortion statutes void as vague and overbroadly infringing those plaintiffs' Ninth and Fourteenth Amendment rights. The court ruled the Does' complaint not justiciable. Appellants directly appealed to this Court on the injunctive rulings, and appellee cross-appealed from the District Court's grant of declaratory relief to Roe and Hallford." , inline = True)
    embed.set_footer(text = " To learn more, go to https://www.law.cornell.edu/supremecourt/text/410/113")
    embed.set_thumbnail(url = "https://otb.cachefly.net/wp-content/uploads/2013/06/law-gavel-flag.jpg")
    await ctx.send(embed=embed)
    return
  elif content == "list":
    embed = discord.Embed(title = "**List of Court Cases**" , description = "This is the list of what Liberty Bot has so far." , color = discord.Color.red())
    embed.add_field(name = "Plessy v Ferguson" , value = "\n\u200b" , inline = True)
    embed.add_field(name = "Brown v Board of Education" , value = "\n\u200b" , inline = True)
    embed.add_field(name = "Roe v Wade" , value = "\n\u200b" , inline = True)
    await ctx.send(embed=embed)
  elif content == "NA":
    await ctx.send("You must enter something into the command!")
  else:
    await ctx.send("Court case not found!")
    return

@client.command()
async def help(ctx):
  embed = discord.Embed(
    title = "**Help Menu**", description = "Liberty Bot Help Menu" , color = discord.Color.red())
  embed.add_field(name = "**Amendment[Roman Numeral lowercase]**" , value = "Recites the selected amendment" + "\n\u200b" , inline = True)
  embed.add_field(name = "**Whatis [Court case]**" , value = "Explains a monumental US court case!" + "\n\u200b" , inline = True)
  embed.add_field(name = "**Whatis list**" , value = "Displays a list of court cases that Liberty Bot can display" + "\n\u200b" , inline = True)
  embed.add_field(name = "**Yapms**" , value = "Sends the link to Yet Another Political Map Simulator" + "\n\u200b")
  embed.add_field(name = "**Potus [number]**" , value = "Displays info about the selected president." + "\n\u200b" , inline = True)
  embed.add_field(name = "**[Coming Soon!]** *Whois*" , value = "Displays who currently is in a position!" + "\n\u200b" , inline = True)
  embed.set_thumbnail(url = "https://tse3.mm.bing.net/th?id=OIP.L1HySTKDqLRYJ8MPyirxDwHaHa&pid=Api&P=0&w=300&h=300")

  await ctx.send(embed=embed)

@client.command()
async def potus(ctx, * , number = "N/A"):
  if number == "N/A":
    await ctx.send("Please specify a number between 1-46!")
  elif number == "1":
    await ctx.send("https://www.potus.com/george-washington/")
  elif number == "2":
    await ctx.send("https://www.potus.com/john-adams")
  elif number == "3":
    await ctx.send("https://www.potus.com/thomas-jefferson/")
  elif number == "4":
    await ctx.send("https://www.potus.com/james-madison/")
  elif number == "5":
    await ctx.send("https://www.potus.com/james-monroe"
    )
  elif number == "6":
    await ctx.send("https://www.potus.com/john-quincy-adams")
  elif number == "7":
    await ctx.send("https://www.potus.com/andrew-jackson/")
  elif number == "8":
    await ctx.send("https://www.potus.com/martin-van-buren/")
  elif number == "9":
    await ctx.send("https://www.potus.com/william-henry-harrison/")
  elif number == "10":
    await ctx.send("https://www.potus.com/john-tyler/")
  elif number == "11":
    await ctx.send("https://www.potus.com/james-k-polk/")
  elif number == "12":
    await ctx.send("https://www.potus.com/zachary-taylor/")
  elif number == "13":
    await ctx.send("https://www.potus.com/millard-fillmore/")
  elif number == "14":
    await ctx.send("https://www.potus.com/franklin-pierce/")
  elif number == "15":
    await ctx.send("https://www.potus.com/james-buchanan/")
  elif number == "16":
    await ctx.send("https://www.potus.com/abraham-lincoln/")
  elif number == "17":
    await ctx.send("https://www.potus.com/andrew-johnson")
  elif number == "18":
    await ctx.send("https://www.potus.com/ulysses-s-grant/")
  elif number == "19":
    await ctx.send("https://www.potus.com/rutherford-b-hayes/")
  elif number == "20":
    await ctx.send("https://www.potus.com/james-a-garfield/")
  elif number == "21":
    await ctx.send("https://www.potus.com/chester-a-arthur")
  elif number == "22":
    await ctx.send("https://www.potus.com/chester-a-arthur/")
  elif number == "23":
    await ctx.send("https://www.potus.com/benjamin-harrison")
  elif number == "24":
    await ctx.send("https://www.potus.com/grover-cleveland/")
  elif number == "25":
    await ctx.send("https://www.potus.com/william-mckinley/")
  elif number == "26":
    await ctx.send("https://www.potus.com/theodore-roosevelt")
  elif number == "27":
    await ctx.send("https://www.potus.com/william-h-taft/")
  elif number == "28":
    await ctx.send("https://www.potus.com/woodrow-wilson/")
  elif number == "29":
    await ctx.send("https://www.potus.com/warren-g-harding/")
  elif number == "30":
    await ctx.send("https://www.potus.com/calvin-coolidge")
  elif number == "31":
    await ctx.send("https://www.potus.com/herbert-hoover/")
  elif number == "32":
    await ctx.send("https://www.potus.com/franklin-d-roosevelt/")
  elif number == "33":
    await ctx.send("https://www.potus.com/harry-s-truman/")
  elif number == "34":
    await ctx.send("https://www.potus.com/dwight-d-eisenhower")
  elif number == "35":
    await ctx.send("https://www.potus.com/john-f-kennedy/")
  elif number == "36":
    await ctx.send("https://www.potus.com/lyndon-b-johnson/")
  elif number == "37":
    await ctx.send("https://www.potus.com/richard-m-nixon/")
  elif number == "38":
    await ctx.send("https://www.potus.com/gerald-r-ford/")
  elif number == "39":
    await ctx.send("https://www.potus.com/jimmy-carter/")
  elif number == "40":
    await ctx.send("https://www.potus.com/ronald-reagan/")
  elif number == "41":
    await ctx.send("https://www.potus.com/george-hw-bush/")
  elif number == "42":
    await ctx.send("https://www.potus.com/bill-clinton/")
  elif number == "43":
    await ctx.send("https://www.potus.com/george-w-bush/")
  elif number == "44":
    await ctx.send("https://www.potus.com/barack-obama/")
  elif number == "45":
    await ctx.send("https://www.potus.com/donald-j-trump/")
  elif number == "46":
    await ctx.send("https://www.potus.com/joe-biden/")
  
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
