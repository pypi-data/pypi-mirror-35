import os
import subprocess
from mhelper import ansi


def run( *args, **kwargs ):
    return run_subprocess( *args, **kwargs )


def run_subprocess( wd: str, cmd: str, *, echo = False ) -> str:
    """
    Runs a command (`cmd`) in the specified working directory (`wd`), returning std.out.
    """
    
    if not os.path.isdir( wd ):
        raise FileNotFoundError( "Not a directory: " + wd )
    
    if echo:
        print( ansi.FORE_YELLOW + "cd {}".format( wd ) + ansi.RESET )
        
    os.chdir( wd )
    
    if echo:
        print( ansi.FORE_YELLOW + "{}".format( cmd ) + ansi.RESET )
    p = subprocess.Popen( [cmd], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True )
    stdout = p.stdout.read().decode( "utf-8" )
    stderr = p.stderr.read().decode( "utf-8" )
    
    if stdout:
        for line in stdout.split( "\n" ):
            line = "O>" + ansi.DIM + ansi.FORE_GREEN + line + ansi.RESET
            print( line )
    
    if stderr:
        for line in stderr.split( "\n" ):
            line = "E>" + ansi.DIM + ansi.FORE_RED + line + ansi.RESET
            print( line )
            
    return stdout
