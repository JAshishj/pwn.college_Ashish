# **1.<ins>The root</ins>**:-
   The challenge asks us to get the flag by invoking the pwn program by using it's absolute path.

## My solve:-
   **My flag** :-`pwn.college{AUhJazBtOvY4jD7pVzGGS2eEEGK.QX4cTO0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the pwn using it's absolute path hence, I opened the shell and enter the path /pwn to invoke the program and got the flag.
   ```bash
    hacker@path~the-root:~$ BOOM!!!
   Here is your flag:
   pwn.college{AUhJazBtOvY4jD7pVzGGS2eEEGK.QX4cTO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that there are 2 types of paths:- 1.absolute path and 2.relative path and that / is the root directory.I also learned how to invoke a program by using it's absolute path.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
  
  # **2.<ins>Program and absolute paths</ins>**:-
 The challenge asks us to get the flag by invoking the run program by using it's absolute path which is in the challenge directory which in turn is in the root directory.
    
## My solve:-
   **My flag** :-`pwn.college{MuwmaHtivXp9dOlCKzHtB1DGJH_.QX1QTN0wCNxAzNzEzW}`

   So,the challenge asks us to get the flag by invoking the run program by using it's absolute path hence, I opened the shell and entered the path /challenge/run to invoke the progrm and got the flag.
   ```bash
    hacker@hello~program-and-absolute-paths:~$/challenge/run
   Correct!!!
   /challenge/run is an absolute path! Here is your flag:
   pwn.college{MuwmaHtivXp9dOlCKzHtB1DGJH_.QX1QTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learened that many directory can be inside one another but all will be atlast be in the root directory.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
