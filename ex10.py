tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print """
You open your bag and reach inside. You find:
\t- 43 Gold Pieces
\te Short Sword
\t* Jesus
"""


while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" %i,