import math
import datetime
import os 
from PIL import Image


def hello(name1):
	print("Hello " + name1 + "!")

def hello2(name1,name2):
	print("Hello " + name1 + " " + name2 + "!")

def sum_two(x,y):
	z = x + y
	return (z)



def circle_area(radius):
	y = radius * radius * math.pi
	return y

def today():
	now = datetime.datetime.now()
	return now.day

def my_sum(a_list):
	total = 0
	for n in a_list:
		total = total + n
	return total

def my_prod(a_list):
	list0 = []
	prod = 1
	for n in a_list:
		prod = prod * n
	if list0 == a_list:
		prod = 0
	return prod

def my_count(a_list):
	count = 0
	for n in a_list:
		count = count + 1
	return count

def my_count_less_5(a_list):
	count = 0
	for n in a_list:
		if n < 5:
			count = count + 1
	return count

def my_count_ones(a_list):
	count = 0
	for n in a_list:
		if n == 1:
			count = count + 1
	return count

def is_list_empty(a_list):
	if my_count(a_list) == 0:
		return True
	else:
		return False

def my_max(a_list):
	if is_list_empty(a_list):
		return None
	else:
		a = a_list[0]
		for n in a_list:
			if n > a:
				a = n 
		return a

def get_filenames(a_dirname):
	list_of_files = os.listdir(a_dirname)
	all_files = list()
	for n in list_of_files:
		full_path = os.path.join(a_dirname,n)
		if not os.path.isdir(full_path):
			all_files.append(full_path)
	return all_files
	
def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed, box)
    return an_image

def open_all_pic_and_rotate(a_dirname):
    photos_list = get_filenames(a_dirname)
    for photo in photos_list:
        im = Image.open(photo)
        im = rotate_box(im)
        im.show()

def to_grayscale(an_image):
	grayscale_im = an_image.convert("LA")
	return grayscale_im

def open_all_pic_and_grayscale(a_dirname):
	photos_list = get_filenames(a_dirname)
	for photo in photos_list:
		im = Image.open(photo)
		im = to_grayscale(im)
		im.show()


def open_rotate_save(a_dirname):
	pic_list = get_filenames(a_dirname)
	anum = 0
	for pic_name in pic_list:
		newfilename = "pic_rotate_" + str(anum) + ".jpg"
		anum = anum + 1
		im = Image.open(pic_name)
		im = rotate_box(im)
		newfullpath = os.path.join("C:\\Users\\Joergson\\Desktop\\pictures\\rotate",newfilename)
		im.save(newfullpath)


def open_grayscale_save(a_dirname):
	pic_list = get_filenames(a_dirname)
	anum = 0
	for pic_name in pic_list:
		newfilename = "pic_gray_" + str(anum) + ".jpg"
		anum = anum + 1
		im = Image.open(pic_name)
		im = to_grayscale(im)
		newfullpath = os.path.join("C:\\Users\\Joergson\\Desktop\\pictures\\grayscale",newfilename)
		im.save(newfullpath)

# [12, 34, [56, 67]] -> [12, 34, 56, 67,]
def flatten(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				new_list.append(i)
		else:
			new_list.append(n)
	return new_list

def print_right(a_list_with_lists):
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				print(i,end="")
			print()
		else:
			print(n)

def new_elements(a_list_with_lists):
	new_list = []
	for n in a_list_with_lists:
		if isinstance(n,list):
			for i in n:
				if not i in new_list:
					print(i)
				new_list.append(i)
				
		else:
			if not n in new_list:
				print(n)
			new_list.append(n)

def single_row_stars(number):
	for n in range(number):
		print("*",end="")

def single_row_of(number,string):
	for n in range(number):
		print(string,end="")


def square_of_stars(number):
	for n in range(number):
		for n in range(number):
			print("*",end="")
		print()


def create_grid(size):
	new_grid = []
	for row in range(size):
		sub_grid = []
		for column in range(size):
			sub_grid.append("-")
		new_grid.append(sub_grid)	
	return new_grid	



def reverse_list(a_list):
	a = my_count(a_list)
	new_list = []
	for n in a_list:
		new_list.append(n)
	count = 0
	for n in a_list:
		position = (count + a) -1
		new_list[position] = n
		count = count - 1
	return new_list

def is_duplicate_there(list_a,list_b):
	for i in list_a:
		if (i in list_b):
			return True
	return False

def what_is_there(list_a,list_b):
	
	new_list = []
	for n in set(list_a):
		if not n in set(list_b):
			new_list.append(n)
	for i in set(list_b):
		if not i in set(list_a):
			new_list.append(i)
	return new_list
	



	return new_list
	

