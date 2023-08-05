"""
Contains all functions used for parsing the command line args
"""
import argparse,argcomplete
import textwrap


def parse_arguments(command):
    """
    Parses the command into arguments and flags
    :param command: the command in list form
    :return: an object that contains the values for all arguments

    Currently, all help messages are not in use and helpman() is the default.
    Need to implement nicer --help format in the future.
    """
    parser = argparse.ArgumentParser(description=textwrap.dedent('Stack Overflow command line client'), add_help=False)

    # Comment this line out if you want to use argparse's default help function
    parser.add_argument('--help', '-h', action='store_true', help='Show this help message and exit')

    # Flags that return true if present and false if not
    parser.add_argument('--new', '-n', action='store_true',
                        help=textwrap.dedent("Opens the stack overflow new questions page in your "
                                             "default browser. You can create a new question using it."))
    parser.add_argument('--interactive', '-i', action='store_true', help=textwrap.dedent(
        "To search in Stack Overflow and display the matching results. "
        "You can choose and browse any of the results interactively"))
    parser.add_argument('--debug', action='store_true', help="Turn debugging mode on")
    parser.add_argument('--sosearch', '-s', action='store_true',
                        help="Searches directly on Stack Overflow instead of using Google")
    parser.add_argument('--api', '-a', action='store_true', help="Sets a custom API key for socli")
    parser.add_argument('--delete', '-d', action='store_true',
                        help="Deletes the configuration file generated by socli -u command")

    # Accepts 1 argument. Returns None if flag is not present and
    # 'STORED_USER' if flag is present, but no argument is supplied
    parser.add_argument('--user', '-u', nargs='?', const='(RANDOM_STRING_CONSTANT)', type=str,
                        help="Displays information about the user "
                             "provided as the next argument(optional). If no argument is provided "
                             "it will ask the user to enter a default username. Now the user "
                             "can run the command without the argument")

    # Accepts one or more arguments
    parser.add_argument('--tag', '-t', nargs='+', help="To search a query by tag on stack overflow."
                                                       "Visit http://stackoverflow.com/tags to see the list of all "
                                                       "tags.\n   eg:- socli --tag javascript,node.js --query "
                                                       "foo bar: Displays the search result of the query"
                                                       " \"foo bar\" in stack overflow's javascript and node.js tags")
    parser.add_argument('--query', '-q', nargs='+', default=[],
                        help="If any of the following commands are used then you "
                             "must specify this option and a query following it.")
    parser.add_argument('--browse', '-b', nargs='+', default=[],
                        help="Searches for ten hot,week and interesting questions on today's page.")
    # Accepts 0 or more arguments. Used to catch query if no flags are present
    parser.add_argument('userQuery', nargs='*', help=argparse.SUPPRESS)

    # Accepts 1 argument
    parser.add_argument('--res', '-r', type=int, help="To select and display a result manually and display "
                                                      "its most voted answer. \n   eg:- socli --res 2 --query "
                                                      "foo bar: Displays the second search result of the query"
                                                      " \"foo bar\"'s most voted answer")
    parser.add_argument('--open-url', '-o', nargs=1, type=str, help='To load the given url')
    parser.add_argument('--json', '-j', action='store_true', help='Write output to stdout as json')
    parser.add_argument('--register', '-g', action='store_true', help='Registers socli\'s shell autocompletion')
    parser.add_argument('--version' , '-v', action='store_true', help='Prints the current version of socli')
    
    argcomplete.autocomplete(parser)
    namespace = parser.parse_args(command)
    return namespace
