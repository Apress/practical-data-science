# encoding: utf-8
import sys
from argparse import ArgumentParser
from xml.dom import minidom
try:
	from urllib.request import urlopen
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlopen, urlencode


API_URL = "http://www.google.com/ig/api?"

def main():
	arguments = ArgumentParser(prog="weather")
	arguments.add_argument("--unit", choices="CF", dest="unit", default="C", help="Which unit to display the temperatures in")
	arguments.add_argument("location", nargs="+")
	args = arguments.parse_args(sys.argv[1:])

	for location in args.location:
		url = API_URL + urlencode({"weather": location})
		xml = urlopen(url).read()
		doc = minidom.parseString(xml)

		forecast_information = doc.documentElement.getElementsByTagName("forecast_information")[0]
		city = forecast_information.getElementsByTagName("city")[0].getAttribute("data")

		current_conditions = doc.documentElement.getElementsByTagName("current_conditions")[0]
		temp = current_conditions.getElementsByTagName("temp_f" if args.unit == "F" else "temp_c")[0].getAttribute("data")
		condition = current_conditions.getElementsByTagName("condition")[0].getAttribute("data")
		wind_condition = current_conditions.getElementsByTagName("wind_condition")[0].getAttribute("data")
		humidity = current_conditions.getElementsByTagName("humidity")[0].getAttribute("data")

		indent = "  "
		print("Weather for {0}:".format(city))
		print(indent + "{0}°{1}".format(temp, args.unit))
		print(indent + condition)
		print(indent + wind_condition)
		print(indent + humidity)

if __name__ == "__main__":
	main()