**Notes:**

1. The problem ask us to find if a student can take all the courses from a list of pre-requisites pair. Return false if the student cannot take all the courses.  We are also given total number of courses. Courses are numbered/labeled as [0 - numCourses - 1]. Each pair in the prerequisites list is represented as: [0, 1] where in order to take course 0, you have to take course 1 first. OR course 1 is the pre-requisite of course 0. 0 -> 1.
2. The problem can be solved with 3 different approches, DFS, BFS and Topological Sort. Here we will only discuss and implement the DFS solution.
3. The intution to solve this problem is to recognize that this is a graph problem and the list of pre-requisites pairs is basically a list of edges in a graph. The other important thing is that, this list forms a directed graph. i.e in order to take course at 0-index we have to take the course at 1-index.
4. So with the given information we have to first create an adjacency list map. We can call it the PrereqMap where the keys is the course/vertex and value is a list of pre-requisite courses required to complete this course. If a course has no prequisites we will just have an empty list as its value. If the pre-requisite list is empty, it means we can complete this course without taking any other courses.
5. Once we have created our adjacency list map. We need to keep in mind that if there is a cycle in our graph it means that student would not be able to complete all the courses. Meaning a set of courses are pre-requsites of each other. In order to detect such a cycle we have to keep track of the visited courses along the current DFS path. So we will use a hashset to keep track of all the visited courses/vertices of the current path. Once we have explored the entire DFS path, then we backtrack and start removing courses/vertices from the hashset because now we are exploring a different DFS path.
6. There will be four major steps of our DFS function.
   1. Base Condition - If the current course in the visited hashset. It means we have detected a cycle, so we should simply return False.
   2. Base Condition - if the pre-requsite list in the PrereqMap is empty. It means we can take this course, so we will simply return True.
   3. Recursive Case - Now we process the current course by adding to the visited hashset and then recursively call the dfs function on all of its pre-requsite courses. We will simply return False if any of pre-requisite course cannot be completed within the loop.
   4. CleanUp Case - We will exit the loop only If we can complete all the pre-requisite courses of the current course. It means we have successfully explored an entire path of the DFS. Now we have to explore another path. So we have to do two things:

      1. Remove the current course from the visited hashset.
      2. Since we have exited the pre-req loop and we know that the current course can be completed. So we will set the value of this course to an empty list in our PrereqMap.
      3. After that we will simply return True from this DFS function.
7. Then we have to call this DFS on all of the courses one by one. We have call DFS on all the courses because it is possible that we have disconnected graph. We can have 2 or more disconnected graphs. Thats why we will run the DFS on all the courses in a loop. ProTip: For one connected graph, when run the DFS on next connected vertex/course that has all ready been processed, in that case our adjacency list PrereqMap will have its value set to an empty list. So we will simply shortcircut from the DFS function by simply return True and move on to next course.
8. Since we are visiting each and every course once "n" and we also process every edge "e" once as well. So the time complextiy of such a solution is O(n + e). We are also keeping track of the DFS path in a visited hashset, So the space complexity will O(n).