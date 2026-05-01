README but also personal notes

Work in progress.

Became curious about how different news sites would portray the same events differently.
This formed a very crude idea about using RSS feeds to ingest news articles (Title, summary, content etc)
and use the python NLP library NLTK to have some fun with sentiment analysis.

Base idea is using RSS feeds to ingest simple news articles, and compare sentiment of title vs content.
I know this provides no real insight, im just trying to become familiar with the ingesting RSS feeds and
NLP libraries.

In progress/thoughts:
Comparisons across different news sites. 
	ie find same topic/event from two sources.

Topic/event selection
	create keyword store(probably just a csv for now) and have articles separated based on these keys, eg "Fuel prices"

Per outlet
	separation based on news source, get overall view of outlets tone, eg positive or all doom and gloom

make it all relat(ional)able
	schema and db with
		article(outlet, topic, content,title, sentiment)
		outlet(articles, topics, topicspecific sentitemnt)
	 	etc
	doing this first may make everything else simpler?
	
keyword matching alone will undoubtedly lead to mistakes
	do sorting manually ie tag articles with topics
	get some gaddah prompt engineering to do the tagging, ie ingest article and determine its topic. Ollama back?


