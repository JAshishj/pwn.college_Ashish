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

   So, the challenge asked us to read the flag present in the flag file using it's absolute path by using cat command, hence i opened the shell and used the cat command to read that file by adding it's absolute path as an argument in the cat command and got the flag.
   ```bash
   hacker@commands~catting-absolute-paths:~$ cat /flag
   pwn.college{MGshbh1EDuDtGUQXyxSSv5J1v_w.QX5ETO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that cat command is used to read a file by adding it's path as an argument and it can concatenate multiple file if provided with multiple arguments and that the path can either be relative or absolute.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
