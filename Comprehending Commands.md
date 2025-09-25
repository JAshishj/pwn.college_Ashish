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
   **My flag** :-`pwn.college{Awc0LVaQFgdu0XUTzewWhISPH4I.QX3EDO0wCNxAzNzEzW}`

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
   I learned that to create new files we can use the `touch` command which takes the name or path along with the name of the file that we want to create as the argument, also i learned that the file will always be created in the current directory if only the name is used and if we use the name along with the path the it will be created in the specified place.

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
   The challenge asks us to find the flag which is present in a hidden dot-prepended file in `/` directory by using the `ls` command along with `-a` option.
## My solve:-
   **My flag** :-`pwn.college{MPVuO5Hv11NB1B_HvCZAbkiGkO3.QXwUDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `ls` command with `-a` option to find the file in which the flag is present as a hidden dot-pretended file in `/`, hence i opened the shell and  used the `ls -a` command which gave me a file called `.flag-141632437824762` along with other files as it contained the word flag in it's name i thought that the flag should be present in it hence i used the `cat` command to read it and got the flag.
   ```bash
   hacker@commands~hidden-files:~$ ls -a /
   .   .dockerenv             bin   challenge  etc   lib    lib64   media  nix  proc  run   srv  tmp  var
   ..  .flag-141632437824762  boot  dev        home  lib32  libx32  mnt    opt  root  sbin  sys  usr
   hacker@commands~hidden-files:/$ cat ./.flag-141632437824762
   pwn.college{MPVuO5Hv11NB1B_HvCZAbkiGkO3.QXwUDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `ls` command does not show the files that start with a `.`, and inorder to view them we have to use the `-a` option along with the `ls` command also ilearned that `ls` command can take options along with it's arguments.
   
   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC). 


# **11.<ins>An epic filesystem quest</ins>**:-
   The challenge asks us to find the flag which is hidden by using the `cd`, `ls`, and `cat` commands the challenge also gives us some steps on how to solve them those are :- your first clue is in `/`, head on over there, look around with `ls`, there'll be a file named HINT or CLUE or something along those lines, `cat` that file to read the clue, depending on what the clue says, head on over to the next directory.
## My solve:-
   **My flag** :-`pwn.college{0ag7Q9hr12TortMGXqG0ZoNVOvf.QX5IDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `cd`, `ls`, and `cat` command and find the flag using the clues given by the challenge,hence i opened the shell and changed my directory to `/` and then listed the files and directories  present in it using the `ls` command and used the `cat` command to read the `ALERT` file as it seemed different then the other files and got the next clue and similarly continued doing this till i got the flag.
   ```bash
   hacker@commands~an-epic-filesystem-quest:~$ cd /
   hacker@commands~an-epic-filesystem-quest:/$ ls
   ALERT  boot       dev  flag  lib    lib64   media  nix  proc  run   srv  tmp  var
   bin    challenge  etc  home  lib32  libx32  mnt    opt  root  sbin  sys  usr
   hacker@commands~an-epic-filesystem-quest:/$ cat ALERT
   Lucky listing!
   The next clue is in: /usr/lib/ruby/vendor_ruby/power_assert
   The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
   hacker@commands~an-epic-filesystem-quest:/$ cd /usr/lib/ruby/vendor_ruby/power_assert
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ ls -a
   .   .DISPATCH    configuration.rb  enable_tracepoint_events.rb  parser.rb
   ..  colorize.rb  context.rb        inspector.rb                 version.rb
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ cat .DISPATCH
   Congratulations, you found the clue!
   The next clue is in: /usr/lib/python3/dist-packages/jedi/inference/compiled
   Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ ls /usr/lib/python3/dist-packages/jedi/inference/compiled
   BRIEF-TRAPPED  __init__.py  __pycache__  access.py  getattr_static.py  mixed.py  subprocess  value.py
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ cat /usr/lib/python3/dist-packages/jedi/inference/compiled/BRIEF-TRAPPED
   Great sleuthing!
   The next clue is in: /usr/share/javascript/mathjax/jax/output/HTML-CSS/fonts/Neo-Euler/Size2/Regular
   Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ ls /usr/share/javascript/mathjax/jax/output/HTML-CSS/fonts/Neo-Euler/Size2/Regular
   INFO-TRAPPED  Main.js
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ cat /usr/share/javascript/mathjax/jax/output/HTML-CSS/fonts/Neo-Euler/Size2/Regular/INFO-TRAPPED
   Congratulations, you found the clue!
   The next clue is in: /opt/linux/linux-5.4/tools/perf/util/cs-etm-decoder
   hacker@commands~an-epic-filesystem-quest:/usr/lib/ruby/vendor_ruby/power_assert$ cd /opt/linux/linux-5.4/tools/perf/util/cs-etm-decoder
   hacker@commands~an-epic-filesystem-quest:/opt/linux/linux-5.4/tools/perf/util/cs-etm-decoder$ ls
   Build  README  cs-etm-decoder.c  cs-etm-decoder.h
   hacker@commands~an-epic-filesystem-quest:/opt/linux/linux-5.4/tools/perf/util/cs-etm-decoder$ cat README
   Lucky listing!
   The next clue is in: /usr/share/racket/pkgs/typed-racket-doc/typed-racket
   hacker@commands~an-epic-filesystem-quest:/opt/linux/linux-5.4/tools/perf/util/cs-etm-decoder$ cd /usr/share/racket/pkgs/typed-racket-doc/typed-racket
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/typed-racket-doc/typed-racket$ ls
   INSIGHT  compiled  info.rkt  scribblings
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/typed-racket-doc/typed-racket$ cat INSIGHT
   Great sleuthing!
   The next clue is in: /var/lib/php/modules/7.4/cli
   The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/typed-racket-doc/typed-racket$ ls -a /var/lib/php/modules/7.4/cli
   .  ..  .WHISPER  enabled_by_maint
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/typed-racket-doc/typed-racket$ cat /var/lib/php/modules/7.4/cli/.WHISPER
   Tubular find!
   The next clue is in: /usr/share/racket/pkgs/plot-lib/plot/private
   The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/typed-racket-doc/typed-racket$ cd /usr/share/racket/pkgs/plot-lib/plot/private
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/plot-lib/plot/private$ ls
   MEMO  common  compiled  deprecated  no-gui  plot2d  plot3d  utils-and-no-gui.rkt
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/plot-lib/plot/private$ cat MEMO
   Lucky listing!
   The next clue is in: /usr/share/javascript/three/examples/js/nodes/materials/nodes
   Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/plot-lib/plot/private$ ls /usr/share/javascript/three/examples/js/nodes/materials/nodes
   GIST-TRAPPED  MeshStandardNode.js  PhongNode.js  RawNode.js  SpriteNode.js  StandardNode.js
   hacker@commands~an-epic-filesystem-quest:/usr/share/racket/pkgs/plot-lib/plot/private$ cat /usr/share/javascript/three/examples/js/nodes/materials/nodes/GIST-TRAPPED
   CONGRATULATIONS! Your perserverence has paid off, and you have found the flag!
   It is: pwn.college{0ag7Q9hr12TortMGXqG0ZoNVOvf.QX5IDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned how to use `ls` and `cat` command with and without changing the directories and `cd` commands clearly.
   
   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC). 


