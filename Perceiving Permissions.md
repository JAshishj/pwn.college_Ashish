# **1.<ins>Changing file ownership</ins>**:-
   In this challenge we will practice changing the owner of the `/flag` file to the `hacker` user, and then read the flag. For this challenge only, I made it so that you can use `chown` to your heart's content as the hacker user (again, typically, this requires you to be root).
## My solve:-
   **My flag** :-`pwn.college{QHmrbAsxG299dUZpekUyA_dAu-L.QXxEjN0wCNxAzNzEzW}`

   So, the challenge asked us to change the owner of the `/flag` file to the `hacker` user, and then read the flag, hence i opened the shell and used the `chown` command and changed the owner of the `/flag` to `hacker` and then catted the flag from it.
   ```bash
   hacker@permissions~changing-file-ownership:~$ chown hacker /flag
   hacker@permissions~changing-file-ownership:~$ cat /flag
   pwn.college{QHmrbAsxG299dUZpekUyA_dAu-L.QXxEjN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that every file in Linux is owned by a user on the system.On a shared system (such as in a computer lab), there might be many people with different user accounts, all with their own files in their own home directories. But even on a non-shared system (such as your personal PC), Linux still has many "service" user accounts for different tasks.The two most important user accounts are:-our user account! On `pwn.college`, this is the `hacker` user, regardless of what your username is. and `root`. This is the administrative account and, in most security situations, the ultimate prize.
  I also came to know that we can prevent others from accessing certain files owned by the` root` user, configure its permissions so that no other user can read it, and that we can change the ownership of files! This is done via the `chown` (change owner) command which takes the username to which we want it to be changed and the file that we want to change the user of as it's arguments.

### Refference :-
   None


# **2.<ins>Groups and files</ins>**:-
   In this challenge, I have made the flag readable by whatever group owns it, but this group is currently root. Luckily, I have also made it possible for you to invoke `chgrp` as the `hacker` user! Change the group ownership of the flag file, and read the flag!
## My solve:-
   **My flag** :-`pwn.college{wnDTgmJTbqrgkGnS0i84dvyxIGi.QXxcjM1wCNxAzNzEzW}`

   So, the challenge asked us to change the group ownership of the `/flag` file to the `hacker` user, and then read the flag, hence i opened the shell and used the `chgrp` command and changed the owner of the `/flag` to `hacker` and then catted the flag from it.
   ```bash
    hacker@permissions~groups-and-files:~$ chgrp hacker /flag
   hacker@permissions~groups-and-files:~$ cat /flag
   pwn.college{wnDTgmJTbqrgkGnS0i84dvyxIGi.QXxcjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can check what groups you are part of with the `id` command and that group ownership can be changed with the `chgrp` (change group) command! Unless we have write access to the file and membership in the new group, this typically requires root access.

### Refference :-
   None


# **3.<ins>Fun with group names</ins>**:-
   The point is, you've used `hacker` for the group before, but in this level, that is not going to work. I'll still allow you to use `chgrp`, but I have randomized the name of the group that your user is in. You will need to use the `id` command to figure that name out, then `chgrp` to victory!
## My solve:-
   **My flag** :-`pwn.college{kpGuLsE7U0dVxN18H9FXMbX1tEm.QXycjM1wCNxAzNzEzW}`

   So, the challenge asked us to find the name of the group that we the user are in and then change the group to it and then get the flag, hence i opened the shell and used the `id` command to find the name of the group that i am in and then i changed the group of `/flag` to it using the `chgrp` command and then catted the flag.
   ```bash
   hacker@permissions~fun-with-groups-names:~$ chgrp grp21320 /flag
   hacker@permissions~fun-with-groups-names:~$ cat /flag
   pwn.college{kpGuLsE7U0dVxN18H9FXMbX1tEm.QXycjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that there is a convention in Linux that every user has their own group, but this does not have to be the case. For example, many computer labs will put all of their users into a single, shared users group.

### Refference :-
   None


# **4.<ins>Changing permissions</ins>**:-
   In this challenge, you must change the permissions of the `/flag` file to read it! Typically, you need to have write access to the file in order to change its permissions, but I have made the chmod command all-powerful for this level, and you can chmod anything you want even though you are the hacker user. This is an ultimate power. The /flag file is owned by root, and you can't change that, but you can make it readable. 
## My solve:-
   **My flag** :-`pwn.college{AQj8nNTCmajDjmz97u-f29sY8ps.QXzcjM1wCNxAzNzEzW}`

   So, the challenge asked us to change the permissions of the `/flag` file to read it, hence i opened the shell and gave the others permission to read the `/flag` file by using the `chmod` command and passed it `o+r` option, and path of the file as the argument and then catted `/flag` and got the flag.
   ```bash
   hacker@permissions~changing-permissions:~$ chmod o+r /flag
   hacker@permissions~changing-permissions:~$ cat /flag
   pwn.college{AQj8nNTCmajDjmz97u-f29sY8ps.QXzcjM1wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the first character there is the file type when we use `ls -l` command and the next nine characters are the actual access permissions of the file or directory, split into 3 characters denoting permissions for the owning user (now you understand this!), 3 characters denoting the permissions for the owning group (now you understand this as well!), and 3 characters denoting the permissions that all other access (e.g., by other users and other groups) has to the file.Each character of the three represent permission for a different type:
r - user/group/other can read the file (or list the directory)
w - user/group/other can modify the files (or create/delete files in the directory)
x - user/group/other can execute the file as a program (or can enter the directory, e.g., using `cd`)
- - nothing 
   I also learned that Like ownership, file permissions can also be changed. This is done with the chmod (change mode) command. The basic usage for chmod is: `chmod [OPTIONS] MODE FILE` You can specify the `MODE` in two ways: as a modification of the existing permissions mode, or as a completely new mode to overwrite the old one and in modifying an existing mode `chmod` allows you to tweak permissions with the mode format of `WHO+/-WHAT`, where `WHO` is `user/group/other` and `WHAT` is `read/write/execute`. For example, to add "r"ead access for the owning "u"ser, you would specify a mode of `u+r`. write and execute access for the "g"roup and the "o"ther (or "a"ll the modes) are specified the same way. 

### Refference :-
   None


# **5.<ins>Executable files</ins>**:-
   In this challenge, the `/challenge/run` program will give you the flag, but you must first make it executable! Remember your `chmod`, and get `/challenge/run` to tell you the flag!
## My solve:-
   **My flag** :-`pwn.college{o4AJ4w4sxmQwtKUil2-AzMBhLUg.QXyEjN0wCNxAzNzEzW}`

   So, the challenge asked us to make the `/challenge/run` executable and the run it, hence i opened the shell and used the `chmod` command and passed it `u+x` option, and the path of the file as the argument and made the file executable and the ran it and got the flag.
   ```bash
   hacker@permissions~executable-files:~$ chmod u+x /challenge/run
   hacker@permissions~executable-files:~$ /challenge/run
   Successful execution! Here is your flag:
   pwn.college{o4AJ4w4sxmQwtKUil2-AzMBhLUg.QXyEjN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that when you invoke a program linux will only actually execute it if you have execute-access to the program file. 

### Refference :-
   None


# **6.<ins>Permission tweaking practice</ins>**:-
   This challenge will ask you to change the permissions of the `/challenge/pwn` file in specific ways a few times in a row. If you get the permissions wrong, the game will reset and you can try again. If you get the permissions right eight times in a row, the challenge will let you `chmod` `/flag` to make it readable for yourself :-) Launch `/challenge/run` to get started!
## My solve:-
   **My flag** :-`pwn.college{IH1ziF2cTsYHjVijWONqChgSO6u.QXwEjN0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` to get the instructions, hence i opened the shell and ran `/challenge/run` the it gave me a specific permissions to change multiple times on the file `/challenge/pwn` which i did and then the challenge allowed me to make `/flag` readable hence i used the `chmod` and passed the `u+r` option and `/flag` as the argument to do so, then i catted the `/flag` and got the flag. 
   ```bash
   hacker@permissions~permission-tweaking-practice:~$ /challenge/run
   Round 1 of 8!

   Current permissions of "/challenge/pwn": rw-r--r--
   * the user does have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": rw-r--rw-
   * the user does have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod o+w /challenge/pwn
   You set the correct permissions!
   Round 2 of 8!

   Current permissions of "/challenge/pwn": rw-r--rw-
   * the user does have read permissions
   *the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": rw-rwxrw-
   * the user does have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod g+wx /challenge/pwn
   You set the correct permissions!
   Round 3 of 8!

   Current permissions of "/challenge/pwn": rw-rwxrw-
   * the user does have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": -w-rwxrw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod u-r /challenge/pwn
   You set the correct permissions!
   Round 4 of 8!

   Current permissions of "/challenge/pwn": -w-rwxrw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": -w-rw-rw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod g-x /challenge/pwn
   You set the correct permissions!
   Round 5 of 8!

   Current permissions of "/challenge/pwn": -w-rw-rw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": -w-rwxrw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod g+x /challenge/pwn
   You set the correct permissions!
   Round 6 of 8!

   Current permissions of "/challenge/pwn": -w-rwxrw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   
   Needed permissions of "/challenge/pwn": -w--w--w-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   * the group does have write permissions
      - the group doesn't have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod g-rx,o-r /challenge/pwn
   You set the correct permissions!
   Round 7 of 8!

   Current permissions of "/challenge/pwn": -w--w--w-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   * the group does have write permissions
   - the group doesn't have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": rwxrwxrwx
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   * the world does have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod u+rx,g+rx,o+rx /challenge/pwn
   You set the correct permissions!
   Round 8 of 8!
   
   Current permissions of "/challenge/pwn": rwxrwxrwx
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   * the world does have execute permissions

   Needed permissions of "/challenge/pwn": rwxr--r--
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod g-wx,o-wx /challenge/pwn
   You set the correct permissions!
   You've solved all 8 rounds! I have changed the ownership
   of the /flag file so that you can 'chmod' it. You won't be able to read
   it until you make it readable with chmod!

   Current permissions of "/flag": ---------
   - the user doesn't have read permissions
   - the user doesn't have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   - the world doesn't have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permission-tweaking-practice:~$ chmod u+r /flag
   hacker@permissions~permission-tweaking-practice:~$ cat /flag
   pwn.college{IH1ziF2cTsYHjVijWONqChgSO6u.QXwEjN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that we can change the permission of a file multiple times.

### Refference :-
   None


# **7.<ins>Permisssion setting practice</ins>**:-
   This challenge extends the previous challenge by requesting more radical permission changes, which you will need `=` and `,`-chaining to achieve.
## My solve:-
   **My flag** :-`pwn.college{coeh5g5ZGByt1w6B0TFEFtHCewk.QXzETO0wCNxAzNzEzW}`

   So, the challenge asked us to  run `/challenge/run` to get the instructions like the previous challenge, hence i opened the shell and ran `/challenge/run` the it gave me a specific permissions to change multiple times on the file `/challenge/pwn` which i did and then the challenge allowed me to make `/flag` readable hence i used the `chmod` and passed the `u=r` option and `/flag` as the argument to do so, then i catted the `/flag` and got the flag. 
   ```bash
   hacker@permissions~permissions-setting-practice:~$ /challenge/run
   Round 1 of 8!

   Current permissions of "/challenge/pwn": rw-r--r--
   * the user does have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": r-x-wx-w-
   * the user does have read permissions
   - the user doesn't have write permissions
   * the user does have execute permissions
   - the group doesn't have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=rx,g=wx,o=w /challenge/pwn
   You set the correct permissions!
   Round 2 of 8!

   Current permissions of "/challenge/pwn": r-x-wx-w-
   * the user does have read permissions
   - the user doesn't have write permissions
   * the user does have execute permissions
   - the group doesn't have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": -w---x-wx
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   * the group does have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   * the world does have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=w,g=x,o=wx /challenge/pwn
   You set the correct permissions!
   Round 3 of 8!

   Current permissions of "/challenge/pwn": -w---x-wx
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   * the group does have execute permissions
   - the world doesn't have read permissions
   * the world does have write permissions
   * the world does have execute permissions

   Needed permissions of "/challenge/pwn": --xr--rwx
   - the user doesn't have read permissions
   - the user doesn't have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   *the world does have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=x,g=r,o=rwx /challenge/pwn
   You set the correct permissions!
   Round 4 of 8!
   
   Current permissions of "/challenge/pwn": --xr--rwx
   - the user doesn't have read permissions
   - the user doesn't have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   * the world does have execute permissions

   Needed permissions of "/challenge/pwn": r----xr--
   * the user does have read permissions
   - the user doesn't have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=r,g=x,o=r /challenge/pwn
   You set the correct permissions!
   Round 5 of 8!

   Current permissions of "/challenge/pwn": r----xr--
   * the user does have read permissions
   - the user doesn't have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   
   Needed permissions of "/challenge/pwn": rwxrw-r--
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=rwx,g=rw,o=r /challenge/pwn
   You set the correct permissions!
   Round 6 of 8!

   Current permissions of "/challenge/pwn": rwxrw-r--
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   * the group does have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": rwxr--rwx
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   * the world does have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=rwx,g=r,o=rwx /challenge/pwn
   You set the correct permissions!
   Round 7 of 8!

   Current permissions of "/challenge/pwn": rwxr--rwx
   * the user does have read permissions
   * the user does have write permissions
   * the user does have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   * the world does have execute permissions

   Needed permissions of "/challenge/pwn": -w-r--rw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=w,g=r,o=rw /challenge/pwn
   You set the correct permissions!
   Round 8 of 8!

   Current permissions of "/challenge/pwn": -w-r--rw-
   - the user doesn't have read permissions
   * the user does have write permissions
   - the user doesn't have execute permissions
   * the group does have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   * the world does have read permissions
   * the world does have write permissions
   - the world doesn't have execute permissions

   Needed permissions of "/challenge/pwn": r-x-wxr--
   * the user does have read permissions
   - the user doesn't have write permissions
   * the user does have execute permissions
   - the group doesn't have read permissions
   * the group does have write permissions
   * the group does have execute permissions
   * the world does have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=rx,g=wx,o=r /challenge/pwn
   You set the correct permissions!
   You've solved all 8 rounds! I have changed the ownership
   of the /flag file so that you can 'chmod' it. You won't be able to read
   it until you make it readable with chmod!

   Current permissions of "/flag": ---------
   - the user doesn't have read permissions
   - the user doesn't have write permissions
   - the user doesn't have execute permissions
   - the group doesn't have read permissions
   - the group doesn't have write permissions
   - the group doesn't have execute permissions
   - the world doesn't have read permissions
   - the world doesn't have write permissions
   - the world doesn't have execute permissions
   hacker@permissions~permissions-setting-practice:~$ chmod u=r /flag
   hacker@permissions~permissions-setting-practice:~$ cat /flag
   pwn.college{coeh5g5ZGByt1w6B0TFEFtHCewk.QXzETO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that in addition to adding and removing permissions, `chmod` can also simply set permissions altogether, overwriting the old ones. This is done by using `=` instead of `-` or `+` and if we want to set `rw` for the owning `user`, but only `r` for the owning `group`, we can achieve this by chaining multiple modes to `chmod` with `,` and additionally we can zero out permissions with `-`.

### Refference :-
   None


# **8.<ins>The SUID bit</ins>**:-
   The challenge asks us to add the SUID bit to the `/challenge/getroot` program in order to spawn a root shell for you to `cat` the flag ourself!
## My solve:-
   **My flag** :-`pwn.college{g01Haap3KniNIgdBtUqGDd5Jn0W.QXzEjN0wCNxAzNzEzW}`

   So, the challenge asked us to add the SUID bit to the `/challenge/getroot` and then `cat` the flag, hence i opened the shell and used the `chmod u+s` command and passed `/challenge/getroot` as the argument and made the program exectable with SUID, and then ran `/challenge/getroot` which took me to the root and then i catted `/flag`  and got the flag.
   ```bash
   hacker@permissions~the-suid-bit:~$ chmod u+s /challenge/getroot
   hacker@permissions~the-suid-bit:~$ /challenge/getroot
   SUCCESS! You have set the suid bit on this program, and it is running as root!
   Here is your shell...
   root@permissions~the-suid-bit:~# cat /flag
   pwn.college{g01Haap3KniNIgdBtUqGDd5Jn0W.QXzEjN0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that there are many cases in which non-root users need elevated access to do certain system tasks. The system admin can't be there to give them the password every time a user wanted to do a task that only `root/sudoers` can do. Instead, the "Set User ID" (SUID) permissions bit allows the user to run a program as the owner of that program's file, as the owner of a file, we can set a file's SUID bit by using chmod i.e `chmod u+s [program]` and when we `ls -l` it we can see `s` instead of `x` in the permissions and the `s` part in place of the executable bit means that the program is executable with SUID. It means that, regardless of what user runs the program as long as they have executable permissions, the program will execute as the owner user.

### Refference :-
   None
