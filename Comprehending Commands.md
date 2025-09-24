# **1.<ins>Cat: not the pet, but the command</ins>**:-
   The challenge asks us to read the flag which has been copied to the flag file in our home directory by using the `cat` command. 
## My solve:-
   **My flag** :-`pwn.college{8omhWineoybnC5Ja8qaWLdu5hqa.QXxcTN0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the flag file which is present in our home directory, hence i opened the shell and used the `cat` command to read that file by adding it's relative path as an argument in the `cat` command and got the flag.
   ```bash
   hacker@commands~cat-not-the-pet-but-the-command:~$ cat ./flag
   pwn.college{8omhWineoybnC5Ja8qaWLdu5hqa.QXxcTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `cat` command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **2.<ins>Catting absolute paths</ins>**:-
   The challenge asks us to read the flag which is present in the flag file by using the `cat` command and entering it's absolute path in the argument. 
## My solve:-
   **My flag** :-`pwn.college{MGshbh1EDuDtGUQXyxSSv5J1v_w.QX5ETO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the flag file by using it's absolute path in the `cat` command, hence i opened the shell and used the `cat` command to read that file by adding it's absolute path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~catting-absolute-paths:~$ cat /flag
   pwn.college{MGshbh1EDuDtGUQXyxSSv5J1v_w.QX5ETO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `cat` command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments and that the path can either be relative or absolute.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   # **3.<ins>More catting practice</ins>**:-
   The challenge asks us to read the flag which is present in some directory by using the `cat` command and entering it's absolute path in the argument, and it  also says that we can not change the directories by using the `cd` command. 
## My solve:-
   **My flag** :-`pwn.college{sLTitXy-UlO-Sk_Sldzb50g8FrZ.QXwITO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in some directory by using it's absolute path in the `cat` command without changing directories, hence i opened the shell where it told me that the flag is in the file `/usr/lib/flag` , so i used the `cat` command to read that file by adding it's absolute path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~more-catting-practice:~$ cat /usr/lib/flag
   pwn.college{sLTitXy-UlO-Sk_Sldzb50g8FrZ.QXwITO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `cat` command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments and that the path can either be relative or absolute.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   # **4.<ins>Grepping for a needle in a haystack</ins>**:-
   The challenge asks us to find the flag present in the hundred thousand lines of text present in the `/challenge/data.txt` file by using the `grep` command, also the challenge also gave us a hint that all the flag starts from pwn.college.
## My solve:-
   **My flag** :-` pwn.college{Awc0LVaQFgdu0XUTzewWhISPH4I.QX3EDO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the hundred thousand lines of text present in the `/challenge/data.txt` file by using the `grep` command, hence i opened the shell and by using the hint i used the `grep` command to find all the words containing the pwn.college and got the flag.
   ```bash
   hacker@commands~grepping-for-a-needle-in-a-haystack:~$ grep pwn.college /challenge/data.txt
   pwn.college{Awc0LVaQFgdu0XUTzewWhISPH4I.QX3EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that it is difficult to read specific parts requiered to us in large files by using `cat`, instead of it we could use the `grep` command which takes two arguments those are:- string_name and the path of the file , then it will search the file and provides us with all the string containing the specified word.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
   

 # **5.<ins>Comparing files</ins>**:-
   The challenge asks us to find the flag by using the diff command on the 2 files of `/challenge` that is `/challenge/decoys_only.txt`:- which contains 100 fake flags and `/challenge/decoys_and_real.txt`:- contains all 100 fake flags plus the one real flag.
## My solve:-
   **My flag** :-`pwn.college{0WtSR3ojHcA-G1n7AlVyud8ChGM.01MwMDOxwCNxAzNzEzW}`

   So, the challenge asked us to find the flag by using the `diff` command on the 2 files of `/challenge`, hence i open the shell and use the diff command on `/challenge/decoys_only.txt` and `/challenge/decoys_and_real.txt`, and get the flag.
   ```bash
   hacker@commands~comparing-files:~$ diff /challenge/decoys_only.txt /challenge/decoys_and_real.txt
   67a68
   > pwn.college{0WtSR3ojHcA-G1n7AlVyud8ChGM.01MwMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to find the difference between two files by using the `diff` command which takes the path of files as an argument and gives what all difference are present between along with the line number on which the change is present on and also `<` followed by what is present before and `>` followed by what it became after.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


 # **6.<ins>Lisiting files</ins>**:-
   The challenge asks us to find the flag which is present in the `/challenge` directory with some random name using the `ls` command to get it's name and then invoke it.
## My solve:-
   **My flag** :-`pwn.college{Me9Gq2JhadYDXpfmYqghND7gJoK.QX4IDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `ls` command to list the files of the `/challenge` directory and then invoke that file to get thf flag, hence i opened the shell and entered the `ls` command and used the path `/challenge` an an argument and got the name of file which contains the flag i.e `7281-renamed-run-26752  DESCRIPTION.md` and then i invoked this file in the same way i did `/challenge/run` and got the key.
   ```bash
   hacker@commands~listing-files:~$ ls /challenge
   7281-renamed-run-26752  DESCRIPTION.md
   hacker@commands~listing-files:~$ /challenge/7281-renamed-run-26752  DESCRIPTION.md
   Yahaha, you found me! Here is your flag:
   pwn.college{Me9Gq2JhadYDXpfmYqghND7gJoK.QX4IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to find the list of files and other directories in a directory `ls` command is used which takes the path of the directory as the argument, i also so learned that if no argument is provided then it takes the current directory as the argument and lists all the files and other directories present in it.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **7.<ins>Touching files</ins>**:-
   The challenge asks us to create two files `/tmp/pwn`and `/tmp/college` by using the `touch` command, and then invoke the `/challenge/run` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{cBGYgTMoTFC4RB0-0nUYdJX5Pdo.QXwMDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `touch` command to create two files i.e `/tmp/pwn`and `/tmp/college`, and then invoke the `/challenge/run` to get the flag, hence i opened the shell and create the two files using the `touch` command and then invoked `/challenge.run` and got the flag.
   ```bash
   hacker@commands~touching-files:~$ touch /tmp/pwn
   hacker@commands~touching-files:~$ touch /tmp/college
   hacker@commands~touching-files:~$ /challenge/run
   Success! Here is your flag:
   pwn.college{cBGYgTMoTFC4RB0-0nUYdJX5Pdo.QXwMDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to create new files we can use the `touch` command which takes the name or path along with the name of the file that we want to create as the argument, also i learned that the file will be always created in the current directory if use only the name and if we use the name along with the path the it will be created in the specified place.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **8.<ins>Removing files</ins>**:-
   The challenge asks us to delete the `delete_me` file which will be present in our home directory using the `rm` command, and then invoke the `/challenge/run` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{wVQZ9jl3IIpdwEGfsSpZxDyyErB.QX2kDM1wCNxAzNzEzW}`

   So, the challenge asked us to use the `rm` command to delete the `delete_me` file, and then invoke the `/challenge/run` to get the flag, hence i opened the shell and as we always start in the home directory i directly deleted the `delete_me` file by usind `rm` command and entering the file as the argument and then invoked `/challenge/run` and got the flag.
   ```bash
   hacker@commands~removing-files:~$ rm delete_me
   hacker@commands~removing-files:~$ /challenge/check
   Excellent removal. Here is your reward:
   pwn.college{wVQZ9jl3IIpdwEGfsSpZxDyyErB.QX2kDM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to delet files we can use the `rm` command which takes the name of the file that we want to delete as the argument, also i learned that the only the files present in the current directory can be deleted.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).   


# **9.<ins>Moving files</ins>**:-
   The challenge asks us to `/flag` file into `/tmp/hack-the-planet` using the `mv` command, and then run the `/challenge/check` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{g0AfgYPHJBT16vrX2lymHynLGiw.0VOxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to use the `mv` command to move the `/flag` to `/tmp/hack-the-planet`, and then run the `/challenge/check` to get the flag, hence i opened the shell and  moved the `/flag` to `/tmp/hack-the-planet` file by usind `mv` command and entering the file path as the argument and then ran `/challenge/check` and got the flag.
   ```bash
   hacker@commands~moving-files:~$ mv /flag /tmp/hack-the-planet
   Correct! Performing 'mv /flag /tmp/hack-the-planet'.
   hacker@commands~moving-files:~$ /challenge/check
   Congrats! You successfully moved the flag to /tmp/hack-the-planet! Here it is:
   pwn.college{g0AfgYPHJBT16vrX2lymHynLGiw.0VOxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to move files we can use the `mv` command which takes the name or path of the file that we want to move as the argument where the first argument is the source and the second is the destination, also i learned that if the source file exists and the destination file does not then the source file will be renamed to the destination file, if the destination already exists then it will be overwritten, if source is a file and destination is a directory,source file will be moved into that directory.  
   
   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC). 


   # **10.<ins>Hidden files</ins>**:-
   The challenge asks us to find the flag which is present in a hidden dot-prepended file in `/` directory by using the `ls` command along with `-a` flag.
## My solve:-
   **My flag** :-`pwn.college{MPVuO5Hv11NB1B_HvCZAbkiGkO3.QXwUDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `ls` command with `-a` flag to find the file in which the flag is present as a hidden dot-pretended file in `/`, hence i opened the shell and  used the `ls -a` command which gave me a file called `.flag-141632437824762` along with other files as it contained flag in it's name i thought that the flag should be present in it hence i used the `cat` command to read it and got the flag.
   ```bash
   hacker@commands~hidden-files:~$ ls -a /
   .   .dockerenv             bin   challenge  etc   lib    lib64   media  nix  proc  run   srv  tmp  var
   ..  .flag-141632437824762  boot  dev        home  lib32  libx32  mnt    opt  root  sbin  sys  usr
   hacker@commands~hidden-files:/$ cat ./.flag-141632437824762
   pwn.college{MPVuO5Hv11NB1B_HvCZAbkiGkO3.QXwUDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `ls` command does not show the files that start with a `.`, and inorder to view them we have to use the `-a` flag along with the `ls` command.
   
   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC). 
