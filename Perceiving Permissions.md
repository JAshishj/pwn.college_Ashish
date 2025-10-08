# **1.<ins>Changing file ownership</ins>**:-
   In this challenge we will practice changing the owner of the `/flag` file to the `hacker` user, and then read the flag. For this challenge only, I made it so that you can use `chown` to your heart's content as the hacker user (again, typically, this requires you to be root).
## My solve:-
   **My flag** :-``

   So, the challenge asked us to change the owner of the `/flag` file to the `hacker` user, and then read the flag, hence i opened the shell and used the `chown` command and changed the owner of the `/flag` to `hacker` and then catted the flag from it.
   ```bash
  
   ```

### What i learned:-
   I learned that every file in Linux is owned by a user on the system.On a shared system (such as in a computer lab), there might be many people with different user accounts, all with their own files in their own home directories. But even on a non-shared system (such as your personal PC), Linux still has many "service" user accounts for different tasks.The two most important user accounts are:-our user account! On `pwn.college`, this is the `hacker` user, regardless of what your username is. and `root`. This is the administrative account and, in most security situations, the ultimate prize.
  I also came to know that we can prevent others from accessing certain files owned by the` root` user, configure its permissions so that no other user can read it, and that we can change the ownership of files! This is done via the `chown` (change owner) command which takes the username to which we want it to be changed and the file that we want to change the user of as it's arguments.

### Refference :-
   None


# **2.<ins></ins>**:-
   The challenge asks us to 
## My solve:-
   **My flag** :-``

   So, the challenge asked us to
   ```bash
  
   ```

### What i learned:-
   I learned that 

### Refference :-
   None
