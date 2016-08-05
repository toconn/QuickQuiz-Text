import sys
from app import App 
import appconst
import appfactory
import apputils


argument_parser = appfactory.new_argument_parser()
parsed_params = apputils.get_parsed_args(argument_parser, sys.argv)
apputils.show_defaults(argument_parser, parsed_params, appconst.APP_INFO)

app = App()
app.main(parsed_params)
