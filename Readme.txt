README:

Here we have a 2-D matrix having characters only '#' or '.'

Given: for each face, the paint required is 1 litre
and also when any '#' comes, it means it has 4 four walls.
Steps for Program:

(1) we will move on the perimeter of the 2-D matrix and find whether the character is '#' or '.'.
(2) If the character is '#' and also the particular character is not in visited_list, Therefore we will add the count of amount of paint needed in litre.
(3) If the character is '.', we will enter the 2-D matrix and traverse all the elements in that particular direction.
	(i) If any character is '#' we will add amount 0f paint needed for that '#'
	(ii) If the character is '.', we will move forward 
(4) We will follow step 2-3 untill all the perimeter is traversed by us.

(5) The final amount_of_paint will be the answer.