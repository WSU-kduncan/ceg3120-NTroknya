# How to guide for bot.py

## Required software/API:
- `python3`
- `python3-pip`
- `discord.py`
- `python-dotenv`

## How to get API token:
- [instructions for how to get API token and initialize bot](https://realpython.com/how-to-make-a-discord-bot-python/)
- Store this token in a `.env` file that you SHOULD NEVER, EVER push to a github repository.
- If you do, then you will need to remove the file from tracking AND generate a new token.
- The token will be stored in a variable called `DISCORD_TOKEN`
- Also in the `.env` file you will create a variable called `DISCORD_GUILD` to store the name of the server you wish to deploy the bot to

## Usage
- The bot will respond to the command `oath!`
- This command will randomly output on of the Lantern Oaths from DC comics:
  - `IN BRIGHTEST DAY, IN BLACKEST NIGHT, NO EVIL SHALL ESCAPE MY SIGHT, LET THOSE WHO WORSHIP EVIL’S MIGHT, BEWARE MY POWER… GREEN LANTERN’S LIGHT!`
  - `IN BLACKEST DAY, IN BRIGHTEST NIGHT, BEWARE YOUR FEARS MADE INTO LIGHT, LET THOSE WHO TRY TO STOP WHAT’S RIGHT, BURN LIKE MY POWER… SINESTRO’S MIGHT!`
  - `THE BLACKEST NIGHT FALLS FROM THE SKIES, THE DARKNESS GROWS AS ALL LIGHT DIES, WE CRAVE YOUR HEARTS AND YOUR DEMISE, BY MY BLACK HAND… THE DEAD SHALL RISE!`
  - `WITH BLOOD AND RAGE OF CRIMSON RED, RIPPED FROM A CORPSE SO FRESHLY DEAD, TOGETHER WITH OUR HELLISH HATE, WE’LL BURN YOU ALL… THAT IS YOUR FATE!`
  - `IN FEARFUL DAY, IN RAGING NIGHT, WITH STRONG HEARTS FULL, OUR SOULS IGNITE, WHEN ALL SEEMS LOST IN THE WAR OF LIGHT, LOOK TO THE STARS… FOR HOPE BURNS BRIGHT!`
  - `THIS POWER IS MINE, THIS IS MY LIGHT. BE IT IN BRIGHT OF DAY OR BLACK OF NIGHT. I LAY CLAIM TO ALL THAT FALLS WITHIN MY SIGHT, TO TAKE WHAT I WANT… THAT IS MY RIGHT!`
  - `TOR LOREK SAN, BOR NAKKA MUR. NATROMO FAAN TORNEK WOT UR. TER LANTERN KER LO ABIN SUR. TAAN LEK LEK NOK – FORMORROW SUR!`
  - `FOR HEARTS LONG LOST AND FULL OF FRIGHT, FOR THOSE ALONE IN BLACKEST NIGHT, ACCEPT OUR RING AND JOIN OUR FIGHT, LOVE CONQUERS ALL… WITH VIOLET LIGHT!`
  - `IN DARKEST DAY, IN SILENT NIGHT WITH SOULS FULL OF LIGHT CRUSH THOSE WHO BRING BLACKEST NIGHT BY OUR HAND… WHITE LANTERN’S LIGHT!!`
- Each oath corresponds to a different color and "emotion":
  - Green:Will
  - Yellow:Fear
  - Black:Death
  - Red:Rage/Anger
  - Blue:Hope
  - Orange:Greed/Avarice
  - Indigo:Compassion
  - Violet/Pink:Love
  - White:Life

## Research
- How to have the code "always on"
 - Use the `setsid` to run the script in a new session that is not affected by the current shell terminal.
 - This way allows the code to always be running so long as the system it is running on is powered on.
