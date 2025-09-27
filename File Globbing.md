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

   So, the challenge asked us to change our directory to `/challenge/files`which contains a bunch of files and then run `/challenge/run` with a single argument that `[]` globs into `file_b`, `file_a`, `file_s`, and `file_h`, hence i opened the shell and changed my directory to `/challenge/files` , then i ran the `/challenge/run` with `file_[bash]` as it's argument and got the flag.
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


# **4.<ins>Matching paths with []</ins>**:-
   The challenge asks us to run `/challenge/run` from our home directory with a single argument that `[]`globs into the absolute paths to the `file_b`, `file_a`, `file_s`, and `file_h` files which are present in the`/challenge/files` along with a bunch of files.
## My solve:-
   **My flag** :-`pwn.college{IEVj5V6YRaRgg9Jjjs1fd5PrvdI.QX0IDO0wCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` from our home directory with a single argument that `[]` globs into the absolute paths to the `file_b`, `file_a`, `file_s`, and `file_h` files which are present in the`/challenge/files`, hence i opened the shell and ran the `/challenge/run` with `/challenge/files/file_[bash]` which is it's absolute path as it's argument and got the flag.
   ```bash
   hacker@globbing~matching-paths-with-:~$ /challenge/run /challenge/files/file_[bash]
   You got it! Here is your flag!
   pwn.college{IEVj5V6YRaRgg9Jjjs1fd5PrvdI.QX0IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that glob is a pattern that the shell uses to match filenames or paths and that `[]` is one of the glob which when it is encountered in any argument, the shell will treat it as a for some subset of potential characters, specified within the brackets "wildcard" which works like`?` but matches only specified character and replaces it with the files that match that pattern, i also learned that globs also works with the paths of files.

### Refference :-
   None


 # **5.<ins>Multiple globs</ins>**:-
   The challenge asks us to change our directory to `/challenge/file` which contains diversely named files there and run `/challenge/run` providing a single argument short 3 characters or less globbed word with two `*` globs in it that covers every word that contains the letter p to get the flag.
## My solve:-
   **My flag** :-`pwn.college{0oVQdTjR4at0FrvGhbZKISO5DO2.0lM3kjNxwCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge/file` and then run `/challenge/run` with a single short 3 or less character globbed word with two `*` globs in it that covers every word that contains the letter p as the argument to get the flag, hence i opened the shell and changed my directory to `/challenge/file` and then ran the `/challenge/run` with `*p*` which covers all the words that contain the letter p in it and got the flag.
   ```bash
   hacker@globbing~multiple-globs:~$ cd /challenge/files
   hacker@globbing~multiple-globs:/challenge/files$ /challenge/run *p*
   You got it! Here is your flag!
   pwn.college{0oVQdTjR4at0FrvGhbZKISO5DO2.0lM3kjNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that shell supports the expansion of multiple globs in a single word. 

### Refference :-
   None


# **6.<ins>Mixing globs</ins>**:-
   The challenge asks us to change our directory to `/challenge/file` which contains diversely named files there and run `/challenge/run` providing a single argument short 6 characters or less glob that when passed as an argument to `/challenge/run` will match the files `challenging`, `educational`, and `pwning` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{YNbwpF6aec65dlzCFedR3PKWYpG.QX1IDO0wCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge/file` and then run `/challenge/run` with a single short 6 characters or less glob that when passed as an argument to `/challenge/run` will match the files `challenging`, `educational`, and `pwning` as the argument to get the flag, hence i opened the shell and changed my directory to `/challenge/file` and then ran the `/challenge/run` with `[cep]*` which only lists the mentioned files and got the flag.
   ```bash
   hacker@globbing~mixing-globs:~$ cd /challenge/files
   hacker@globbing~mixing-globs:/challenge/files$ /challenge/run [cep]*
   You got it! Here is your flag!
   pwn.college{YNbwpF6aec65dlzCFedR3PKWYpG.QX1IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that shell supports the expansion of multiple globs in a single word. 

### Refference :-
   None


# **7.<ins>Exclutionary globing</ins>**:-
   The challenge asks us to change our directory to `/challenge/file` which contains diversely named files there and run `/challenge/run` providing a single argument which gives all the files that don't start with `p` in them to get the flag.
## My solve:-
   **My flag** :-`pwn.college{EueNZXEyMwBrVSYL5OmbWxj2OH1.QX2IDO0wCNxAzNzEzW}`

   So, the challenge asked us to change our directory to `/challenge/file` and then run `/challenge/run` with a single argument which would give us all the files wich doesn't start with `p` to get the flag, hence i opened the shell and changed my directory to `/challenge/file` and then ran the `/challenge/run` with `[^p]` and got the flag.
   ```bash
   hacker@globbing~exclusionary-globbing:~$ cd /challenge/files
   hacker@globbing~exclusionary-globbing:/challenge/files$ /challenge/run [^pwn]*
   You got it! Here is your flag!
   pwn.college{EueNZXEyMwBrVSYL5OmbWxj2OH1.QX2IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that if the frst character in the `[]` is a `!` or a `^` (in newer versions of bash), the glob inverts, and that bracket instance matches characters that aren't listed. 

### Refference :-
   None


# **8.<ins>Tab completion</ins>**:-
   The challenge  has copied the flag into `/challenge/pwncollege`, and we can freely `cat` that file. But we can't type the filename and must use  tab-to complete it to get the flag.
## My solve:-
   **My flag** :-`pwn.college{M3J8e9c7ZWwHmzVVZjBdMELSxF3.0FN0EzNxwCNxAzNzEzW}`

   So, the challenge asked us to read `/challenge/pwncollege` without typing the filename instead by using tab to complete it, hence i opened the file and used the `cat` command and started to write the name of the file and then used tab to auto complete it and got the flag.
   ```bash
   hacker@globbing~tab-completion:~$ cat /challenge/pwncollege​
   pwn.college{M3J8e9c7ZWwHmzVVZjBdMELSxF3.0FN0EzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that if we hit tab in the shell, it'll try to figure out what you're going to type and automatically complete it.

### Refference :-
   None

   # **9.<ins>Multiple options for tab completion</ins>**:-
   The challenge has a `/challenge/files` directory with a bunch of files starting with `pwncollege`. Tab-complete from `/challenge/files/p` or so, and get the flag.
## My solve:-
   **My flag** :-`pwn.college{IevrKAwO9xGwNyIvpX7UMfqGVbL.0lN0EzNxwCNxAzNzEzW}`

   So, the challenge asked us to read `/challenge/files` contains bunch of files starting with `pwncollege`. Tab-complete from `/challenge/files/p` to get the flag, hence i opened the file and used the `cat` command and started to write the name of the file and then used tab to auto complete it and tried various name till i got the flag and got the flag.
   ```bash
   hacker@globbing~multiple-options-for-tab-completion:~$ cat /challenge/files/pwncollege-flag
   pwn.college{IevrKAwO9xGwNyIvpX7UMfqGVbL.0lN0EzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that if there are multiple options by default bash will auto-expand until the first point when there are multiple options when you hit tab a second time, it'll print out those options and some other shells and configurations, instead, will cycle through the options.

### Refference :-
   None

   # **10.<ins>Tab completion on commands</ins>**:-
   The challenge  has  has a command that starts with `pwncollege`, and it'll give you the flag, type `pwncollege` and hit the tab key to auto-complete it.
## My solve:-
   **My flag** :-``

   So, the challenge asked us to type `pwncollege` and hit the tab key to auto-complete it, hence i opened the file and used the `cat` command and started to wrote `pwncollege`  and then used tab to auto complete it and got the flag.
   ```bash
   hacker@globbing~tab-completion-on-commands:~$ pwncollege-9302
   Correct! Here is your flag:
   pwn.college{wrq0LO-t3tF8uawdegVTnHNlFLE.0VN0EzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that tab completion can also be used on commands.

### Refference :-
   None
