import random
import time
import mysql.connector
import discord
from discord.ext import commands


database = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
)
curseur = database.cursor()

bot = commands.Bot(command_prefix = "=", description = "Windows xp")
@bot.event
async def on_ready():
  global count
  Help = open("help.txt", "r", encoding = 'utf-8')
  ligne = Help.readlines()
  count = 0
  for line in ligne:
    count += 1
  Help.close()

  print("Opérationnel à 100 % !")





@bot.remove_command("help")

@bot.command(name = 'help_command', aliases = ['help', 'h'])
async def help_command(ctx):
  Help = open("help.txt", "r", encoding = 'utf-8')
  ligne = Help.readlines()
  Help_txt = ""
  for i in range(1, count):
    Help_txt += ligne[i]
  Help.close()
  aide = discord.Embed(title = ligne[0], description = Help_txt)
  message = await ctx.send(embed = aide)





@bot.command()
async def xp(ctx):
  message = await ctx.send("https://cdn.discordapp.com/attachments/817332910826455040/820627887409070090/DiscordXP.png")





@bot.command(name = 'binary_command', aliases = ['binary', 'b'])
async def binary_command(ctx , nb10 : int):
  try:
    if nb10 > 114813069527425452423283320117768198402231770208869520047764273682576626139237031385665948631650626991844596463898746277344711896086305533142593135616665318539129989145312280000688779148240044871428926990063486244781615463646388363947317026040466353970904996558162398808944629605623311649536164221970332681344168908984458505602379484807914058900934776500429002716706625830522008132236281291761267883317206598995396418127021779858404042159853183251540889433902091920554957783589672039160081957216630582755380425583726015528348786419432054508915275783882625175435528800822842770817965453762184851149029375:
      await ctx.send(":flag_fr: \nNombre trop élevé \n:flag_es: \nNúmero demasiado alto")
    elif nb10 < 0:
      await ctx.send(":flag_fr: \nJe ne fait pas les nombres négatif pour les nombres binaires\n:flag_es: \nNo hago los números negativos para los números binarios")
    else:
      nb2 = 0
      i = 0
      while nb10 != 0:
        n = nb10 % 2
        nb2 +=  n * 10 ** i
        nb10 = nb10 // 2
        i += 1
      await ctx.send(str(nb2))
  except:
    await ctx.send(":flag_fr: \nIl y a une erreur dans votre nombre \n:flag_es: \nHay un error en tu número")





@bot.command(name = 'binary_decimal_command', aliases = ['binary_decimal', 'bd'])
async def binary_decimal_command(ctx , nb2 : str):
  bon_nb = True
  i = 0
  u = -1
  nb10 = 0
  while bon_nb and u >= 0 - int(len(nb2)):
    if nb2[u] != '1' and nb2[u] != '0':
      bon_nb = False
    elif nb2[u] == '1':
        nb10 += 2 ** i
    else:
        nb10 += 0
    u -= 1
    i += 1
  if not bon_nb:
    await ctx.send(":flag_fr: \nIl y a une erreur dans votre nombre \n:flag_es: \nHay un error en tu número")
  else:
    await ctx.send(str(nb10))





@bot.command(name = 'hexadecimal_command', aliases = ['hexadecimal', 'hexa'])
async def hexadecimal_command(ctx , nb10 : str):
  try:
      nb16 = hex(int(nb10))
      nb16 = nb16[2::]
      await ctx.send(str(nb16))
  except:
    await ctx.send(":flag_fr: \nIl y a une erreur dans votre nombre \n:flag_es: \nHay un error en tu número")





@bot.command(name = 'hexadecimal_decimal_command', aliases = ['hexadecimal_decimal', 'hexad'])
async def hexadecimal_decimal_command(ctx , nb16 : str):
  try:
    nb10 = int(nb16, 16)
    await ctx.send(str(nb10))
  except:
    await ctx.send(":flag_fr: \nIl y a une erreur dans votre nombre \n:flag_es: \nHay un error en tu número")






@bot.command(name = 'crash_command', aliases = ['crash', 'c'])
async def crash_command(ctx):
  number_random = random.randint(0,4)
  gif = open("gif_crash.txt", "r", encoding = 'utf-8')
  all_gif = gif.readlines()
  gif.close()

  gif_random = all_gif[number_random]
  embed = discord.Embed(title=f"{ctx.author.name} has stopped working",color=0xFFFFFE)
  embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
  embed.set_image(url = gif_random)
  await ctx.send(embed = embed)





