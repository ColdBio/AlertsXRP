## AlertsXRP - A Twitter XRP Price Alert Bot
This simple twitter bot that tweets key metrics about XRPs market performance every three hours. Metrics include:
- Current price in 🇺🇸 🇬🇧 🇪🇺 🇨🇳 currencies
- 24 hour high
- 24 hour low
- 24 hour percent change
- Volume: is the total trading volume of a cryptoasset across all active cryptoasset exchanges tracked by CoinGecko. [[1]](https://www.coingecko.com/en/faq)

## Short Case
Going into this I had no clue on how to execute my idea nor had any abstract image except that I wanted to tweet about important metrics in set intervals.
Commingling my private account and the price alert account was not idea so I first began by figuring out how to set up a twitter developer account and a seperate unique gmail account. After this, It was time to understand how to use Twitters API and after some poking around I decided to use Tweepy. Tweepy is a library that allows easy access to twitters API without getting bogged down in the details and fluff. 

Once I was able to send out tweets, it was easy to attach market data and an Image to every tweet. One issue had somewhat of a difficulty was overlaying the price to an image and making sure it was aligned properly. Other than that this project was not too difficult. For the future, I could change the core functionality of sending out tweets every three hours to sending out a tweet based on some market condition that is met, for example, if the price changed by 15% in the last 30 minutes.

## Example
[Here](https://twitter.com/AlertsXrp/status/1536368329774211073?s=20&t=5b8NnWMvdHPnCin_oan1og) the the direct link to the tweet displayed below

![Screenshot 2022-06-13 at 16 45 35](https://user-images.githubusercontent.com/64978825/173392815-0443e0e1-a90c-4d4d-9c96-7fd7f9eb1465.png)

## Credit
- [Tweepy](https://www.tweepy.org)
- [Coingecko API](http://coingecko.com)
- [Heroku](https://www.heroku.com)
- [Figma](https://www.figma.com)
