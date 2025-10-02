# **1.<ins>Translating characters</ins>**:-
   The challenge asks us to run `/challenge/run` which will print the flag but will swap the casing of all characters (e.g., A will become a and vice-versa) and asks us to get the flag by swapping them using the `tr` command.
## My solve:-
   **My flag** :-`pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` which will print the flag but will swap the casing of all characters and asks us to reverse it using `tr`, hence i opened the shell and an ran `/challenge/run` and piped it's output to the `tr` command as it's input and changed all the lower letters to upper and upper to lower and got the flag. 
   ```bash
   hacker@data~translating-characters:~$ /challenge/run | tr '[:upper:][:lower:]' '[:lower:][:upper:]'
   yOUR CASE-SWAPPED FLAG:
   pwn.college{Ic7a5KqdvwDqugSed3eXdBW8sUK.01MxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `tr` command translates characters it receives over standard input and prints them to standard output, i alo came to know that in basic usage, `tr` translates the character provided in its first argument to the character provided in its second argument.

### Refference :-
   None


# **2.<ins>Deleting characters</ins>**:-
   The challenge will intersperse some decoy characters (specifically: `^` and `%`) among the flag characters and asks us to use `tr -d` to remove them.
## My solve:-
   **My flag** :-`pwn.college{I-2dLPo4NQsjE6n-tQKkzhJwKd1.0FNxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to use `tr -d` to remove the interspersed decoy characters (specifically: `^` and `%`) among the flag characters, hence i opened the shell and ran `/challenge/run` and piped it's output to `tr` command and used the `-d` option on `^` to delete it and then piped it's output as the input of another `tr` command because `tr` can only take one arrgument for deleting and used `-d` option on `%` to delete it and got the flag. 
   ```bash
   hacker@data~deleting-characters:~$ /challenge/run | tr -d ^ | tr -d %
   Your character-stuffed flag:
   pwn.college{I-2dLPo4NQsjE6n-tQKkzhJwKd1.0FNxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `-d` option in the `tr` command is used to delete the characters provided to it as the argument.

### Refference :-
   None


# **3.<ins>Deleting newlines</ins>**:-
   The challenge will inject a bunch of newlines into the flag and asks us to delete them with `tr`'s `-d` flag and the escaped newline specification to get the flag.
## My solve:-
   **My flag** :-`pwn.college{Ir5RLBO5jVAPbX37suJiLfozwk0.0VNxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to use the `tr` commands `-d` option to delete the newline characters i.e `"\n"`, hence i opened the shell and ran `/challenge/run` and piped it's output to `tr` and used the `-d` option on `"\n"` to delete them and got the flag.
   ```bash
   hacker@data~deleting-newlines:~$ /challenge/run | tr -d "\n"
   Your line-split flag: pwn.college{Ir5RLBO5jVAPbX37suJiLfozwk0.0VNxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that to add new line we have to use `"\n"` character.

### Refference :-
   None


# **4.<ins>Extracting the first lines with head</ins>**:-
   The challenge asks us to run `/challenge/pwn` which outputs a bunch of data, and we'll need to pipe it through `head` to grab just the first `7` lines and then pipe them onwards `/challenge/college`, to get the flag.
## My solve:-
   **My flag** :-`pwn.college{oLZZ8pPk7XO8UhqmxvyTjMyYpoR.0lNxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/pwn` which outputs a bunch of data and  pipe it through `head` to grab just the first `7` lines and then pipe them to `/challenge/college`, hence i opened the shell and ran `/challenge/pwn` and piped it's output to the `head` command and took the first `7` lines using the `-n` option and then piped it's output to `/challenge/college` and got the flag.
   ```bash
   hacker@data~extracting-the-first-lines-with-head:~$ /challenge/pwn | head -n 7 | /challenge/college
   Congratulations, you piped the right codes!
   pwn.college{oLZZ8pPk7XO8UhqmxvyTjMyYpoR.0lNxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `head` command is used to display the first few lines of its input and by default it shows the first 10 lines, but we can control this with the `-n` option followed by how many lines we want as it's argument.

### Refference :-
   None


# **5.<ins>Extracting specific sections of text</ins>**:-
   The challenge asks us to run `/challenge/run` which will give you a bunch of lines with random numbers and single characters (characters of the flag) as columns and we have to use `cut` to extract the flag characters, and then pipe them to `tr -d "\n"` (like the previous level!) to join them together into a single line to get the flag.It also gave us a hint that our solution will look something like `/challenge/run | cut ??? | tr ???`, with the `???` filled out.
## My solve:-
   **My flag** :-`pwn.college{gTAEVh_w4on_DsYJmdOaHuG9IZJ.01NxEzNxwCNxAzNzEzW}`

   So, the challenge asked us to run `/challenge/run` and  use `cut` to extract the flag characters and then pipe them to `tr -d "\n"`, hence i opened the shell and ran the `/challenge/run` and piped it's output to `cut` and extracted the flag characters and then piped it to `tr` command and removed the newlines to get the flag in one sentence and got the flag. 
   ```bash
   hacker@data~extracting-specific-sections-of-text:~$ /challenge/run | cut -d " " -f 2 | tr -d "\n"
   pwn.college{gTAEVh_w4on_DsYJmdOaHuG9IZJ.01NxEzNxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that `cut` command is used to grab specific columns in a file, the `cut` command has the `-d` argument specifies the column delimiter i.e how columns are separated, and the `-f` argument specifies the field number which column to extract.

### Refference :-
   None


# **6.<ins>Sorting data</ins>**:-
   The challenge has a file at `/challenge/flags.txt` containing 100 fake flags, with the real flag mixed among them and when sorted alphabetically, the real flag will be at the end.
## My solve:-
   **My flag** :-`pwn.college{kwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}`

   So, the challenge asked us to sort the `/challenge/flags.txt` file in alphabetical order, hence i opened the shell and used the sort command and `/challenge/flags.txt` as it's arguments to sort the in alphabetical and got the flag at the end of the list like said in the challenge.
   ```bash
   hacker@data~sorting-data:~$ sort /challenge/flags.txt
   ovm.cnlkefe{kwb2S3IclBQa9sZy3hWsRsSHJaG.0EM0MDOxwBNwAzNzEyW}
   ovm.cokldge{jwc2S4IblBQa9sYy2hXtSsSIIaH.0FM0MDOwwCNxAyMyEzW}
   ovn.boklege{kvc2S4HbkAQa8sZy3gXsSsSIJaH.0FM0MCNxwBNwAzMyEyW}
   ovn.bollege{kwc1S4HclBQa9sYz3gXsSsSIIaH.0FM0LDOxvCNwAyNyDzW}
   ovn.cnkkdfe{kvb2R4IclAQa9rYz2hXtRsSHJaH.0EL0LDNxvCNxAzMyEzV}
   ovn.cnlkege{kvc2S4IclBPa8sZy3hXtSsSHJaH.0EM0MCOxwCNwAzNzEzV}
   ovn.colldfe{jvc1R4HclBPa8sYz2gXtRsSIJaH.0FM0MDNwvCNxAzNyDyW}
   ovn.collefd{kwc2S4IclBPa9sZz3hXtSsSHJaG.0FM0MDOxwBNxAzMzEzW}
   ovn.college{kwc1S4HclBQa9sZy3hXtSrRIJaH.0FM0MCOxvCNxAzMzEzW}
   owm.bolkege{kvc1S4IclBQa9rZy2hWtSsSIJaH.0EM0MDOxwCNxAzNzEzW}
   owm.bollefe{jvb2S4IblAPa9sZz2hXtRsRIJaH.0EM0MCNxwCNwAzNzDzV}
   owm.cnklege{kwc2S3IclBPa9sZz3gXtRrSHJaG.0EM0LCOxwCMxAzNzDzW}
   owm.cnllegd{kwc1S4IclBQa8rZz3hXtSsSIJaH.0FM0LDOxwCNxAzNzEzW}
   owm.cnllege{kvb2S3IclBQa8sZz3hXtSsSIIaH.0FM0LDOwwCNxAzNzEzW}
   owm.coklegd{kwc1S4IclBQa9rZy3hWtSsSIJaH.0FL0MDOxwCNwAzNyEzW}
   owm.colkefe{kvc2R3HclBQa8sYz3hWsSsSIIaH.0EM0LDOxwCNxAyNyEzW}
   owm.colldge{jvb1S4IblBQa9sYy3hXtRsSHJaH.0FM0MCNxwCNwAzNzDzV}
   owm.collefe{jwc1S4HblBQa9rZz2hXtSrSIJaH.0EM0MDOwwBNwAyNzDzV}
   owm.college{kwc2S4IclBQa9sZz3hWsSsSIJaH.0FM0MDOxwBNwAyNyEzW}
   own.bokkege{kvc2S3IclBPa8sZy3hXtRsSHJaH.0EM0MDOxwCNxAzNyEzV}
   own.bolkegd{kwc2R4IclBQa9rZy3hXtSrSIJaH.0FL0LDOxwBNwAzNzEzV}
   own.bollege{kvc2S4IclAQa9sZz3hXtSsSIIaH.0EM0MDOxwCNxAzNzEzV}
   own.cnklege{kwc2S4IclBPa9rZz3hWtSrSHJaH.0FL0MCOwvCNxAzMyEzW}
   own.cnllefe{kwc1S4HclBQa9sYz2gXsSsSHJaH.0EM0MDOxwCNxAyMyDzW}
   own.cokkege{kwb1S4HckBQa9rYz2gXtSsRIJaG.0FM0MDOxwCNxAzMzDzV}
   own.coklege{kwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   own.colkdgd{jwc1S4IckBQa9rZz3gWsSsRIJaG.0EM0MDOwwCMxAzMyEyV}
   own.colkege{kwc2R4IblBQa9sZz3gXsSrSIIaG.0FM0LDOwwCNwAzNzEzV}
   own.colldfe{kvc2R3IbkBQa9sZz3hXtRsRIJaH.0FM0MDOwwCMxAzMyDzW}
   own.collefe{kwc1R3IckAQa9rZy3gXtSrRIJaH.0FM0MDOwvCNxAyNyEzV}
   own.collegd{kvc2S4IclAQa9sZz3hWtSsSIIaG.0FM0MDOwvBMxAzNzEyW}
   own.college{kwc1R4HclBQa8rZz3gWsSsSIJaH.0FM0MDOxwBNxAzNzEzV}
   own.college{kwc1R4IclBQa9rYz3hXsSsSIJaG.0FM0MDOxwCNwAzNzEzW}
   own.college{kwc1S4HclBQa9sZz2hXtSsSIJaH.0FM0MDOwvCNxAzNzEzW}
   own.college{kwc2S3HclBQa9sYz3hXtSsSIJaH.0FM0MDOwvCNxAzNzEzW}
   own.college{kwc2S4IclBQa9rZz3hXtSsRHJaG.0FM0MDOxwCMxAzNzEzW}
   pvm.bnllefd{kvb2S3IckBPa9rZy2gXtSsRIJaG.0EM0LDOxwBNxAzNyDzW}
   pvm.cnkkdge{kwb2S3HclAQa9sZz3hXsSsSHJaH.0FM0MCOxwCMxAzNzDzW}
   pvm.cokkege{kwc2S4IckBQa8sZz3gXtSrRIIaH.0FM0LDOxwCNwAzNzEzW}
   pvm.cokldge{kvc2S4IclAQa8sYz3hWtSrRIIaH.0EL0MDNxwCMxAzNzEyW}
   pvm.collegd{kvc2R4IclAPa9sYz2hXtSrRIJaH.0EM0MDOxwBNwAzMyEyV}
   pvn.bolkefe{jvc1S4HblBPa8sZz2hXtSsSIJaH.0FM0MDOxvCMwAzMzDzV}
   pvn.bollefd{kwc2S3HclBQa9rZz2hXtRsSIJaH.0FM0MDOxwCMwAyNzEyW}
   pvn.bollege{kwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOwwCNwAzNzEzW}
   pvn.cnlldfe{kwb2S4IblBPa9sZz3hXtSsSIJaH.0FL0MDOxvCMwAzMzEzW}
   pvn.cnlldge{kvc1S3HclBQa8sZz3hWtSsRIIaH.0EL0MDOxwBNxAzNzDyW}
   pvn.cnllege{jvc2R4IckBPa9sZz3hXsSrSIJaH.0FM0MDOxwCNxAzNzEyW}
   pvn.cokkefe{kwb2S3HclBPa9sYz3gXtSrSIJaH.0FL0MDOxwCMxAyNzEyW}
   pvn.cokldfe{kwb2S4IclBQa9sZz2gXtSsSIIaH.0FM0MDNxwCNxAzNzDyV}
   pvn.colkefd{kwb2S4IblAPa9sZz3hWtRsSIJaH.0FM0MDOxvCMxAyNzEzW}
   pvn.colkegd{kvc2S4HclBPa9sZz2gXtSsSHJaH.0EM0MCNwvBMxAyNzEzV}
   pvn.colldge{jwc2S3IclBQa9sZy3gXtSsSIJaH.0FM0MDOwwBNwAyMzDzW}
   pvn.collegd{jwc2S4HclBQa9sZz3hXtSsSHJaH.0FL0MDOxwCNxAzNzDzV}
   pvn.college{kwc2S3IckBQa9sZz3gXtSrRIJaG.0FM0MDOxwCNxAzNzEzW}
   pwm.bolkege{kwc2R4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   pwm.cnlldge{kvc1S4IckBQa8rZz2gXtSsSIJaG.0FM0MDOwwCMxAyNzEzV}
   pwm.cokldfe{kwc2R4IclAPa8rZz3gWtSsSIJaH.0EM0MCOxwCMxAzMzDyV}
   pwm.collefd{kwc2R4IclBQa9sZy2hWsSsSIJaH.0FM0LDOxwCNxAzNyEzW}
   pwm.collefe{kwc2S3IclAQa9sZz3hXtSsSIJaH.0FM0MDNxwCNxAzNzEzW}
   pwm.collefe{kwc2S4HckBPa9sZz2gXtRsSIIaH.0FM0LDOwwBMwAyMzEzV}
   pwm.collegd{kwc2S4IckBQa9sZz3hXtSsSIJaH.0FM0MDOxwCMxAzNyEzW}
   pwn.bolkefe{jvc2S4IblBQa8sZz3gWtRsRHJaH.0FL0MDOwvCNxAyMzDyW}
   pwn.bollefe{kwb1S4IckBQa9rZz3hXsRsRIJaH.0FM0MDOxvCNxAyNzEzW}
   pwn.bollege{kwc2R4IclBQa9sZz3hXtSsSHJaH.0FM0LDOxwCNxAzNyEzW}
   pwn.cnkldge{kvc2S3IclBQa9sZz3hXtSsRIJaH.0FL0MDOwwCNwAzNzEzW}
   pwn.cnlkdge{kwb2S4IclBQa9sZz3hXtSsSIJaH.0FL0MDNwwCNxAzNzEzW}
   pwn.cnlldge{kwc2S4IclBQa9rZz3hXtSsSIJaH.0FL0MDOxwCMxAzNzDyW}
   pwn.cnllegd{kvc1S3IblBPa9sZy3hWsSsSIJaH.0EM0MDOxwCNxAzNyDzW}
   pwn.cnllege{kwc2R4IblBQa9sZz2hWsSrSIJaH.0FM0MDNxwCNxAyNzEyW}
   pwn.cnllege{kwc2S4IblBQa9sZy3gXtSsSIJaH.0FM0MDOxwCNxAyNzEzW}
   pwn.cokkdgd{kvc2S4IblBQa9sYy3hXtSsSIJaG.0FM0MDOwwCMxAzNyEzV}
   pwn.cokkdgd{kwb2S4HclAQa9sZz3hXtRsSIJaH.0EL0MCOxwCNxAzNzEzW}
   pwn.coklege{jvc2R4IbkBQa9sZy3hXsSsSIJaH.0EM0LCNxwCNwAyMzEzV}
   pwn.coklege{kwb2S4IclBQa9sZz3hXtSsSIIaH.0FM0MDOxwCNxAzNzDzW}
   pwn.coklege{kwc2S4IblBQa8rZz3hWsSsRIIaH.0FM0MDOxwCNxAzNyEzW}
   pwn.colkdfe{kvc1R4IclBPa9rZz3hXtRsSIIaG.0FL0MCOwwBMwAyMzEzV}
   pwn.colkdfe{kvc2S3IclBQa9rZz3gWtSsSHJaG.0FM0LDOxwBMxAzNzEyV}
   pwn.colkefd{kwc2S4HclAQa9sZy3hXtSsSIJaG.0EM0MDOwwBNxAzMzEyW}
   pwn.colkefe{kvc2S4IblBQa9rZy2hXtSsSIJaH.0FL0MDOxwBMxAzNyEzW}
   pwn.colkege{kwc2S4IclBQa9sZz3hXtSsSHJaH.0FM0MDOxwCNwAzNzEzW}
   pwn.colldgd{jwc2R4IclBQa8rYy3hXtRsSIJaH.0FM0MDOxwBNxAzMzEyV}
   pwn.colldge{kwc2S3IclBQa9sZz3hXtSsSIJaH.0FM0LDNxwCNxAyNzEzW}
   pwn.collefe{kwc2S3IckBQa9sYz3hXtSsSIJaH.0EM0MDOxwCNxAzNzDzW}
   pwn.collegd{jwc2S4IblBPa9rZz3hXtSsRIIaH.0FM0MCNxwCNwAzNyEyV}
   pwn.collegd{kwc1S4IclBQa9sZz3hXsSsSIJaH.0FM0MDOxwCMxAzNzEzV}
   pwn.college{jwc1R4IblBPa9rZz3hXsSrSIJaG.0FM0MCNwwCNxAzNyEzW}
   pwn.college{jwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   pwn.college{kvc2S4IclBPa9sZz3hWtSsRIIaH.0FM0LDOxwCNxAzNyDzW}
   pwn.college{kwb2S4IclBQa8sZz3gXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   pwn.college{kwb2S4IclBQa9sZy3hXtSrSIJaH.0FM0MDOxwBNxAzNzEzW}
   pwn.college{kwb2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   pwn.college{kwc2R4IclBQa9sZz3gXsSsSIJaG.0FM0MDNxwCNxAzNzEzW}
   pwn.college{kwc2S3HblBQa9sZy3gXtSsSIJaH.0EM0MCOxwBNwAyNzEzW}
   pwn.college{kwc2S3IckBQa9sYz3hXsSsSIIaH.0FM0MDNxwCNxAzNzEzW}
   pwn.college{kwc2S3IclBQa9sZz3hXtSsSHJaH.0EL0MDOxwCNxAyMzEzW}
   pwn.college{kwc2S3IclBQa9sZz3hXtSsSIJaH.0FL0MDOxwCNwAzNzEzW}
   pwn.college{kwc2S4IblBPa9sYz3hXtSrRIJaH.0EM0MDNxwCNxAzNzEzW}
   pwn.college{kwc2S4IblBQa9sZy3hXtSrRIJaH.0EM0MDNxwCNxAzNzEzW}
   pwn.college{kwc2S4IclBQa9sYz3hXtSsSIJaH.0FM0MCNxwCNxAyNyEyW}
   pwn.college{kwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNwAyNzEzW}
   pwn.college{kwc2S4IclBQa9sZz3hXtSsSIJaH.0FM0MDOxwCNxAzNzEzW}
   ```

### What i learned:-
   I learned that the `sort` command orders lines alphabetically and we can this using various options like can change this:
    -r: reverse order (Z to A)
    -n: numeric sort (for numbers)
    -u: unique lines only (remove duplicates)
    -R: random order!.

### Refference :-
   None
