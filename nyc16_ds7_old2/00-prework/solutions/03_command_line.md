# Learn command line
---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>>```
cd      change working directory
pwd     print working directory
ls      display list of files
echo    eval args then display results
chown   change the owner of a file
chmod   change the access permissions for a file eg. chmod 777 is rwx for owner, group, and everyone
mkdir   create a new directory
cp      copy a file
rm      delete a file
more    display contents of a file - one page at a time
```

---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>>```
ls	list directory
ls -a   lists all entries, including hidden files
ls -l	long output
ls -lh	display sizes in unit prefixes (B, KB, MB, ...)
```

>>
```
-m  stream output (comma separated)
-p	 distinguish directories by appending '/'
-R	  show full tree beneath pwd
-Glp  prints files and directories in different colors
```


---  

What does `xargs` do? Give an example of how to use it.

>>
The xargs command takes in a standard input and will split up the standard input so that it can be passed to utlities that may otherwise not be able to take such long inputs. Additionally, some utilities do not accept standard inputs and instead the input is required to be spelled out (for example: rm, touch, cp, etc.). xargs, when used with these utilities will take an input and split the input into individual arguments that can then be passed into these utilities.

>> 
Example 1: Search in the current directory (and other subdirectories) for files ending in .txt 
and remove these files.
```
$ find . -name "*.txt" -print0 | xargs -0 rm -rf
```

>> 
Example 2: Recursively find all Python files and count the number of lines  
```
$ find . -name 'c*.py' | xargs wc -l
```
