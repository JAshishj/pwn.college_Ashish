# **1. <ins>Intro to the commands</ins>**:-
   The challenge asks us to enter the hello command in the shell to get the flag.
   
   ## My solve:-
   My flag :- pwn.college{sx-8ZC15Stsq73B3AYwgptYt-E5.QX3YjM1wCNxAzNzEzW}
   
   Basically,the challange asked us to get the flag by entering the command hello in the shell so i opened the shell and entered the hello command and got the flag.
   ```bash
      hello
      pwn.college{sx-8ZC15Stsq73B3AYwgptYt-E5.QX3YjM1wCNxAzNzEzW}
  ```

## What i learned:-
  I learned how to run basic commands in shell and that commands in linux is case sensitive.

## Refference :-
  [pwn.college Linux Luminarium-1.The command line](https://youtu.be/g_85EVO3IC0?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


# **2.<ins>Intro to the arguments</ins>**:-
 The chalenge asks us to enter the hello command in the shell with a single argument of hackers to get the flag.
 
## My solve:-
   **My flag** :-pwn.college{YSB3qxKUvhU1NP5cNaCBdBU7aeS.QX4YjM1wCNxAzNzEzW}
 
   Basically,the challange asked us to get the flag by entering the command hello along with a single argument hackers in the shell, so i opened the shell and entered the hello hackers command and got the flag.
   ```bash
   hello hackers
   pwn.college{YSB3qxKUvhU1NP5cNaCBdBU7aeS.QX4YjM1wCNxAzNzEzW}
   ```

## What i learned:-
   I learned that commands can have arguments and we can enter it by giving a space after the command.

## Refference :- 
[pwn.college Linux Luminarium-1.The command line](https://youtu.be/g_85EVO3IC0?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).

  # 3.**<ins>Command history</ins>**:-
   The chalenge asks us to get the flag which is injected into our history.  
   
   ## My solve:- 
   **My flag**:-  pwn.college{0NBDO0vDI86DbAcfzzaOwvcgsOR.0lNzEzNxwCNxAzNzEzW}

   Basically,the challenge asked us to get the flag injected in our history so i opened the shell and used the history command and got the flag.

  ```bash
  history
  1  hello
  2  hello hackers
  3  the flag is pwn.college{0NBDO0vDI86DbAcfzzaOwvcgsOR.0lNzEzNxwCNxAzNzEzW}
  4  history
 ```

### What i learned:-
   I learned that the shell saves a history of every command that we invoke and that we can invoke it by using the history command.

## Refference :-
[pwn.college Linux Luminarium-1.The command line](https://youtu.be/g_85EVO3IC0?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC),
             [Basic shell commands](https://bash.cyberciti.biz/guide/Shell_commands).
             
