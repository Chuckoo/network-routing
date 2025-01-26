Project Proposal

Is the popularity of Wikipedia articles contagious ?

Abstract

Wikipedia stands as the sixth most visited website globally, attracting a diverse audience. The articles within Wikipedia form an intricate network through numerous hyperlinks interconnecting them. This project investigates the correlation between the popularity of Wikipedia articles and the popularity of their interconnected neighboring articles, as measured by the Google PageRank algorithm. 
In this study, "popularity" is defined in terms of the pageviews received by an article. The primary question addressed is whether a relationship exists between the popularity of a Wikipedia article and the popularity of its adjacent hyperlink articles, utilizing a suitable algorithm. Notably, PageRank reflects the importance of a page based on the number and popularity of pages that link to it and the overall structure of the interconnected network.
The methodology involves adopting a graphical approach, where selected subsets of Wikipedia (outlined in “Data and Tools”) are treated as directed graphs. In this representation, articles are depicted as nodes, and hyperlinks serve as edges. The focus is on understanding the dynamics of popularity within the Wikipedia ecosystem through the lens of graph theory and PageRank, shedding light on the interconnected nature of information dissemination within this widely accessed knowledge platform.

Problem Statement 

Problem: This research tries to address the issue of understanding the interrelationship between articles within Wikipedia, investigating facets such as association, correlation, and causality. The central problem at hand is the determination of how the popularity of one Wikipedia article may impact the popularity of another. The investigation necessitates an examination of the influence of hyperlinks, employing the PageRank algorithm as a crucial metric. The challenge lies in the validation of this influence by comparing PageRank values with the actual pageviews of specific articles, aiming to provide insights into the intricate dynamics of popularity within the Wikipedia ecosystem.

Input: Selected subsets of Wikipedia articles, where the selected subsets both represent pages that are prone to and unaffected by fluctuation in views. For example, celebrity pages are more prone to sudden influx of views due to current events, while history and math theorem pages are generally unaffected by time. 

Desired Output: An understanding of the correlation between the popularity of a Wikipedia article and the popularity of its neighbors, giving insight regarding the several controlled factors involved in research to allow for comprehensive analysis of the chemical reactions between Wikipedia articles.

Previous and Relevant Work
Although there are previous research papers dedicated to exploring Wikipedia through similar lenses, there is nevertheless a lack of research with the same objective, making it challenging to design a streamlined research process on our own. One such paper [2] discusses the popularity as the number of edits made to a page and how it is affected by the granularity of the particular article. We have adopted this to find out if this categorization has the same outcome when we define popularity to be the number of pageviews. 
Another paper [5]  discusses the importance of the first link network and defines the first link as the article’s closest neighbor. However, we set out to find the correlation of the articles with all its neighbors (All the hyperlinks contained in the article). This will give us a broader view in figuring out the flow of popularity influence in a Wikipedia network.

Data and tools

Wikipedia Categories: South American history stubs‎, Ancient Greece stubs, Indian Artists‎. We selected the first two categories because they're likely to remain consistent over time, since they're about history. We wanted to see if the correlation still holds true in the Indian Artists category, even though it's dynamic and may have more edits and added articles.

Wikipedia Python API: We utilize the Wikipedia Python API to collect data from the categories mentioned above. This enables us to browse through subcategories and obtain all the pages associated with them. We retrieve several details including titles, wiki-links, article IDs, and view counts within the category, and store them in JSON format.

Python NetworkX: We utilize the Python NetworkX library to build and examine the directed graph network. This allows us to analyze the properties and relationships among popular articles and their influence on neighboring articles.

Python data manipulation tools: We will utilize NumPy and Pandas for implementing PageRank due to their efficient handling of matrix operations and data manipulation, facilitating the computation and organization of data necessary for the algorithm's execution.

Google PageRanking: We utilize the Google PageRank algorithm to rank Wikipedia articles using inbound link quality(measured by the popularity of the pages linking a particular page). This method accounts for popularity and importance within our selected category, providing a comprehensive ranking system.

*We cannot use huggingface dataset because it does not contain information that we require, like hyperlinks and category.
