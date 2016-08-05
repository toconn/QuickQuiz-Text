from ua.core.utils import listutils


def get_parsed_args(argument_parser, arguments):
    
    arguments = arguments[1:]   # Remove the parameter with the app name.
    parsed_arguments = argument_parser.parse_args(arguments)
    parsed_arguments.params = arguments
    
    if listutils.is_empty(parsed_arguments.params):
        parsed_arguments.help_flag = True
        
    return parsed_arguments

def show_defaults(argument_parser, parsed_params, app_info):
    
    if parsed_params.help_flag:
        show_help(argument_parser)
    
    if parsed_params.version_flag:
        show_version(app_info)
        
    if parsed_params.params_flag:
        show_params(parsed_params)

def show_help(argument_parser):

    argument_parser.print_help()
    print('')
        
def show_params(parsed_params):
    
    print ('App Params:')
    print ('  ' + ' '.join(parsed_params.params))
    print ('')

def show_version(app_info):
    
    print ('App Info:')
    print ('  App Version:  ' + app_info.version)
    print ('  Created:      ' + app_info.created_date)
    print ('  Build Date:   ' + app_info.build_date)
    print ('  Build Number: ' + app_info.build_number)
    print ('')

