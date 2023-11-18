# CODSOFT
This repository is created to show the progress of the AI intenship provided by ''CODSOFT''

INTRODUCTION:
       Artificial Intelligence (AI) is revolutionizing society through advanced algorithms and machine learning. Its 
applications in data analytics, autonomous systems, and decision-making have become ubiquitous. 
However, ethical considerationsand regulatory frameworks are imperative to ensure responsible AI deployment. The future holds 
promise for further advancementsin deep learning and robotics, demanding a balanced approach to harness AI's potential for 
societal benefit.

There are many applications of AI but for this project the focus will be on three tasks. They are:

         TASK 1: CREATING A SIMPLE CHATBAOT THAT RESPOONDS TO USER INPUTS USING IF-ELSE STATEMENTS OR PATTERN MATCHING 
                TECHNIQUES
         TASK 2: IMPLEMENTING A TIC-TAC-TOE GAME WITH AI
         TASK 4: CREATING A SIMPLE RECOMMENDATION SYSTEM OF MOVIES

OVERVIEW:


TASK 1:   CHAT BOT AI


A chatbot is usually designed to simulate a conversation with human users They can be rule based, fallowing predefined scripts or they can be advanced
building a chatbot:
STEP 1: Define User Input Patterns:
    Identify common phrases or keywords users might input. This could include greetings, inquiries about specific topics, or requests for information.

STEP 2: Craft Responses:
    Determine the responses you want the chatbot to provide based on the identified patterns. These responses could be straightforward answers or more complex explanations, depending on the nature of your chatbot.

STEP 3: Research Content:
    Conduct research to gather relevant information or content for the responses. This step is crucial if your chatbot is expected to provide accurate and informative answers.

STEP 4: Incorporate Research into Responses
Integrate the researched content into your responses. This ensures that your chatbot provides valuable and contextually relevant information to users.

 STEP 5: Handle Variations:
 Consider potential variations in user input. Account for different ways users might express the same intent by refining your if-else statements or using techniques like string matching or regular expressions.

STEP 6: Implement Interaction Loop:
    Create a loop that allows users to interact with the chatbot continuously. Prompt the user for input, process their input using your if-else statements, and provide appropriate responses. Include an exit condition to end the interaction.

STEP 7: Test and Iterate:
    Test your chatbot with various inputs to ensure it responds correctly and handles different scenarios. Iterate on your design based on user interactions and feedback.


TASK 2:   TIC-TAC-TOC WITH AI


         This can be accomplished using the minimax algorithm. 
The min max algorithm

Minimax is a recursive algorithm that is used to choose an optimal move for a player assuming that the other player is also playing optimally. It is used in games such as tic-tac-toe, Go, chess, isola, checkers and various other two-player games. Such games are known as games of perfect information as it is possible to see all the possible moves of a particular game. There can be two-player games, which are not of perfect information such as Scrabble as the move of the opponent cannot be predicted.

The players in the game are referred to as MAX and MIN. MAX represents the person who is trying to win the game and hence maximise his or her score. MIN represents the opponent who is trying to minimise the score of MAX.

This algorithm is used to look ahead and decide which move to make first. If the game space is small enough the entire space can be generated and the leaf nodes can be allocated a win (1) or loss (0) value.

These values might be propagated back up the tree to decide which node to use. In propagating the values back up the tree, a MAX node is appointed the maximum value of all its children and MIN node is appointed the minimum values of all its children.

ALGORITHM

Step 1: In case of search reaching its limit, the static value of the current position relative to the appropriate player is calculated. The result is reported.

Step 2: Otherwise, if the level is a minimising level, use the minimax on the children of the current position. The minimum value of the results is reported here

Step 3: Also, if the level is a maximising level, use the minimax on the children of the current position. The maximum of the results is reported here.

Step 4: The utility values is calculated with the help of leaves considering one layer at a time until the root of the tree.

Step 5: Eventually, all the backed-up values reach to the root of the tree, that is, the topmost point. At that point, MAX is responsible for choosing the highest value.

Properties of minmax

• Complete: It is complete (if the tree is finite).
• Optimal: The minimax is optimal against an optimal opponent and is not optimal where it does not exploit opponent weakness against suboptimal opponent.
• Time complexity: The time complexity is defined as O(bm).
• Space complexity: The space complexity is written as O(bm) (depth-first exploration).


TASK 4:    RECOMMENDATION SYSTEM 


     Machine learning algorithms with some Natural Language Processing.study certain user patterns or behavior and based 
upon that they are able to recommend shows and movies to the user. To understand movie recommendations in a little depth we need to understand the two broad types of recommendation systems which are: Content Based and Collaborative based 
recommendation systems.

Collaborative filtering recommends items by leveraging of other users where as content based analyses the characteristics of items and the preferences of the user to make recommendations 

CONTENT BASED FILTERING:
This is basically how this algorithm works:

STEP 1: Item Representation:
Each item in the system is represented by a set of descriptors or features. For example, a movie might be described by 
features such as genre, director, and actors.

STEP 2: User Profile Creation:
The system builds a profile for each user based on their historical preferences. This profile includes weights for different features, indicating the user's preference strength for each feature. For instance, a user might heavily favor action and science fiction genres.

STEP 3:Feature Weighting:
    Features are assigned weights based on their importance to the user. This could be determined by analyzing the user's 
  interactions with items in the past. High weights are assigned to features that the user has shown a strong preference 

STEP 4: Scoring Items:
The system calculates a score for each item by combining the weights of the features present in the item's description with the corresponding weights in the user profile. This reflects how well the item matches the user's preferences.

STEP 5: Ranking and Recommendation:
Items are ranked based on their scores, and the system recommends the top-ranked items to the user. The higher the score, 
the more likely the item is to be of interest to the user.

STEP 6: Profile Updating:
    As the user interacts with the recommended items and provides feedback, the system updates the user profile to 
  continually refine the understanding of the user's preferences.
            
Advantages:

- it's adaptive. that means it can keep up with changes in user's intrest
- Items recommended to one user is not the same to the items recommended to other users
- it can capture specific interests of users can will even recommend niche , unpopular items



REFERENCES:

https://www.kaggle.com/tmdb/tmdb-movie-metadata

https://doi.org/10.1016/j.mlwa.2020.100006

https://doi.org/10.1080/15332861.2021.1966723

https://www.javatpoint.com/mini-max-algorithm-in-ai


https://www.kaggle.com/code/alexisbcook/getting-started-with-kaggle-competitions

https://www.turing.com/kb/content-based-filtering-in-recommender-systems










 
