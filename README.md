# Hacash-Telegram-Bot

t.me/HacashBot

I am creating an open source project for Hacash in Telegram, it will be known as HacashBot

Progress:
Set up a bot using BotFather >> [HacashBot]( https://t.me/HacashBot)
Bot is in beta:
Issues:
- [x] 1. Consensus to >248 and <240 / changed to 230 - 255
- [x] 2. Rounding Up numbers still in debate since lower values can't be represented in higher formats. /not necessary
- [x] 3. Non-digits get rejected. /not necessary
- [x] 4. Fixed a bug on #Balance and #BalanceAndFormatter when inputing values with '/' since it can trigger new page leading to 'not found reply' instead of 'Address has no     Balance' /fixed   

On-going features:
- [x] 1. HAC formatter
- [x] 2. Web Scraping on http://explorer.hacashpool.com/address/foo or http://block.hacash.org/address/ to check balance by using BeautifulSoup
- [x] 3. Adding icons to menu-reply. //it can be implemented however there are instances where (for example, MAC Os) has a hard time accessing the menu button.  Since implementing icons on the menu reply also requires ```menu-reply == string-command-identifier``` which not smart to implement.
- [x] 4. Web Scraping dynamic data using Puppeteer by using Node.js framework. Or Pyppeteer port of Puppeteer /done
- [ ] 5. Diamond name finder - Log the address on [http://explorer.hacashpool.com/diamond/.....] on a file by knowing name of  diamondnum>blk.dat (from hacash_mainnet_data). Then set name of diamond to the address, thus creating a database.


Note: The program can also be made by utilizing the API.



