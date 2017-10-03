# German to English JSON Dictionary

This is a JSON representation of **Mr. Honey's Beginner's Dictionary (German-English)** by *Winfried Honig*. The dictionary is available in various other formats on [Project Gutenberg](http://www.gutenberg.org/ebooks/3212).

Command line tester:
```
python3 tester.py
```
Available commands:
```
> \s	-- show current statistics
> \w	-- show correct and incorrect words
> \h 	-- show command help
> \q	-- quit
```

`jq` can be used to parse the dictionary e.g.

```
$ jq .also english_german.json
"auch"
```
