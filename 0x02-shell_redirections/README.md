# Project 0x02 - I/O Redirections and filters

### Scripts Descriptions


0. **0-hello_world** - Prints "Hello, World"

1. **1-confused_smilet** - Prints `"(Ôo)'` by escaping it

2. **2-hellofile** - Displays `/etc/passwd` using `cat`

3. **3-twofiles** - Displays `/etc/passwd` and `/etc/hosts` using `cat`

4. **4-lastlines** - Displays the last 10 lines of `/etc/passwd` using `tail -n 10`

5. **5-firstlines** - Displays the first 10 lines of `/etc/passwd` using `head -n 10`

6. **6-third_line** - Displays the third line of `./iacta` by combining `head -n 3` with `tail -n 1`

7. **7-file** -  creates the file `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)` with contents: ***Holberton School*** by using echo, with stdout redirection and the escape sequence: `'\*\\'\''"Holberton School"\'\''\\*$\?\*\*\*\*\*:)'`

8. **8-cwd_state** - Redirects the output of `ls -la` to `ls_cwd_content` using the `>` operator

9. **9-duplicate_last_line** - Duplicates the last line of `./iacta` using `tail` to the the last line, and `>>` to redirect the output to the end of **iacta**

10. **10-no_more_js** - Deletes all `.js` files using `find` with the `-type t` and `-delete` arguments

11. **11-directories** - Counts the number of directories and sub directories by combining `find` with `wc -l`

12. **12-newest_files** - Displays the 10 newest files using `ls` to sort files by time, `grep` to filter out nested files, and `head` for the first 10 files

13. **13-unique** - Outputs only unique inputs by leveraging `sort` and `uniq -u`

14. **14-findthatword** - Displays lines matching the pattern "root" in `/etc/passwd` using `grep`

15. **15-countthatword** - Displays matched line count of the pattern `bin` in `/etc/passwd` using `grep -c`

16. **16-whatsnext** - Displays the following 3 line of all mathes of `bin` in `/etc/passwd` using `grep -A 3`

17. **17-hidethisword** - Finds lines without the word `bin` using the `-v` argument to `grep` to negate test

18. **18-lettersonly** - Fins lines starting with a letter by using `grep` with the beginning of line anchor and the `[:alpha:]` character class

19. **19-AZ** - Replaces `A` and `c` with `Z` and `e` respectively with `tr`

20. **20-hiago** - Removes all `c` and `C` occurrance using `tr -d`

21. **21-reverse** - Uses `rev` to reverse input

22. **22-users_and_homes** - Displays all users and their home directories by splitting input by `:` with `cut` and selecting index **1** and **6** which corresponds to the username and it's home directory. The result is sorted with `sort`

23. **100-empty_casks** - Finds all empty files and directories by using `find` with the `-empty` argument

24. **101-gifs** - Finds all `.gif` files using `find` then gets the basename by using `cut` with `rev`

25. **102-acrostic** - Displays acrostics from an inputs first letter of it's lines by using `cut` to get the first letter, and `paste` to concatenate them and end with a newline

26. **103-the_biggest_fan** - Finds the 11 most active hosts by first using `tail` to remove the tsv header, then use `cut` to get the first row which is the hostnames. `sort` and `uniq` are combined to display the most active hosts in descending order, before `head` is used to get the top 11, and `rev` and `cut` are used to remove the padding and numbers introduced by `uniq`

















