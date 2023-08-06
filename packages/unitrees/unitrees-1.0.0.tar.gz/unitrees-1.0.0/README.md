## Introduction

Unitrees is a very simple Python module for printing out little text "trees" generated from lists, turning out to look rather like this: \
Note that the font on PyPi may affect the way this is seen. If all goes well, it should be perfect, but online it may not be. However, the following text, when viewed in the terminal/shell, should be devoid of gaps between the lines.
\

\
`┐`\
`├─A`\
`├─B`\
`├─C`\
`├┐`\
`│├─D`\
`│├─E`\
`│├┐`\
`││├─F`\
`││├─G`\
`││├┐`\
`│││├─H`\
`││├┘`\
`│├┘`\
`│├─I`\
`├┘`\
`... [shortened for clarity] ... `\
`├─O`\
`├─P`\
`┘`

## Usage

This module is incredibly easy to use. It has three main functions; `visual_standard(...)`, `visual_space(...)`, and `visual_ascii(...)`. It comes with multiple character sets (in list form), that can be plugged into the `visual_standard(...)` function. Here is a list of the character sets:

- characters_thick
- characters_thin
- characters_unicode
- characters_alt
- characters_dubl
- characters_audiowaves

Each character set has it's own style. The style used for the demonstration tree was `characters_thin`, the default option (it looks the best on a mac - if you are using windows, `characters_thick` may look better). In order to generate a tree using one of the character sets, you simply have to type the following python line into a python shell: \
\
`>>> unitrees.visual_standard(<your list, eg. ['A', ['A, 'B', ['C']], 'D']>, charset=unitrees.characters_thin)` \
\
This command will print out a unicode tree.

### visual_space(...) & visual_ascii(...)

If you would like to have an ascii tree, you can either use the characters_unicode character set or use the specalised function. Furthermore, if you would like a tree puerly based off indention, you may use the `visual_space(...)` function.

## Technical ⚙️

### Creating your own character sets

It is actually quite easy to create your own character sets; all you have to do is define a five character list containing all the symbols that the function might request. The list used for characters_thin is shown below: \
\
`characters_thin = [`\
`	'├', '┐', '┘', '│', '─'`\
`]`\
\ 
The first item in the list is used as a junction between the main line and either a sub-line or a text snippet. An example of this section in the tree is shown below:\
\
`├ ─ A`\
`Note that the characters have a space between them for clarity.`\
\
As also shown above, the *last* character in the list adds as a "cross beam" of sorts, seperating  the letter form the junction. \
\
The second character acts as a sub-tree start symbol, and can also be found at the begining of the tree. The text snippet below shows this: \
\
`├┐`\
`│├─D`\
\
The third also acts as a terminator for a sub-tree, and the overall main tree: \
\
`│├─I`\
`├┘`\
\
The fourth character does not seem very important, but it is actually cruital - it continues through to show depth when a sub-tree is being displyed. An example is shown below: \
\
`├┐`\
`│├─D`\
`│├─E`\
`│├┐`\
`││├─F`\
`││├─G`\
`││├┐`\
`│││├─H`\
`││├┘`\
`│├┘`\
`│├─I`\
`├┘`\
\
Tip: If you cannot see what I mean, look at the first character of every line. That line is unbroken while the sub-tree is being printed. That is the fourth character in every list.

## Credits

Credits go to: \
Pigeon Nation!! :] 