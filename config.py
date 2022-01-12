
# from main import get_barcode_name
# papername = get_barcode_name()
from commandconfig import CBAppCmd001 as details

camera = "http://192.168.225.109:8080//video"
roi = details.roi
lower_hsv = details.paper_lower_hsv
upper_hsv = details.paper_upper_hsv
application_names = details.application_names
command = details.command

outputresolution = [[0,0], [0, 1080], [1920, 1080],[1920,0]]

header_lower_hsv_values = details.header_lower_hsv_values
header_upper_hsv_values = details.header_upper_hsv_values

