# **1.<ins>Matching with *</ins>**:-
   The challenge asks us to change our directory to `/challenge` by using glob and that the argument which we pass to the `cd` should be atmost characters abd then run `/challenge/run` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{0RwFca6F9q35nKdra1_rpXnC02-.QXxIDO0wCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge` by using the `*` glob with the argument being atmost 4 characters and then run `/challenge/run`, hence i opened the shell and used the `cd` command and passed `/ch*` as the argument which fit the 4 character limt, then i ran the `/challenge/run` and got the flag.
   ```bash
   hacker@globbing~matching-with-:~$ cd /ch*
   hacker@globbing~matching-with-:/challenge$ /challenge/run
   You ran me with the working directory of /challenge! Here is your flag:
   pwn.college{0RwFca6F9q35nKdra1_rpXnC02-.QXxIDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that glob is a pattern that the shell uses to match filenames or paths and that `*` is one of the glob which when it encountered in any argument, the shell will treat it as a "wildcard" and try to replace that argument with any files that match the pattern.

### Refference :-
   None

