# **1.<ins>Cat: not the pet, but the command</ins>**:-
   The challenge asks us to read the flag which has been copied to the flag file in our home directory by using the cat command. 
## My solve:-
   **My flag** :-`pwn.college{8omhWineoybnC5Ja8qaWLdu5hqa.QXxcTN0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the flag file which is present in our home directory, hence i opened the shell and used the cat command to read that file by adding it's relative path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~cat-not-the-pet-but-the-command:~$ cat ./flag
   pwn.college{8omhWineoybnC5Ja8qaWLdu5hqa.QXxcTN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cat command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **2.<ins>Catting absolute paths</ins>**:-
   The challenge asks us to read the flag which is present in the flag file by using the cat command and entering it's absolute path in the argument. 
## My solve:-
   **My flag** :-`pwn.college{MGshbh1EDuDtGUQXyxSSv5J1v_w.QX5ETO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the flag file by using it's absolute path in the cat command, hence i opened the shell and used the cat command to read that file by adding it's absolute path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~catting-absolute-paths:~$ cat /flag
   pwn.college{MGshbh1EDuDtGUQXyxSSv5J1v_w.QX5ETO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cat command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments and that the path can either be relative or absolute.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   # **3.<ins>More catting practice</ins>**:-
   The challenge asks us to read the flag which is present in some directory by using the cat command and entering it's absolute path in the argument, and it  also says that we can not change the directories by using the cd command. 
## My solve:-
   **My flag** :-`pwn.college{sLTitXy-UlO-Sk_Sldzb50g8FrZ.QXwITO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in some directory by using it's absolute path in the cat command without changing directories, hence i opened the shell where it told me that the flag is in the file `/usr/lib/flag` , so i used the cat command to read that file by adding it's absolute path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~more-catting-practice:~$ cat /usr/lib/flag
   pwn.college{sLTitXy-UlO-Sk_Sldzb50g8FrZ.QXwITO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cat command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments and that the path can either be relative or absolute.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


   # **4.<ins>Grepping for a needle in a haystack</ins>**:-
   The challenge asks us to find the flag present in the hundred thousand lines of text present in the `/challenge/data.txt` file by using the grep command, also the challenge also gave us a hint that all the flag starts from pwn.college.
## My solve:-
   **My flag** :-` pwn.college{Awc0LVaQFgdu0XUTzewWhISPH4I.QX3EDO0wCNxAzNzEzW}`

   So, the challenge asked us to read the flag present in the hundred thousand lines of text present in the `/challenge/data.txt` file by using the grep command, hence i opened the shell and by using the hint i used the grep command to find all the words containing the pwn.college and got the flag.
   ```bash
   hacker@commands~grepping-for-a-needle-in-a-haystack:~$ grep pwn.college /challenge/data.txt
   pwn.college{Awc0LVaQFgdu0XUTzewWhISPH4I.QX3EDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that it is difficult to read specific parts requiered to us in large files by using cat, instead of it we could use the grep command which takes two arguments those are:- string_name and the path of the file , then it will search the file and provides us with all the string containing the specified word.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
   

 # **5.<ins>Comparing files</ins>**:-
   The challenge asks us to find the flag by using the diff command on the 2 files of `/challenge` that is `/challenge/decoys_only.txt`:- which contains 100 fake flags and `/challenge/decoys_and_real.txt`:- contains all 100 fake flags plus the one real flag.
## My solve:-
   **My flag** :-`pwn.college{0WtSR3ojHcA-G1n7AlVyud8ChGM.01MwMDOxwCNxAzNzEzW}`

   So, the challenge asked us to find the flag by using the diff command on the 2 files of `/challenge`, hence i open the shell and use the diff command on `/challenge/decoys_only.txt` and `/challenge/decoys_and_real.txt`, and get the flag.
   ```bash
   hacker@commands~comparing-files:~$ diff /challenge/decoys_only.txt /challenge/decoys_and_real.txt
   67a68
   > pwn.college{0WtSR3ojHcA-G1n7AlVyud8ChGM.01MwMDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to find the difference between two files by using the diff command which takes the path of files as an argument and gives what all difference are present between along with the line number on which the change is present on and also `<` followed by what is present before and `>` followed by what it became after.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
