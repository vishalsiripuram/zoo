# zoo-design •
Constraints

• 0 < number of animals of each type <= 20

• 0 < max area for each animal type <= 500

• 0 < total area of land on which zoo is to be built <= 1000

• 0 < min area required by individual animals <= 15

• 0 < price of each type of enclosure <= 10000

• Area of each type of enclosure should be rounded off to the nearest integer

Input

• First line contains three space separated integers denoting the cost per square meter of building 
  the enclosure for each type of animals viz. herbivorous, carnivorous and aquatic respectively..

• Second line contains three space separated integers denoting the maximum area that can be allocated
  to each type of animal viz. herbivorous, carnivorous and aquatic respectively..
  
• Next three lines, each will contain two space separated integers M and N, for each type of animal viz.
  herbivorous, carnivorous and aquatic respectively, where M denotes minimum number of animals of that 
  type and N denotes minimum area required for that animal type..
  
• Last line contains an integer which represents the total area of land on which the zoo needs to be built

Output
Single integer containing the minimum cost required to build the zoo


Examples
Example 1
Input
10000 1000 1500
250 250 300
5 5
15 5
10 10
500
Output
837500
Explanation
·The cost of constructing the enclosure for herbivores is high. 
 However, since we need to accommodate 5 herbivores as per given constraints, a 25 sq. meter land will need to allocated for the herbivores.
·Since the cost of constructing the enclosure for carnivores is cheapest we are able to allocate them the maximum limit that we can allocate.
Thus we are allocating 250 sq. meters for carnivores.
·The remaining 225 sq. meters can thus be allocated to aquatics without violating any constraint.
·Thus the minimum cost of constructing the zoo adhering to all constraints is (25 * 10000 + 250 * 1000 + 225 * 1500) = 837500
