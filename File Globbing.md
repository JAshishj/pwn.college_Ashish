# **1.<ins>Matching with *</ins>**:-
   The challenge asks us to change our directory to `/challenge` by using `*` glob and that the argument which we pass to the `cd` should be atmost characters and then run `/challenge/run` to get the flag.
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
   I learned that glob is a pattern that the shell uses to match filenames or paths and that `*` is one of the glob which when it is encountered in any argument, the shell will treat it as a "wildcard" and try to replace that argument with any files that match the pattern.

### Refference :-
   None


# **2.<ins>Matching with ?</ins>**:-
   The challenge asks us to change our directory to `/challenge` by using `?` glob instead of the `c` and `l` as the argument of `cd` and then run `/challenge/run` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{44E-pJZpdM9uTXJ9XDp5E2UL1LF.QXyIDO0wCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge` by using the `?` glob instead of `c` and `l` as the argument and then run `/challenge/run`, hence i opened the shell and used the `cd` command and passed `/?ha??enge` as the argument, then i ran the `/challenge/run` and got the flag.
   ```bash
   hacker@globbing~matching-with-:~$ cd /?ha??enge
   hacker@globbing~matching-with-:/challenge$ /challenge/run
   You ran me with the working directory of /challenge! Here is your flag:
   pwn.college{44E-pJZpdM9uTXJ9XDp5E2UL1LF.QXyIDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that glob is a pattern that the shell uses to match filenames or paths and that `?` is one of the glob which when it is encountered in any argument, the shell will treat it as a single "wildcard" which works like`*` but matches only one character and replaces it with the files that match that pattern.

### Refference :-
   None


   
# **3.<ins>Matching with []</ins>**:-
   The challenge asks us to change your working directory to `/challenge/files` which contains a bunch of files and run `/challenge/run` with a single argument that `[]` globs into `file_b`, `file_a`, `file_s`, and `file_h` and get the flag.
## My solve:-
   **My flag** :-`pwn.college{Y-S1QR1KGH-XXras6PoOSue8NJ7.QXzIDO0wCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge/files`which contains a bunch of files and then run `/challenge/run` ith a single argument that `[]` globs into `file_b`, `file_a`, `file_s`, and `file_h`, hence i opened the shell and changed my directory to `/challenge/files` , then i ran the `/challenge/run` with `[bash]` as it's argument and got the flag.
   ```bash
   hacker@globbing~matching-with-:~$ cd /challenge/files
   hacker@globbing~matching-with-:/challenge/files$ /challenge/run file_[bash]
   You got it! Here is your flag!
   pwn.college{Y-S1QR1KGH-XXras6PoOSue8NJ7.QXzIDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that glob is a pattern that the shell uses to match filenames or paths and that `[]` is one of the glob which when it is encountered in any argument, the shell will treat it as a for some subset of potential characters, specified within the brackets "wildcard" which works like`?` but matches only specified character and replaces it with the files that match that pattern.

### Refference :-
   None
