We chose Netflix movies as the topic for the Task 5. The attributes and examples of the topic are shown below:

**Attributes:** 

 1.  (ChildrenMovie: AdultMovie) 
 2. (ClassicMovie:ThrillerMovie)
 3. (AnimeMovie:NonAnimeMovie)
 4. (ComedyMovie:HorrorMovie)
 5. (WarMovie:RomanticMovie)
 6. (ShortMovie:LongMovie)
 7. (WatchOnceMovie:WatchMultipleMovie)
 8. (BadMovie:GoodMovie)
 9. (NonExpensiveMovie:ExpensiveMovie)
 10.(EducationalMovie:EntertainerMovie) 

**Examples:**

 1. RushHour
 2. Sully
 3. BicycleThieves
 4. Parasite
 5. AmericanSniper
 6. SocialNetwork
 7. LordOfTheRings
 8. KingsMan
 9. Titanic
 10. IceAge 


**Cluster Example:**

![cluster](https://github.com/setu1421/CSC-791/blob/aadbaffc11bd3b514efc3a25115e468377903d30/repgrids/cluster.png)




**Similarities:**

 1. In the cluster, we can see similarities between attributes such as (WatchOnceMovie:WatchMultipleMovie) and (BadMovie:GoodMovie). The relation between these attributes is obvious as users will not watch a bad movie multiple times whereas users will watch a good movie multiple times.
 2. We have also seen similarities between attributes such as (ChildrenMovie:AdultMovie) and (AnimeMovie:NonAnimeMovie). The relation is obvious as children like to watch animation movies whereas adult likes to watch non-animation movies.
 3. We have seen BicycleThieves and Titanic movies are clustered together which can be because of both are classic good movies. This relation perfectly relates the taste of a user. Same relation goes for Social Network and Parasite movie as these movies are both related to society. 
 
 **Dissimilarities:**
 
 1. In the cluster, we have seen that there is a similarity between (NonExpensiveMovie:ExpensiveMovie) and (ClassicMovie:ThrillerMovie). But, this relation may not hold for large data as classic movies can also be expensive and a thriller movie can be non-expensive. We believe this relation will not hold when we provide larger dataset.


**Limitation:**

 - **Different Culture:** The three person whom we interviewed may not be of the same culture. Some of them may no like war movies as their parent did not let them to see those movie from childhood. So, we may have cultural bias in our dataset.
 - **Unseen Movies:** The three person may not see all the movies as they may give response based on what they have heard or seen some clips from youtube.


**Conclusion:** The tools seems to provide interesting outputs as we can see some obvious relations. Having more data, we can resolve some dissimilarities that we found in the cluster. 
