# **1.<ins>Becoming root with su</ins>**:-
   This challenge (and only this challenge) does have a root password. That password is `hack-the-planet`, and you must provide it to `su` to become root! Go do that, and read the flag!
## My solve:-
   **My flag** :-`pwn.college{8eVBc1zqnFyQcOsl0Myv5TB8Zq7.QX1UDN1wCNxAzNzEzW}`

   So, the challenge asked us to become the root by using `su` command and providing it with the root password, hence i opened the shell and used the `su` command and provided it with the root password i.e `hack-the-planet` and then catted the `/flag` as the flag of all challenge is stored there and got the flag.
   ```bash
   hacker@users~becoming-root-with-su:~$ su
   Password:
   root@users~becoming-root-with-su:/home/hacker# cat /flag
   pwn.college{8eVBc1zqnFyQcOsl0Myv5TB8Zq7.QX1UDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that oftentimes, we, as the owner of your computer, need to use root access to administer it. Becoming root is a fairly common action that Linux users take, and there are two utilities that exist for this purpose: `su` and `sudo`. I also came to know that `su` (the substitute user command) is not typically used to elevate to root access anymore, but it is an elegant utility from a more civilized time, and that because it has the SUID bit set, `su` runs as root. Running as root, it can start a root shell and that `su` is discerning: before allowing the user to elevate privileges to root, it checks to make sure that the user knows the root password, this check against the root password is what obsoletes `su`. Modern systems very rarely have root passwords, and different mechanisms are used to grant administrative access.

### Refference :-
   None


# **2.<ins>Other users with su</ins>**:-
   In this challenge, you must switch to the `zardus` user and then run `/challenge/run`. Zardus' password is `dont-hack-me`.
## My solve:-
   **My flag** :-`pwn.college{UWoC933MXPymWyhA7wAtFJVeeoS.QX2UDN1wCNxAzNzEzW}`

   So, the challenge asked us to witch to the `zardus` user and then run `/challenge/run`, hence i opened thel shell and used the `sh` command and passed `zardus` as the argument to change to that user and proided it's password provided n the challenge and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@users~other-users-with-su:~$ su zardus
   Password:
   zardus@users~other-users-with-su:/home/hacker$ /challenge/run
   Congratulations, you have become Zardus! Here is your flag:
   pwn.college{UWoC933MXPymWyhA7wAtFJVeeoS.QX2UDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that with no arguments, `su` will start a root shell (after authenticating with root's password). However, you can also give a username as an argument to switch to that user instead of root.

### Refference :-
   None


# **3.<ins>Cracking passwords</ins>**:-
   The challenge gives us a leak of `/etc/shadow` in `/challenge/shadow-leak`. Crack it (this could take a few minutes), `su` to `zardus`, and run `/challenge/run` to get the flag!
## My solve:-
   **My flag** :-`pwn.college{UYCjHtVi3sWDKCLs5Upx2exTd4t.QX3UDN1wCNxAzNzEzW}`

   So, the challenge asked us to crack the leak  of `/etc/shadow` in `/challenge/shadow-leak` and then `su` to `zardus` and run `/challenge/run`, hence i opened the shell and ran `john`, provided the path of the leak `/challenge/shadow-leak` and `su` to the `zardus` by providing the password that i got and then ran `/challenge/run` and got the flag.
   ```bash
   hacker@users~cracking-passwords:~$ john /challenge/shadow-leak
   Created directory: /home/hacker/.john
   Loaded 1 password hash (crypt, generic crypt(3) [?/64])
   Press 'q' or Ctrl-C to abort, almost any other key for status
   aardvark         (zardus)
   1g 0:00:00:20 100% 2/3 0.04916g/s 286.2p/s 286.2c/s 286.2C/s Johnson..buzz
   Use the "--show" option to display all of the cracked passwords reliably
   Session completed
   hacker@users~cracking-passwords:~$ su zardus
   Password:
   zardus@users~cracking-passwords:/home/hacker$ /challenge/run
   Congratulations, you have become Zardus! Here is your flag:
   pwn.college{UYCjHtVi3sWDKCLs5Upx2exTd4t.QX3UDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that passwords used to be stored in `/etc/passwd`, but because `/etc/passwd` is a globally-readable file, this is not good for passwords, these were moved to `/etc/shadow`.I also learned that the passwords are one-way-encrypted (hashed) and then stored, if wehave the hashed value of the password, you can crack it! Even though `/etc/shadow` is, by default, only readable by root, leaks can happen! For example, backups are often stored, unencrypted and insufficiently protected, on file servers, and this has led to countless data disclosures.If a hacker gets their hands on a leaked `/etc/shadow`, they can start cracking passwords and wreaking havoc. The cracking can be done via the famous John the Ripper,i.e by using `john`. 

### Refference :-
   None


# **4.<ins>Using sudo</ins>**:-
   The challenge will give you `sudo` access, and you will use it to read the flag.  
## My solve:-
   **My flag** :-`pwn.college{A5yaGyMLYgTsU-BrqxdC8fCp22e.QX4UDN1wCNxAzNzEzW}`

   So, the challenge asked us to use the `sudo` access and get the flag,as there were no other instructions i opened the shell and listed all the files in the root by using `sudo ls` then i catted the files which i thought would have the flag but the flag they gave were not the real flags and finally i got the real flag in the `not-the-flag` file.
   ```bash
   hacker@users~using-sudo:~$ sudo ls
   COLLEGE  PWN  cat  echo  f  instructions  myfile  myflag  not-the-flag  pwn  pwn_text.txt  temp.txt  the-flag
   hacker@users~using-sudo:~$ sudo cat not-the-flag
   pwn.college{A5yaGyMLYgTsU-BrqxdC8fCp22e.QX4UDN1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that in the olden days, a typical Linux system had a root password that administrators would use to `su` to root. But root passwords are a pain to maintain, they (or their hashes!) can leak, and they don't lend themselves well to larger environments. To address this, in recent decades, the world has moved from administration via `su` to administration via `sudo`, and unlike `su`, which defaults to launching a shell as a specified user, `sudo` defaults to running a command as root and also unlike `su`, which relies on password authentication, `sudo` checks policies to determine whether the user is authorized to run commands as root and these policies are defined in `/etc/sudoers`. 

### Refference :-
   None
