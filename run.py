import converter.converter as converter
import sys

# run file with url and unit as arguments 

url = sys.argv[1]
unit = sys.argv[2]
if unit != "ounces" and unit != "grams":
    print('unit must be "ounces" or "grams". Please re-run with the correct formatting')
else:
    converter.convert(url, unit)