"""
Things for dealing with filenames
"""
import warnings
from os import path
import os

import errno
from typing import Iterable, List, Optional, Union, Sequence

from mhelper.special_types import NOT_PROVIDED
from mhelper import array_helper


def read_all_text( file_name: str, default: Optional[str] = NOT_PROVIDED, *, details: str = None ) -> Optional[str]:
    """
    Reads all the text from a file, returning None if there is no file
    
    :param file_name: Path to file to read
    :param default:   Default value if file does not exist.
                      If `NOT_PROVIDED` then a `FileNotFoundError` is raised.
    :param details:   Appended to `FileNotFoundError` error message.
    :except FileNotFoundError: File does not exist. 
    """
    
    if not os.path.isfile( file_name ):
        if default is NOT_PROVIDED:
            raise FileNotFoundError( "Cannot read_all_text from file because the file doesn't exist: «{}».{}".format( file_name, (" Description of file: {}.".format( details )) if details else "" ) )
        
        return default
    
    with open( file_name, "r" ) as file:
        return file.read()


def get_subdirs( directory_name: str ) -> List[str]:
    results = []
    
    for file_name in os.listdir( directory_name ):
        full_name = os.path.join( directory_name, file_name )
        if path.isdir( full_name ):
            results.append( full_name )
    
    return results


def read_all_lines( file_name: str ) -> List[str]:
    """
    Reads all the text from a file.
    
    :except FileNotFoundError: File not found
    """
    
    if not os.path.isfile( file_name ):
        raise FileNotFoundError( "The file «{}» does not exist.".format( file_name ) )
    
    with open( file_name, "r" ) as file:
        return list( x.rstrip( "\n" ) for x in file )


def write_all_text( file_name: object, text: Union[Sequence[str], str], newline: bool = False ) -> None:
    """
    Writes all text to a file, overwriting the existing content
    """
    
    if array_helper.is_simple_iterable( text ):
        text = "\n".join( text )
        
        if newline:
            text += "\n"
    
    with open( str( file_name ), "w" ) as file:
        file.write( text )


def contains_files( directory: str, ext: str ) -> bool:
    """
    Returns if the directory contains any files.
    """
    ext = ext.upper()
    
    for root, dirs, files in os.walk( directory ):
        for file in files:
            if file.upper().endswith( ext ):
                return True
    
    return False


def get_file_name( full_path: str ) -> str:
    """
    Returns <FILE><EXT> from <PATH><FILE><EXT>
    `a/b/c.d` --> `c.d`
    """
    return path.split( full_path )[1]


def replace_extension( file_name: str, new_extension: str ) -> str:
    """
    Replaces <EXT> in <PATH><FILE><EXT>
    `a/b/c.d` <-- `d`
    """
    return path.splitext( file_name )[0] + new_extension


def get_extension( file_name: str ) -> str:
    """
    Returns <EXT> in <PATH><FILE><EXT>. Note this includes the ".".
    `a/b/c.d` --> `.d`
    """
    return path.splitext( file_name )[1]


def get_filename( file_name: str ) -> str:
    """
    Returns <FILE><EXT> in <PATH><FILE><EXT>
    `a/b/c.d` --> `c.d`
    """
    return path.split( file_name )[1]


def get_filename_without_extension( file_name: str ) -> str:
    """
    Returns <FILE> from <PATH><FILE><EXT>
    `a/b/c.d` --> `c`
    """
    file_name = path.split( file_name )[1]
    file_name = path.splitext( file_name )[0]
    return file_name


def get_full_filename_without_extension( file_name: str ) -> str:
    """
    Returns <PATH><FILE> from <PATH><FILE><EXT>
    `a/b/c.d` --> `a/b/c`
    """
    return path.splitext( file_name )[0]


def replace_filename_without_extension( file_name: str, new_name: str ) -> str:
    """
    Replaces <NAME> in <PATH><NAME><EXT>
    `a/b/c.d` <-- `c`
    """
    return path.join( get_directory( file_name ), new_name + get_extension( file_name ) )


def replace_filename( file_name: str, new_name: str ):
    """
    Replaces <NAME><EXT> in <PATH><NAME><EXT>
    `a/b/c.d` --> `c.d`
    """
    return path.join( get_directory( file_name ), new_name )


def join( *args, **kwargs ):
    """
    Just calls path.join
    """
    return path.join( *args, **kwargs )


def get_directory_name( file_name: str ) -> str:
    return get_filename( get_directory( file_name ) )


def get_directory( file_name: str, up = 1 ) -> str:
    """
    Returns <PATH> in <PATH><NAME><EXT>
    """
    for _ in range( up ):
        file_name = path.split( file_name )[0]
    
    return file_name


def suffix_directory( file_name: str ) -> str:
    if file_name.endswith( path.sep ):
        return file_name
    else:
        return file_name + path.sep


def relocate( target_files: Iterable[str], new_folder: str, locate: bool ) -> None:
    """
    Given a list of files, creates a set of symbolic links to them in another folder. 
    :param target_files: List of files (complete paths unless locate is False, in which case they can be partial paths) 
    :param new_folder: Folder to create links in or remove links from  
    :param locate: Whether to create links (True) or remove them (False) 
    """
    for file in target_files:
        name = get_file_name( file )
        new_name = path.join( new_folder, name )
        
        if locate:
            os.link( file, new_name )
        else:
            os.unlink( new_name )