@bot.command(name = 'error404_command', aliases = ['error404', 'e404'])
async def error404_command(ctx):
  number_random = random.randint(0,4)
  gif = open("gif_error_404.txt", "r", encoding = 'utf-8')
  all_gif = gif.readlines()
  gif.close()

  gif_random = all_gif[number_random]

  embed = discord.Embed(title=f"{ctx.author.name} got a error 404",color=0xFFFFFE)
  embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
  embed.set_image(url = gif_random)
  await ctx.send(embed = embed)





@bot.command(name = 'shutdown_command', aliases = ['sd', 'shutdown'])
async def shutdown_command(ctx,user:discord.User):
  gif_random = "https://cdn.discordapp.com/attachments/817332910826455040/878740714698203197/Windows-10-Shutdown.png"
  embed = discord.Embed(title=f"{ctx.author.name} want use \"shutdown\" command on {user.name} computer",color=0xFFFFFE)
  embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
  embed.set_image(url = gif_random)
  await ctx.send(embed = embed)





@bot.command(name = 'quizz_command', aliases = ['quizz', 'q'])
async def quizz_command(ctx):
  run = False

  choix_langue = discord.Embed( description = ":flag_fr:  /  :flag_es:")
  message = await ctx.send(embed = choix_langue)
  await message.add_reaction("🇫🇷")
  await message.add_reaction("🇪🇸")
  def checkEmoji(reaction, user):
    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "🇫🇷" or str(reaction.emoji) == "🇪🇸")
  try:
    reaction, user = await bot.wait_for("reaction_add",timeout = 300, check = checkEmoji)
    await message.delete()

    if reaction.emoji == "🇫🇷":
      langue = 0
    elif reaction.emoji == "🇪🇸":
      langue = 1

    pret = open("pret.txt", "r", encoding = 'utf-8')
    lignes_pret = pret.readlines()
    pret.close()
    langue_txt = langue + 11 * langue
    pret = discord.Embed(title = lignes_pret[0 + langue_txt], description = lignes_pret[1 + langue_txt] + lignes_pret[2 + langue_txt] + lignes_pret[3 + langue_txt] + lignes_pret[4 + langue_txt] + lignes_pret[5 + langue_txt])
    pret_2 = discord.Embed(title = "OKKKKKKKKK", description = f"{lignes_pret[6 + langue_txt]} \n{lignes_pret[7 + langue_txt]}", color = 0x00FF00)
    titre_bonne_réponse = lignes_pret[8 + langue_txt]
    titre_mauvaise_réponse = lignes_pret[9 + langue_txt]
    txt_plus_un = lignes_pret[10 + langue_txt]
    txt_clic = f"\n{lignes_pret[7 + langue_txt]}"

  except:
    await ctx.send("")
    return

  message = await ctx.send(embed = pret)
  await message.add_reaction("1️⃣")
  await message.add_reaction("2️⃣")
  def checkEmoji(reaction, user):
    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "2️⃣" or str(reaction.emoji) == "1️⃣")
  try:
    reaction, user = await bot.wait_for("reaction_add",timeout = 300, check = checkEmoji)

    if reaction.emoji == "1️⃣":
      await message.edit(embed = pret_2)
      await message.add_reaction("⏩")
      def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "⏩")
      try:
        reaction, user = await bot.wait_for("reaction_add",timeout = 100, check = checkEmoji)
        if reaction.emoji == "⏩":
          run = True
          await message.delete()
      except:
        await ctx.send("")
        return
         
    elif reaction.emoji == "2️⃣":
      await message.delete()
      await ctx.send("ok")
  except:
    await ctx.send("")
    return

  if run:
    score = 0
    nb_question = 0
    maxi = 22
    liste = []
    chiffre = [x for x in range(maxi)]
    for u in range(11):
      i = random.choice(chiffre)
      liste.append(10 * i)
      del chiffre[chiffre.index(i)]

    if langue == 0:
      quest = open("quizz_fr.txt", "r", encoding = 'utf-8')
    else:
      quest = open("quizz_es.txt", "r", encoding = 'utf-8')
    ligne = quest.readlines()
    quest.close()

    while nb_question != 10:
      question_choix = liste[nb_question]
      nb_question += 1

      if langue == 1:
        q = "Question " + str(nb_question)
      else:
        q = "Pregunta " + str(nb_question)

      question_quizz = ligne[0 + question_choix]
      r1 = ligne[1 + question_choix]
      r2 = ligne[2 + question_choix]
      if ligne[5 + question_choix] != ligne[4]:
        r5 = ligne[5 + question_choix]
      else:
        r5 = 0
      if ligne[4 + question_choix] != ligne[4]:
        r4 = ligne[4 + question_choix]
      else:
        r4 = 0
      if ligne[3 + question_choix] != ligne[4]:
        r3 = ligne[3 + question_choix]
      else:
        r3 = 0
      txt_mauvaise_réponse = ligne[6 + question_choix]
      if ligne[7 + question_choix] != ligne[4]:
        txt_bonne_réponse = ligne[7 + question_choix]
      else:
        txt_bonne_réponse = 0
      nb_bonne_réponse = int(ligne[8 + question_choix])
      if ligne[9 + question_choix] != ligne[4]:
        image = ligne[9 + question_choix]
      else:
        image = 0

      if r5 != 0:
        quizzz = discord.Embed(title = q, description = question_quizz + "\n 1️⃣ " + r1 + "\n 2️⃣ " + r2 + "\n 3️⃣ " + r3 + "\n4️⃣ " + r4 + "\n5️⃣ " + r5)
      elif r4 != 0:
        quizzz = discord.Embed(title = q, description = question_quizz + "\n 1️⃣ " + r1 + "\n 2️⃣ " + r2 + "\n 3️⃣ " + r3 + "\n4️⃣ " + r4)
      elif r3 != 0:
        quizzz = discord.Embed(title = q, description = question_quizz + "\n 1️⃣ " + r1 + "\n 2️⃣ " + r2 + "\n 3️⃣ " + r3)
      else:
        quizzz = discord.Embed(title = q, description = question_quizz + "\n 1️⃣ " + r1 + "\n 2️⃣ " + r2)

      if image != 0:
        quizzz.set_image(url = image)
      
      message = await ctx.send(embed = quizzz)

      await message.add_reaction("1️⃣")
      await message.add_reaction("2️⃣")
      if r3 != 0:
        await message.add_reaction("3️⃣")
      if r4 != 0:
        await message.add_reaction("4️⃣")
      if r5 != 0:
        await message.add_reaction("5️⃣")

      def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "2️⃣" or str(reaction.emoji) == "1️⃣" or str(reaction.emoji) == "3️⃣" or str(reaction.emoji) == "4️⃣" or str(reaction.emoji) == "5️⃣")
      
      try:
        reaction, user = await bot.wait_for("reaction_add",timeout = 300, check = checkEmoji)
        if reaction.emoji == "1️⃣" :
          réponse = 1
        if reaction.emoji == "2️⃣" :
          réponse = 2
        if reaction.emoji == "3️⃣" :
          réponse = 3
        if reaction.emoji == "4️⃣" :
          réponse = 4
        if reaction.emoji == "5️⃣" :
          réponse = 5

        if réponse == nb_bonne_réponse :
          score += 1
          if txt_bonne_réponse != 0:
            embed2 = discord.Embed(title = titre_bonne_réponse , description = txt_bonne_réponse + "\n" + txt_plus_un + txt_clic, color = 0x00FF00)
          else:
            embed2 = discord.Embed(title = titre_bonne_réponse , description = txt_plus_un + txt_clic, color = 0x00FF00)
        else:
          embed2 = discord.Embed(title = titre_mauvaise_réponse, description = txt_mauvaise_réponse + txt_clic, color = 0xCC0033)

        await message.edit(embed=embed2)
        await message.add_reaction("⏩")
        def checkEmoji(reaction, user):
          return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "⏩")
        try:
          reaction, user = await bot.wait_for("reaction_add",timeout = 300, check = checkEmoji)
          if reaction.emoji == "⏩":
            await message.delete()
        except:
          await ctx.send("")
          return
      except:
        await ctx.send("")
        return

    if nb_question == 10:
      if langue == 0:
        fin_quizz = discord.Embed(title = "Fini", description = f"Bravo {user.name} ! Tu as fini le quizz et ton score est de {score} / 10", color = 0xf1c40f)
        fin_quizz.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
      else:
        fin_quizz = discord.Embed(title = "Fin", description = f"¡ Bravo {user.name} ! has terminado el cuestionario del informatico y tu nota final es de {score} / 10", color = 0xf1c40f)
        fin_quizz.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
      fin_quizz.set_image(url = "https://cdn.discordapp.com/attachments/817332910826455040/817333382861815838/393462246430474241.png")
      message = await ctx.send(embed = fin_quizz)
          

bot.run("") #token to put
