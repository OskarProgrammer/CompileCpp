import colorama
import argparse
import os
import subprocess

#g++ {input_file} -o {output_file}

parser = argparse.ArgumentParser(description="Quick compile c++ file to executable")

parser.add_argument("-i","--inputf",help="Input file.",required=True,type=str)

parser.add_argument("-o","--outputf",help="Output file",required=True,type=str)

args = parser.parse_args()


class Script(object):
    def __init__(self,infile:str,outfile:str) -> None:
        self._infile = infile
        self._outfile = outfile

        self.test(f"g++ -o {self._infile} {self._outfile}")

        print(colorama.Fore.GREEN + f"Created {self._outfile} from {self._infile}!")


    def test(self,command):
        print(colorama.Fore.RED,end="")
        self._command = command
        self._returned_value = subprocess.call(command, shell=True)  

        if self._returned_value !=0:
            print(colorama.Fore.RED + f"ERROR During executing \"{self._command}\" command\nExit code: {self._returned_value}")
            exit()
        
        
objekt = Script(args.outputf,args.inputf)