def split_path( path_: str ) -> List[str]:
    """
    Splits a name into its folders and file
    """
    
    folders = []
    
    while 1:
        path_, folder = os.path.split( path_ )
        
        if folder != "":
            folders.append( folder )
        else:
            if path_ != "":
                folders.append( path_ )
            break
    
    folders.reverse()
    
    return folders


def sub_dirs( directory: str ) -> List[str]:
    """
    Lists the subdirectories as absolute paths.
    """
    return [x for x in list( path.join( directory, x ) for x in os.listdir( directory ) ) if os.path.isdir( x )]


def list_dir( directory: str, filter: str = None, recurse: bool = False ) -> List[str]:
    """
    Lists the contents of a directory as absolute filenames.
    Note that the results do not include directories - use `sub_dirs` for that.
    
    :param directory:       Directory to list. 
    :param filter:          Filter on files (e.g. `".txt"`). Case insensitive.  
    :param recurse:         Recurse into subfolders. 
    :return:                List of absolute filenames. 
    """
    if recurse:
        result = []
        for folder, subfolders, files in os.walk( directory ):
            for file in files:
                result.append( path.join( folder, file ) )
    else:
        result = [x for x in list( path.join( directory, x ) for x in os.listdir( directory ) ) if os.path.isfile( x )]
    
    if filter:
        filter = filter.upper()
        result = [x for x in result if x.upper().endswith( filter )]
    
    return result


def is_windows() -> bool:
    """
    Returns if the current platform is Windows.
    """
    return os.name == "nt"


def default_extension( file_name: str, extension: str ) -> str:
    """
    Returns the `file_name` if it has any extension, otherwise adds the `extension`.
    """
    if not get_extension( file_name ):
        return file_name + extension
    
    return file_name


def create_directory( output_directory: str ):
    """
    Creates a directory (doesn't do anything if it already exists)
    """
    
    if path.isdir( output_directory ):
        return
    
    try:
        os.makedirs( output_directory )
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise FileNotFoundError( "Failed to create directory «{}» due to another error.".format( output_directory ) ) from exception
    
    if not path.isdir( output_directory ):
        raise FileNotFoundError( "Command returned success but the created directory cannot be found «{}».".format( output_directory ) )


def line_count( file_name: str, line_start: Optional[str] = None ) -> int:
    """
    Counts the number of lines in a file, optionally those just starting "line_start"
    """
    
    c = 0
    
    with open( file_name ) as f:
        for line in f:
            if (not line_start) or (line.startswith( line_start )):
                c += 1
    
    return c


def safe_file_name( name ):
    name = str( name )
    name = name.replace( "<>:\"'/\\|?*", "_" )
    
    if not name:
        return "Untitled"
    else:
        return name


def recycle_file( file_name ):
    try:
        # noinspection PyPackageRequirements
        from send2trash import send2trash
        send2trash( file_name )
    except ImportError:
        warnings.warn( "The `send2trash` module is not installed so instead of sending the file '{}' to the recycle bin I am just going to delete it. Please install `send2trash` to avoid this warning in future.".format( file_name ), UserWarning )
        os.remove( file_name )


def get_last_directory_and_filename( file_name ):
    """
    From `a/b/c/d.e` gets `c/d.e` 
    """
    return path.join( get_filename( get_directory( file_name ) ), get_filename( file_name ) )


def delete_file( file_name: str ) -> bool:
    """
    Deletes the file, if it exists.
    :return: Was deleted
    """
    if path.isfile( file_name ):
        os.remove( file_name )
        return True
    
    return False


def home() -> str:
    """
    Returns the home directory.
    :return: 
    """
    return path.expanduser( "~" )  # TODO: Does this work on Windows?


def file_size( file_name: str ) -> int:
    """
    Size of a file, or -1 on error.
    """
    try:
        return os.stat( file_name ).st_size
    except:
        return -1


def sequential_file_name( file_name: str ) -> str:
    """
    Generates a sequential file OR directory name.
    
    Avoids conflicts with existing filenames.
    
    :remarks:
    No multi-thread support - only acknowledges existing files.
    
    :param file_name: Format of filename, with * where the number goes.
    :return: Full filename
    """
    if "*" not in file_name:
        raise ValueError( "`sequential_file_name` requires the filename to contain a placeholder '*' to represent the number, but the value provided «{}» does not.".format( file_name ) )
    
    number = 1
    
    result = file_name.replace( "*", str( number ) )
    
    while path.exists( result ):
        number += 1
        result = file_name.replace( "*", str( number ) )
    
    return result


def highlight_file_name_without_extension( file, highlight, normal ):
    return normal + path.join( get_directory( file ), highlight + get_filename_without_extension( file ) + normal + get_extension( file ) )


def assert_working_directory():
    """
    Having a bad working directory causes weird problems with everything else, even getting a stack trace.
    Assert it exists before we do anything else.
    """
    try:
        os.getcwd()
    except Exception as ex:
        raise ValueError( "Cannot obtain the working directory. Check the current folder exists and try again." ) from ex


# region Deprecated

def file_len( file_name: str, line_start: Optional[str] = None ) -> int:
    warnings.warn( "DEPRECATED (3 aug 2018, misleading name) - use line_count", DeprecationWarning )
    return line_count( file_name, line_start )

# endregion
