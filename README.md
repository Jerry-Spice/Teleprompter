# Teleprompter
## By Josh Brandon

This program is run through the GUI file.


#GUI.py
  - This is the main file which uses tkinter to create the tkinter window and start the process of reading in the script from a 'docx' file
#teleprompter
  - This is the frontend which uses pygame and a series of pygame text elements to display the actual teleprompter. Uses the scrollwheel to adjust the fontsize
  - To update the fontsize one must close the teleprompter and reprocess the file
#wordProcessor
  - This is the backend which takes in a docx file and reads the contents according to a few rules
  - _Anchors or different speakers are denoted with '[Name Here]'_
  - _Colons (':') and apostrophes (" ' ") will be removed from the script due to formatting and issues with Microsoft Word's text processing_
  - Every paragraph break must be a new speaker or else the speaker labels break down. _I.e [Anchor 1]: Words words words \n [Anchor 2]: Foo Bar Foo Bar 
  - The final file which is read into the teleprompter is called 'WordFives.txt' which describes how this processor splits the script into groups of five words for ease of reading and maximum font size on the teleprompter.
#Issues
  - Should the teleprompter also close the GUI or should it just close the teleprompter window?
  - The wordProcessor doesn't always organize the 'wordFives' correctly. Sometimes they're 'wordThrees'
