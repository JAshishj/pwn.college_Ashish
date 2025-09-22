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
   I learened that many directory can be inside one another but all will  atlast be in the root directory.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **3.<ins>Position thy self</ins>**:-
   The challenge asks us to get the flag by invoking the /challenge/run program from a specific directory.

## My solve:-
   **My flag** :-`pwn.college{8hONncErtA4mtZC2JMepUg6ehBN.QX2QTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run program from a specific directory, hence i opened the shell and as i did not know to which directory i had to go i tried to invoke /challenge/run program using absolute path from the root directory the it showed that i was not in `/usr/share/doc/fontconfig` directory ,then i changed the directory to it by using the cd command and got the flag.
   ```bash
  hacker@paths~position-thy-self:/usr/share/doc/fontconfig$ /challenge/run
  Correct!!!
  /challenge/run is an absolute path, invoked from the right directory!
  Here is your flag:
  pwn.college{8hONncErtA4mtZC2JMepUg6ehBN.QX2QTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cd command is used to change directories and that the ~ symbol shown before now shows the current path of our shell .

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).   
   

# **4.<ins>Position elsewhere </ins>**:-
   The challenge asks us to get the flag by invoking the /challenge/run program from a specific directory.

## My solve:-
   **My flag** :-`pwn.college{o4JxTqg5-k8r7TbFkw9kcB_qNry.QX3QTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run program from a specific directory, hence i opened the shell and from the above challenge i had come to know that we would get the directory to which i had to go if i invoke /challenge/run program using absolute path from the root directory then it showed that i was not in `/proc/131/fd` directory ,and then i changed the directory to it by using the cd command and got the flag.
   ```bash
   hacker@paths~position-elsewhere:~$ cd /proc/131/fd
   hacker@paths~position-elsewhere:/proc/131/fd$ /challenge/run
   Correct!!!
   /challenge/run is an absolute path, invoked from the right directory!
   Here is your flag:
   pwn.college{o4JxTqg5-k8r7TbFkw9kcB_qNry.QX3QTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cd command is used to change directories and that the ~ symbol shown before now shows the current path of our shell .

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).   


   # **5.<ins>Position yet elsewhere</ins>**:-
   The challenge asks us to get the flag by invoking the /challenge/run program from a specific directory.

## My solve:-
   **My flag** :-`pwn.college{QQ-tTvoyO_ovHugJGVT6AUMk_Uz.QX4QTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run program from a specific directory, hence i opened the shell from the above challenge i had come to know that we would get the directory to which i had to go if i invoke /challenge/run program using absolute path from the root directory then it showed that i was not in `/sys/kernel` directory ,and then i changed the directory to it by using the cd command and got the flag.
   ```bash
   hacker@paths~position-yet-elsewhere:~$ cd /sys/kernel
   hacker@paths~position-yet-elsewhere:/sys/kernel$ /challenge/run
   Correct!!!
   /challenge/run is an absolute path, invoked from the right directory!
   Here is your flag:
   pwn.college{QQ-tTvoyO_ovHugJGVT6AUMk_Uz.QX4QTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cd command is used to change directories and that the ~ symbol shown before now shows the current path of our shell .

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).   
