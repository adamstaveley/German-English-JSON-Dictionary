# German to English JSON Dictionary

This is a JSON representation of **Mr. Honey's Beginner's Dictionary (German-English)** by *Winfried Honig*. The dictionary is available in various other formats on [Project Gutenberg](http://www.gutenberg.org/ebooks/3212).

You can run `tester.js` to test German word knowledge.

You can also use `jq` to parse the dictionary. Add the following to your .bashrc and use `translate [WORD]` to parse it easily:
```bash
translate() {
	jq .$1 /path/to/German-English-JSON-Dictionary/english_german.json | sed -e 's/\"//g'
}```
