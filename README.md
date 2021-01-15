# flapjack
 ## Introduction
 Flapjack is a two player game played with a deck of poker cards. This project attempts to model the game to determine the best strategy to win the game. To do this, we use 3 different methods:
 1. empirical_analysis: Have 2 agents compete against each other using different strategies large number of times and analyse the results to determine the efficacy of each of the strategy.
 2. statistical_analysis: Model the data using theoretical statistics
 3. adversarial_agents: Use reinforcement leaning to train agents to compete and learn the best possible strategy

 ## Rules
* Each player each get one suit of black cards and one suit of red cards i.e. 26 cards each. Players draw cards at random from their own deck and they have to decide to continue drawing or to stop. Players can opt to stop at any point.
* Each black card drawn contributes to positive points while red card contributes to negative points.
* A's can be treated as either 1 or 11 (positive or negative depending on the colour of the suit).
* Points are converted to a "score" based on the score table.
* Players with the higher score win the game.
* Players go bust and automatically gets 0 score if at any point in the game draws > 25 points.

## Score Table

| Points  | Score  |
|---|---|
| <= 10  | = Points  |
| 11 <= x <= 15  | 10  |
| 16 <= x <= 25  | = Points  |
| > 25  | 0  |


## Strategies
Agents can only choose the score limit at which they would like to stop drawing a card. They cannot choose whether to draw the next individual card, this is predetermined by the limit.

## empirical_analysis
The empirical analysis concluded that  playing the >= 20 strategy is nash equilibrium thought the >= 21 strategy is a very close contender.

## statistical_analysis
TBC

## adversarial_agents
TBC
