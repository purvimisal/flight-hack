<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/flybud.jpeg"> 
</p>

## Inspiration
There is a lot of anxiety with travel in general and COVID-19 has only made it worse. With 2021 being the year of recovery, no one can predict exactly when passenger demand will return. We thought of solving this problem by improving the cutomer onboarding experience and reducing the anxiety around COVID and travelling in flights.

To tackle this problem, we decided to reach the customers of American Airlines on heavily utilized platforms like Whatsapp, Messenger, slack etc. These platforms allow easy to access and quick response when compared to the existing app based chat response which has its own benefits. We showcase a way to tackle the problem which can be considered as a Proof of concept for using the idea as an enhancement or a complete solution in itself.

Both of us being international students, there will be a time when our parents would come to meet us. There experience could be improved by having laguage support for the chat facilities and notifications. So, we added it into the 'core reactor' of our chat buddy.

Using well known messaging systems allow us to utilize the features already integrated into these systems, like speech to text, attachments and location, saving us from the trouble if scaling the platorm. The problem to scale was successly conquered by developing this as a complete cloud based solution.

Some may say chatbots are a thing of the past, yet latest research with GPT3 and knowledge graph based QnA is a highly active field of research, and attracts a lot of attention when used in the right manner. So we followed the quote, "Either ride the wave or be washed by it", and here is flybuddy.

## What it does
Flight buddy is a AI powered chat buddy with traditional features of a notification system. In summary it does the following tasks:
1. Notifies customer on important alerts (eg. reminder for cab, airport regulations, pre and post flight messages)
2. AI chat response system ready to answer questions related to flight, COVID QnA and normal conversation.
3. Information retrieval for latest news on the destiantion.
4. Languge detection and translation for supporting multilingual travellers.

#### Domain used via domain.com: flybuddy.tech

#### Steps to connect and test flybuddy: 
1.  Send twilio number : join village-funny
2.  Go to https://whatsapp-bot-303117.wl.r.appspot.com/ and send notifications, ideally trip_confirmation first

###  Notifying customer on important alerts
<table align="center">
  <tr>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-29%20at%2021.34.18.jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-29%20at%2021.39.28.jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-29%20at%2015.50.05.jpeg" width=400> 
</p></td>
  </tr>
</table>

-  We focused on using the chat platform to send notifications and alerts regarding to empower the motto "Come fly with us". Telling the customer why American airline is safe to travel and providing a smooth onboarding experience by providing all the necessary information to the traveller.
-  The notification system is also used to showcase ads for upgrading to premium seats if the customer wanted.

### AI chat response system

<table align="center">
  <tr>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-30%20at%2015.53.01.jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-30%20at%2015.43.39.jpeg" width=400> 
</p></td>
</table>

-  We provide a response to frequently asked questions, for instance complaints, turbulance anxiety, flight status.
-  A custom response for COVID has been trained that helps with answering basic questions on COVID and travelling during the pandemic.
-  For customer engagement we trained the buddy with normal conversation and funny responses to a few messages(lets see if you find those messages)

### Information retrieval for news
<table align="center">
  <tr>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-31%20at%2001.20.42%20(1).jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-31%20at%2001.33.33%20(1).jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-31%20at%2001.38.37%20(1).jpeg" width=400> 
</p></td>
  </tr>
</table>


-  We all view the news, but we all know google will enhance our experience by showing the news 'relevant' to us, mostly our local news. But as a traveller, I want to make sure that I know the news of my destination.
-  Now, when you can do so much, why not simply read the news with your flight buddy.

### Language detection and translation

<table align="center">
  <tr>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-29%20at%2021.33.50.jpeg" width=400> 
</p></td>
    <td><p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/WhatsApp%20Image%202021-01-29%20at%2021.35.54.jpeg" width=400> 
</p></td>
  </tr>
</table>

-  Language is a great barrier for international travellers. This can be easily tackled if the notification systems had the messages traslated before being sent ot the customer.
-  Being a buddy, it was important to integrate the this feature of showing messages to the user in their preffered language.

## How we built it

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/Screen%20Shot%202021-01-31%20at%208.56.22%20AM.png"> 
</p>


We wanted a scalable solution and went for a complete cloud based solution. The tech stack is as follows, followed by detailed explaination of how we built the features :
* Google cloud app engine
* CockroachDB
* Google Translate API
* Google DialogFlow Engine
* Twilio WhatsApp Sandbox
* NewsAPI
* Stats API
* Python - Flask 

Mahan had recently travelled with american airlines and had materials that could be used for our flybuddy. We manually scraped details from the emails he recieved and curated the set of messages used as notification for flybuddy.

###  Notifying customer on important alerts

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/notif2.gif" width=400> 
</p>



-  We built a Flask server and deployed it in google cloud engine. The Flask server is hosted on https://whatsapp-bot-303117.wl.r.appspot.com, which was used for sending notifications to an active whatsapp number. User can simply select the type of notification or ad they want to show and provide the number connected to send the message.
-  The details of the notifications are retrieved from CockroachDB. We setup a cluster, filled the details and retrieved the data onto the notification sender page.

### AI chat response system

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/chatter.gif" width=400> 
</p>

-  AI chat messages were trained on Dialog flow that was connected using to the GCP project(thank you for the credits from GCP team)
-  Each set(COVID, flights and general qna) were trained on custom made intents and response messages and can be easily improved with more intents, actions and responses.
-  The message from WhatsApp user was sent to the Flask server which in turn directed the message to dialogflow, which processed the request, did query understanding, query classification and returned the most probable response (default if not part of training samples).

### Information retrieval for news

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/news.gif" width=400> 
</p>

-  We used the NewsAPI and statsAPI and the webhook method of dialog flow to determine the country or county (Supported only for US right now) asked for in the query and retieve the relevant news for a county or state and stats of COVID cases.
-  The messages are sent as a combination of one synchronous response and several async response to the whatsapp user for a natural conversatinal "feel"

### Language detection and translation

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/translate.gif" width=400> 
</p>

-  We used Google traslate API to convert the message into the users base languge. For detecting the base language of the user we checked the github repo of translate API and took the code for detecting the language of the message.
-  Therefore, everytime the customer messages something, the language of the message is detected and the response is returned in the same language. This allows for chatting in different languages for fun too.  


## Challenges we ran into

<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/time.gif" width=400> 
</p>
Being a team of two, it was challenging to manage the time given the details and connections to be handled. From scraping data to developing the server, deploying it in cloud engine, integrating Dialogflow and translate api along with news api riding with Twilio whatapp sandbox was quite challenging.

Deciding on the idea was another challenge, but since we thought of all the use cases this product can have, we have stuck with it.

Setting deadlines and missing them, we tried making our own model while but were not completely successful in deploying it in GCP.

## Accomplishments that we're proud of
We are proud of deliver a fully functional and scalable AI buddy that can help American airline customers during their journey as well as act as a new channel for marketing.

We are proud of working together as a team and managing the stress of the competition as well as reaching our goal of building flybuddy.

## What we learned
We learnt to use different technologies during this hackathon including GCP's DialogFlow, Twilio WhatsApp Sandbox and CockroachDB. Having a limited amount of time and having to limit the features of our application pushed us to leverage the technologies to the fullest for the problem at hand. 

## What's next for flybuddy
Improving on the conversation model and adding more features into the buddy system. 
Integrating flybuddy with more messaging applications like Facebook messenger, Telegram to make it more accessible. 


<p align="center">
  <img src="https://github.com/purvimisal/flight-hack/blob/master/static/Screen%20Shot%202021-01-31%20at%2010.08.48%20AM.png"> 
</p>
