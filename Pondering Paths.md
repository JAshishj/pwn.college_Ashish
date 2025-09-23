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


   # **6.<ins>Implicit relative paths, from /</ins>**:-
   The challenge asks us to get the flag by invoking the /challenge/run program by using it's relative path from the /(root) directory.

## My solve:-
   **My flag** :-`pwn.college{4H2dGBUbhS_Z-4uR025bzyAEprs.QX5QTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run using it's relative path from the /(root) directory hence, I opened the shell and changed my directory to /(root) directory by using the cd command and then i invoked the program using it's relative path and got the flag.
   ```bash
   hacker@paths~implicit-relative-paths-from-:/$ challenge/run
   Correct!!!
   challenge/run is a relative path, invoked from the right directory!
   Here is your flag:
   pwn.college{4H2dGBUbhS_Z-4uR025bzyAEprs.QX5QTN0wCNxAzNzEzW}
   ```

### What i learned:-
  I learned that relative path of a file does not start from /(root) directory,rather it is relative to our current working directory, and i also learned that this tyoe of path is also known as "naked" path.
   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   
   # **7.<ins>Explicit relative paths, from /</ins>**:-
   The challenge asks us to get the flag by invoking the /challenge/run program by using it's relative path using `.` from the /(root) directory.

## My solve:-
   **My flag** :-`pwn.college{cr1-SC-P75tWg2EWweZLX5X33M4.QXwUTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run using it's relative path by using `.` from the /(root) directory hence, I opened the shell and changed my directory to /(root) directory by using the cd command and then i invoked the program using `.` in it's relative path and got the flag.
   ```bash
   hacker@paths~explicit-relative-paths-from-:/$ ./challenge/run
   Correct!!!
   ./challenge/run is a relative path, invoked from the right directory!
   Here is your flag:
   pwn.college{cr1-SC-P75tWg2EWweZLX5X33M4.QXwUTN0wCNxAzNzEzW}
   ```

### What i learned:-
  I learned that relative path of a file does not start from /(root) directory,rather it is relative to our current working directory, and i also learned that `.`in a refers to the current directory and `..` refers to the parent directory in the path of a file and these can be used in the shell instead of the directory name.  

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


  # **8.<ins>Implicit relative path</ins>**:-
   The challenge asks us to get the flag by invoking the /run program by using it's relative path using `.` from the /challenge directory.

## My solve:-
   **My flag** :-`pwn.college{gx4cPaAbySVgPQlHJgXxrQCGt84.QXxUTN0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /run program using it's relative path by using `.` from the /challenge directory hence, I opened the shell and changed my directory to /challenge directory by using the cd command and then i invoked the program using `.` in it's relative path and got the flag.
   ```bash
  hacker@paths~implicit-relative-path:/challenge$ ./run
 Correct!!!
 ./run is a relative path, invoked from the right directory!
 Here is your flag:
 pwn.college{gx4cPaAbySVgPQlHJgXxrQCGt84.QXxUTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `.`in a refers to the current directory and `..` refers to the parent directory in the path of a file and these can be used in the shell instead of the directory name, i also learned that linux does not look into the current directory every time we run a "naked" path i.e a relative path without `.` or `..` as a safety precaution.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   
 # **9.<ins>Home sweet home</ins>**:-
   The challenge asks us to invoke /challenge/run with an argument which then will write the copy of the flag in the file we specified in the argument, also there were three constraints:-
 1.Your argument must be an absolute path.
 2.The path must be inside your home directory.
 3.Before expansion, your argument must be three characters or less.

## My solve:-
   **My flag** :-`pwn.college{gFUDl7T284dsOIPAj6IgYh5tWQL.QXzMDO0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag by invoking the /challenge/run with an arguments with 3 constraints hence, I opened the shell and entered the /challenge/run with an argument which fit all the constraints and the it gave me the flag.
   ```bash
   hacker@paths~home-sweet-home:~$ /challenge/run ~/f
   Writing the file to /home/hacker/f!
   ... and reading it back to you:
   pwn.college{gFUDl7T284dsOIPAj6IgYh5tWQL.QXzMDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that every user has a home directory ehich is typically under /home in the filesystem. In the dojo, you are the hacker user, and your home directory is /home/hacker and as we make our way through pwn.college, this is where we'll store most of your solutions, i also learned that the `~` in the shell is the current working directory, with ~ being shorthand for /home/hacker an that bash provides and uses this shorthand because most of our time will be spent in our home directory and thus, whenever bash sees ~ provided as the start of an argument in a way consistent with a path, it will expand it to your home directory, and i also came to know that the expansion of ~ is an absolute path, and only the leading ~ is expanded.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
