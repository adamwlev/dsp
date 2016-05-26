# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`rm -rf ____` is remove for a directory that is not empty

`env` lets you take a look at your environment and **env $PATH** lets you take a look at the your PATH (helpful for looking at which python install you will default to)

`_____ | ______` lets you pipe the results of an operation on the left into a subsequent operation on the right.

`_____ > ______` lets you save the results of an operation on the left to a file on the right and **>>** means appending the results to the (already existant) file on the right.

`_____ < ______` lets you take the contents of the file on the right and feed it to a program on the left

`find -name (directory) (pattern) -print` lets you search through the names of the files on your computer and prints the results to the terminal

`cat` prints a whole file to the terminal window

`less` lets you page through the contents of a file with less

<kbd>Ctrl+A</kbd> moves your cursor to start of the line. <kbd>Ctrl+E</kbd> moves your cursor to end of the line

<kbd>Apple+K</kbd> clear the terminal







---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls` lists all files and directories in a location (working directory if no other directory is specified) excluded normally hidden files and directories

`ls -a` does the same except it includes files and directories that start with a period which would normall be hidden

`ls -l` the l for long flag does the same except it will give you more info. it will give you such things as the date and time of last modification, ownership info, and file size.

`ls -lh` does the same as `-l` except it converts the file size to a reasonable choice for units. The smallest of the following options that allows for output of three digits or less - Byte, Kilobyte, Megabyte, Gigabyte, Terabyte, Petabyte.

`ls -lah` is a combination of the `-l`, `-a`, and `-h` flags.

`ls -t` the `-t` flag sorts the resulting output based on time last modified, with the most recent first

`ls -Glp` this is a combination of the `-G` flag which enables colorized output (I think this mostly colors directories according to what kind of directory they are) and the `-l` flag from earlier and the `-p` flag which will put a slash after all directories to communicate that they're directories.

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

I like `la -A` which shows you all files dircetories except `.` and `..`.

`ls -o` is like `ls -l` except it does not print the group id, which I do not understand the use for at this moment.

`ls -S` will order the files/directories by size.

`ls -AlgoS` will print the long output for everything in the wd except `.` and `..`, except it will omit the group id and owner, and it will order the output by size.

`ls -Galapagos` is fun. (Repeating tags doesn't do anything :smile:)



---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` reads the output of something (either a file or the result of a command) and calls a utility function (like `cat` or `mv`) with the read output as arguments to the function. Here's an example that looks for files in your home folder with the substring 'cat' in the name and concatonates the contents of all the files and writes it to a file called 'cat.txt':

`find ~ -name '*cat*' -print0 | xargs -0 -P 24 cat > cat.txt`

 

