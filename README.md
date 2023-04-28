# wikipedia
You can get some information from wikipedia post and then upload it somewhere.
Work with wikipedia from python. URL,Title,Text ...
In my case I search for food post and ; print(data) You will get Json output:

{'batchcomplete': '', 'query': {'normalized': [{'from': 'food', 'to': 'Food'}], 'pages': {'10646': {'pageid': 10646, 'ns': 0, 'title': 'Food', 'extract': "Food is any substance consumed by an organism for nutritional support. Food is usually of plant, animal, or fungal origin, and contains essential nutrients, such as carbohydrates, fats, proteins, vitamins, or minerals. The substance is ingested by an organism and assimilated by the organism's cells to provide energy, maintain life, or stimulate growth. Different species of animals have different feeding behaviours that satisfy the needs of their metabolisms that have evolved to fill a specific ecological niche within specific geographical contexts.\nOmnivorous humans are highly adaptable and have adapted to obtain food in many different ecosystems. The majority of the food energy required is supplied by the industrial food industry, which produces food with intensive agriculture and distributes it through complex food processing and food distribution systems. This system of conventional agriculture relies heavily on fossil fuels, which means that the food and agricultural system is one of the major contributors to climate change, accountable for as much as 37% of total greenhouse gas emissions.The food system has significant impacts on a wide range of other social and political issues including: sustainability, biological diversity, economics, population growth, water supply, and food security. Food safety and security are monitored by international agencies like the International Association for Food Protection, World Resources Institute, World Food Programme, Food and Agriculture Organization, and International Food Information Council.\n\n", 'thumbnail': {'source': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/500px-Good_Food_Display_-_NCI_Visuals_Online.jpg', 'width': 500, 'height': 333}, 'pageimage': 'Good_Food_Display_-_NCI_Visuals_Online.jpg'}}}}



print("Title: ", article["title"])   #title
print("Text: ", article["extract"])  #text
print("Image URL: ", article['thumbnail']["source"]) #image


If you want to download image you simply can use


with open('image.jpg', 'wb') as handler:
    handler.write(article['thumbnail']["source"])