# **12.<ins>Making directories</ins>**:-
   The challenge asks us to create `/tmp/pwn` directory using the `mkdir` command and then create the `college` file in it, and then run the `/challenge/run` to get the flag.
## My solve:-
   **My flag** :-`pwn.college{Um-T-qRxqMyjhxUO6m3pzQLzEs8.QXxMDO0wCNxAzNzEzW}`

   So, the challenge asked us to use the `mkdir` command to create `/tmp/pwn` directory and then create the `college` file in it, and then invoke the `/challenge/run` to get the flag, hence i opened the shell and create `/tmp/pwn` directory using the `mkdir` command then i used the `cd` command to go to that directory and then used the `touch` command to create the `college` file in it and then invoked `/challenge.run` and got the flag.
   ```bash
   hacker@commands~making-directories:~$ mkdir /tmp/pwn
   hacker@commands~making-directories:~$ cd /tmp/pwn
   hacker@commands~making-directories:/tmp/pwn$ touch college
   hacker@commands~making-directories:/tmp/pwn$ /challenge/run
   Success! Here is your flag:
   pwn.college{Um-T-qRxqMyjhxUO6m3pzQLzEs8.QXxMDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to create new directories we can use the `mkdir` command which takes the name or path along with the name of the directory that we want to create as the argument, also i learned that the directory will always be created in the current directory if only the name is used and if we use the name along with the path the it will be created in the specified place.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


 # **13.<ins>Finding files</ins>**:-
   The challenge asks us to find the flag hidden in the `flag` file present in a random directory.
## My solve:-
   **My flag** :-`pwn.college{Ihuo55u2omOJvfRknG1ZZsJsJ_E.QXyMDO0wCNxAzNzEzW}`

   So, the challenge asked us to get the flag present in the `flag` file which is hidden in some random directory by using the `find` command, hence i opened the shell and used the `find` command along with the search criteria that the name should be flag and the search location as `/` and found the files having `flag` and then used the `cat` command to read all those file till i got the flag.
   ```bash
   hacker@commands~finding-files:~$ find -name flag
   hacker@commands~finding-files:~$ find / -name flag
   find: ‘/tmp/tmp.TpSOPGOVKK’: Permission denied
   find: ‘/etc/ssl/private’: Permission denied
   /usr/local/lib/python3.8/dist-packages/pwnlib/flag
   /usr/share/doc/ruby-xmlrpc/flag
   find: ‘/var/cache/apt/archives/partial’: Permission denied
   find: ‘/var/cache/ldconfig’: Permission denied
   find: ‘/var/cache/private’: Permission denied
   find: ‘/var/lib/apt/lists/partial’: Permission denied
   find: ‘/var/lib/mysql-files’: Permission denied
   find: ‘/var/lib/private’: Permission denied
   find: ‘/var/lib/mysql’: Permission denied
   find: ‘/var/lib/mysql-keyring’: Permission denied
   find: ‘/var/lib/php/sessions’: Permission denied
   find: ‘/var/log/private’: Permission denied
   find: ‘/var/log/apache2’: Permission denied
   find: ‘/var/log/mysql’: Permission denied
   find: ‘/run/mysqld’: Permission denied
   find: ‘/run/sudo’: Permission denied
   find: ‘/root’: Permission denied
   /opt/pwndbg/.venv/lib/python3.8/site-packages/pwnlib/flag
   find: ‘/proc/tty/driver’: Permission denied
   find: ‘/proc/1/task/1/fd’: Permission denied
   find: ‘/proc/1/task/1/fdinfo’: Permission denied
   find: ‘/proc/1/task/1/ns’: Permission denied
   find: ‘/proc/1/fd’: Permission denied
   find: ‘/proc/1/map_files’: Permission denied
   find: ‘/proc/1/fdinfo’: Permission denied
   find: ‘/proc/1/ns’: Permission denied
   find: ‘/proc/7/task/7/fd’: Permission denied
   find: ‘/proc/7/task/7/fdinfo’: Permission denied
   find: ‘/proc/7/task/7/ns’: Permission denied
   find: ‘/proc/7/fd’: Permission denied
   find: ‘/proc/7/map_files’: Permission denied
   find: ‘/proc/7/fdinfo’: Permission denied
   find: ‘/proc/7/ns’: Permission denied
   /nix/store/ka6xbd6z6wj5d6frl7ym4nzfc6p2wkdx-radare2-5.9.8/share/radare2/5.9.8/flag
   /nix/store/f31j0igg7ms3yrj5gm3cm76bjcmdl8w5-python3.12-pwntools-4.13.1/lib/python3.12/site-packages/pwnlib/flag
   /nix/store/7ns27apnvn4qj4q5c82x0z1lzixrz47p-radare2-5.9.8/share/radare2/5.9.8/flag
   /nix/store/5z3sjp9r463i3siif58hq5wj5jmy5m98-python3.12-pwntools-4.13.1/lib/python3.12/site-packages/pwnlib/flag
   /nix/store/n6vb30rd7kkwjj595pgm0dmsmfaqi6i5-rizin-0.7.3/share/rizin/flag
   /nix/store/5n5lp1m8gilgrsriv1f2z0jdjk50ypcn-rizin-0.7.3/share/rizin/flag
   /nix/store/bnlabj2vsbljhp597ir29l51nrqhm89w-rizin-0.7.4/share/rizin/flag
   /nix/store/s8b49lb0pqwvw0c6kgjbxdwxcv2bp0x4-radare2-5.9.8/share/radare2/5.9.8/flag
   /nix/store/8qvj9mzdq2qxgjigw4ysqgbkcx1zi80y-python3.13-pwntools-4.14.1/lib/python3.13/site-packages/pwnlib/flag
   /nix/store/1hyxipvwpdpcxw90l5pq1nvd6s6jdi5m-python3.12-pwntools-4.14.1/lib/python3.12/site-packages/pwnlib/flag
   /nix/store/dz2qxywk6d8hc1gkarpwbhyxb50sh2ak-pwntools-4.14.0/lib/python3.13/site-packages/pwnlib/flag
   hacker@commands~finding-files:~$ cat /usr/local/lib/python3.8/dist-packages/pwnlib/flag
   cat: /usr/local/lib/python3.8/dist-packages/pwnlib/flag: Is a directory
   hacker@commands~finding-files:~$ cat /usr/share/doc/ruby-xmlrpc/flag
   pwn.college{Ihuo55u2omOJvfRknG1ZZsJsJ_E.QXyMDO0wCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to search for a directory we can use the `find` command which takes optional arguments describing the search criteria and the search location, if we don't specify a search criteria, then `find` matches every file and if we don't specify a search location, `find` uses the current working directory.

   ### Refference :-
   [pwn.college Linux Luminarium-2.The file system](https://youtu.be/b67Jq6IZ3U8?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).


 # **14.<ins>Linking files</ins>**:-
   The challenge asks us to find the flag which is in `/flag` file, but `/challenge/catflag` will instead read out `/home/hacker/not-the-flag` by using symbolic links.
## My solve:-
   **My flag** :-``

   So, the challenge asked us to get the flag present in the `/flag` file 
   ```bash
   
   ```

### What i learned:-
   I learned that to search for a directory we can use the `find` command which takes optional arguments describing the search criteria and the search location, if we don't specify a search criteria, then `find` matches every file and if we don't specify a search location, `find` uses the current working directory.

   ### Refference :-
   [pwn.college Linux Luminarium-3.Symbolic links](https://youtu.be/m55AtwjBXpE?list=PL-ymxv0nOtqqRAz1x90vxNbhmSkeYxHVC).
