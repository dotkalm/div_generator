import os
from flask import Blueprint, request, jsonify 
from PIL import Image

api = Blueprint('api', 'api2', url_prefix="/api/v1")
def color_value(form_picture, size):
    output_size = (size, size)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    dims = i.size
    print(i.size, '<--- image size')
    pix = i.load()
    color_str = ''
    list_for_colors = {} 
    for x in range (0,i.size[0]):
        column = str(x + 1)
        list_for_colors[column] = {}
        for y in range (0,i.size[1]):
            row = str(y + 1)
            list_for_colors[column][row] = {}
            rgb_values = pix[x,y]
            list_for_colors[column][row]['r'] = rgb_values[0]
            list_for_colors[column][row]['g'] = rgb_values[1]
            list_for_colors[column][row]['b'] = rgb_values[2]
    print(list_for_colors)
    return list_for_colors 

def avg_color(form_picture):
    output_size = (1,1)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    dims = i.size
    print(i.size, '<--- image size')
    pix = i.load()
    rgb_values = pix[0,0]
    return rgb_values

@api.route('/items/', methods=["POST"])
def create_junk():
    print(request, '<--request')
    print(request.files, '<--request.files')
    pay_file = request.files
    payload = request.form.to_dict()
    dict_file = pay_file.to_dict()
    print(payload, '<-- payload')
    print(dict_file, '<--dict_file')
    array_of_images = dict_file['image']
    two_x_two_color = color_value(array_of_images, 2)
    four_x_four_color = color_value(array_of_images, 4)
    eight_x_eight_color = color_value(array_of_images, 8)
    sixteen_x_sixteen_color = color_value(array_of_images, 16)
    thirty_two_x_thirty_two_color = color_value(dict_file['image'], 32)
    #sixtyfour_x_sixtyfour_color = color_value(dict_file['image'], 64)

    avgRGB = avg_color(array_of_images)
    color_object = {}
    color_object['name'] = payload['name']
    color_object['height'] = int(payload['height'])
    color_object['width'] = int(payload['width']) 
    color_object['r'] = avgRGB[0]
    color_object['g'] = avgRGB[1]
    color_object['b'] = avgRGB[2]
    color_object['2'] = two_x_two_color 
    color_object['4'] = four_x_four_color
    color_object['8'] = eight_x_eight_color
    color_object['16'] = sixteen_x_sixteen_color
    color_object['32'] = thirty_two_x_thirty_two_color
   # color_object['64'] = sixtyfour_x_sixtyfour_color
    return jsonify(data=color_object, status={"code":201, "message":"success"})

