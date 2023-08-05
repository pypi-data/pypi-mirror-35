import argparse

class IndentChanger(object):

    def __init__(self, original='\t', desired='    ', delimiter='\n'):
        """ IndentChanger changes indentation of file or text.
        
            Parameters
            ----------
            original : string
                Indentation used in original text.
                
            desired : string
                Indentation used in desired text.
                
            delimiter : string
                Line delimiter used in text.
            """
        self.original  = original
        self.desired   = desired
        self.delimiter = delimiter
        
    def change(self, text, original=None, desired=None, delimiter=None):
        """ Change indentation of text from original
            indentation to desired indentation.
            
            Parameters
            ----------
            text : string
                Text for which to change the indentation style.
                
            original : string, default=None (optional)
                Indentation used in original text, if None, it uses the
                indentation parameter from the object itself.
                
            desired : string, default=None (optional)
                Desired indentation in output text, if None, it uses the
                indentation parameter from the object itself.
                
            delimiter : string, default=None (optional)
                Line delimiter used in text, if None, it uses the
                delimiter parameter from the object itself.
                
            Returns
            -------
            result : string
                String where the indentation style has changed.
            """
        # Set values to object values if None
        original  = original  or self.original
        desired   = desired   or self.desired
        delimiter = delimiter or self.delimiter
            
        # Split text according to delimiter
        text = text.split(delimiter)
        # Iterate over each line in text
        for index, line in enumerate(text):
            # Split line in chunks of size len(original)
            line = [line[i:i+len(original)] for i, v
                    in enumerate(line) if i%len(original) == 0]
            # Loop over chunks in line
            for i, c in enumerate(line):
                # If chunk equals original, replace
                if c == original:
                    line[i] = desired
                # Otherwise go to next line
                else:
                    break
            # Put line back together
            line = ''.join(line)
            text[index] = line
        # Join lines into text and return
        return delimiter.join(text)
            
            
    def change_file(self, infile, outfile=None, original=None,
                    desired=None, delimiter=None):
        """ Change indentation of text from original
            indentation to desired indentation.
            
            Parameters
            ----------
            infile : string
                Path to file for which to change the indentation style.
                
            outfile : string (optional)
                Path to file to write the output to. If None, it uses the
                infile as the outfile.
                
            original : string, default=None (optional)
                Indentation used in original text, if None, it uses the
                indentation parameter from the object itself.
                
            desired : string, default=None (optional)
                Desired indentation in output text, if None, it uses the
                indentation parameter from the object itself.
                
            delimiter : string
                Line delimiter used in text, if None, it uses the
                delimiter parameter from the object itself.
                
            Returns
            -------
            result : string
                String where the indentation style has changed.
            """		
        # Set outfile to infile values if None
        outfile = outfile or infile
            
        # Read text from infile
        with open(infile, 'r') as infile:
            text = infile.read()
        
        # Change indentation style of text
        text = self.change(text, original, desired, delimiter)
        
        # Write text to outfile
        with open(outfile, 'w') as outfile:
            outfile.write(text)
            

if __name__ == "__main__":
    # Initialise argument parser
    parser = argparse.ArgumentParser(description="Indentation change tool.")
    parser.add_argument('file', nargs='+', type=str, help="File(s) for which"
    " to change indentation.")
    parser.add_argument('-w', '--write'  , type=str, help="File to write output"
    " to (optional, if none is given, change contents of file.")
    parser.add_argument('-o', '--orig'   , type=str, help="Indentation style in"
    " original file (optional, if none is given, use '\\t').")
    parser.add_argument('-t', '--to'     , type=str, help="Indentation style in"
    " desired  file (optional, if none is given, use 4 spaces).")
    parser.add_argument('-d', '--delim'  , type=str, help="Line delimiter in"
    " original file    (optional, if none is given, use '\\n')")
    args = parser.parse_args()
    
    # Create IndentChanger object
    ic = IndentChanger()
    # For each given file, change indentation
    for f in args.file:
        ic.change_file(f, args.write, args.orig, args.to, args.delim)
