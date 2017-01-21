# Logic and CSPs

This code was written for the course Elements of Artificial Intelligence (CSCI-B 551) at Indiana University handled by Professor David Crandall. Skeleton code was provided by the Professor to get us started with the assignment.


**What does the program do?** <br/>
* The program addresses the typical map coloring problem where no adjacent states are supposed to have the same color.
* In addition to that, yet another constraint called legacy states are added to the question.
* The legacy states retain the color that they are assigned.
* More details about the game can be found from this [link](https://github.com/manikandan5/MapColoring/blob/master/Question.pdf).

**How does it find it?** <br/>

* The program uses Arc Consistency with backracking to achieve the expected output.

Detailed explanation about how the code works and the reason why we chose this implementation could be found [here](https://github.com/manikandan5/MapColoring/blob/master/radio.py).
