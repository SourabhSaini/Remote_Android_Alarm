from tkinter import *
import urllib.request as urllib2
import http.cookiejar as cookielib
from getpass import getpass
import sys
import os
from stat import *
from datetime import timedelta,datetime
from math import pi,cos,sin,radians

def textEntered(event):
	text.config(bg="WHITE")
	hour.config(bg="WHITE")
	mins.config(bg="WHITE")

def refresh_clock(event=None):
	canvas.delete(ALL)
	clock()

frame = Tk()
frame.title('Bhulakkad')
width=322
height=156
frame.maxsize(width,height)
frame.minsize(width,height)

screen_width = frame.winfo_screenwidth()
screen_height = frame.winfo_screenheight()

# calculate position x and y coordinates
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
frame.geometry('%dx%d+%d+%d' % (width, height, x, y))


label1 = Label(frame,text="Remind us about:")
label1.pack()
label1.place(x=0,y=0)

text = Entry(frame)
text.bind("<Key>", textEntered)
text.pack()
text.focus_set()
text.place(x=120,y=0,width=200)

label2 = Label(frame,text="At:")
label2.pack()
label2.place(x=0,y=25)

hour = Spinbox(frame,from_="00", to="23",wrap = True,command=refresh_clock)
hour.bind("<Button>", textEntered)
hour.bind("<Key>", textEntered)
hour.bind("<KeyRelease>", refresh_clock)

label3 = Label(frame,text=":")
mins = Spinbox(frame,from_="00", to="59",wrap = True,command=refresh_clock)
mins.bind("<Button>", textEntered)
mins.bind("<Key>", textEntered)
mins.bind("<KeyRelease>", refresh_clock)

hour.pack()
hour.place(x=30,y=25,width=35)
label3.pack()
label3.place(x=63,y=25)
mins.pack()
mins.place(x=70,y=25,width=35)

sun_v,mon_v,tue_v,wed_v,thu_v,fri_v,sat_v = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
global repeat_v
repeat_v = IntVar()

sun = Checkbutton(frame,text="Sun",variable=sun_v)
sun.pack()
sun.place(x=0,y=50)

mon = Checkbutton(frame,text="Mon",variable=mon_v)
mon.pack()
mon.place(x=60,y=50)

tue = Checkbutton(frame,text="Tue",variable=tue_v)
tue.pack()
tue.place(x=120,y=50)

wed = Checkbutton(frame,text="Wed",variable=wed_v)
wed.pack()
wed.place(x=0,y=75)

thu = Checkbutton(frame,text="Thu",variable=thu_v)
thu.pack()
thu.place(x=60,y=75)

fri = Checkbutton(frame,text="Fri",variable=fri_v)
fri.pack()
fri.place(x=120,y=75)

sat = Checkbutton(frame,text="Sat",variable=sat_v)
sat.pack()
sat.place(x=0,y=100)

def toggleAll():
	if repeat_v.get():
		sun.select(), mon.select(), tue.select(), wed.select(), thu.select(), fri.select(), sat.select()
	else:
		sun.deselect(), mon.deselect(), tue.deselect(), wed.deselect(), thu.deselect(), fri.deselect(), sat.deselect()

all_ = Checkbutton(frame,text="All Days",variable=repeat_v,command=toggleAll)
all_.pack()
all_.place(x=60,y=100)

def getValues():
	if text.get() == '' or text.get() == ' ':
		text.config(bg="RED")
	elif hour.get() == '' or hour.get() == ' ' or int(hour.get()) < 0 or int(hour.get()) > 23:
		hour.config(bg="RED")
	elif mins.get() == '' or mins.get() == ' ' or int(mins.get()) < 0 or int(mins.get()) > 59:
		mins.config(bg="RED")
	else:
		message = text.get()+'#'+hour.get()+'/'+mins.get()

	weekdays = 0
	if sun_v.get():
		weekdays += 1
	if mon_v.get():
		weekdays += 2
	if tue_v.get():
		weekdays += 4
	if wed_v.get():
		weekdays += 8
	if thu_v.get():
		weekdays += 16
	if fri_v.get():
		weekdays += 32
	if sat_v.get():
		weekdays += 64

	message += '<>'+str(hex(weekdays))

	#print(message)
	numbers = ['YOUR MOBILE NUMBERS']      #You can give as many numbers you want, example: ['95822xxxx','73378xxxxx']
	if __name__ == "__main__":
		username = "USER NAME HERE"        #Write your Way2SMS user name/mobile no.
		passwd = "YOUR PASSWORD"           #Write your Way2SMS password

		message = "+".join(message.split(' '))

		#logging into the sms site
		url ='http://site24.way2sms.com/Login1.action?'
		data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
		#url = url.encode('UTF-8')
		data = data.encode('UTF8')
		#For cookies
		cj= cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		#Adding header details
		opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
		try:
			usock = opener.open(url, data)
		except IOError:
			os.system('notify-send "Remote Alarm" "Error Occured"')

		for number in numbers:
			jession_id =str(cj).split('~')[1].split(' ')[0]
			send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
			send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
			send_sms_data = send_sms_data.encode('UTF8')
			opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
			try:
				sms_sent_page = opener.open(send_sms_url,send_sms_data)
			except IOError:
				os.system('notify-send "Remote Alarm" "Error while sending Alarm message"')
	        #return()

		print('Success')
		os.system('notify-send "Remote Alarm" "Alarm Set Successfull"')
		#return ()


button = Button(frame,text="Set Alarm", command=getValues)
button.pack()
button.place(x=20,y=125)

###------ANALOG CLOCK------###
#1.Hour angle = [ 360 * (hour % 12) / 12 ] + [ 360 * (minutes / 60) * (1 / 12) ]
#2.Minute angle = 360 * minutes / 60.
#3.Angle between hour and minute = (hour angle - minute angle) % 360.
canvas = Canvas(frame)

def clock():

	global sun_img, moon_img

	if int(hour.get()) <= 12:
		sun_img = PhotoImage(file="sun.png")
		canvas.create_image(53, 58, image=sun_img)
	else:
		moon_img = PhotoImage(file="moon.png")
		canvas.create_image(60, 57, image=moon_img)

	canvas.create_oval(5,5,105,105,width=6)
	center = 55

	#Hour Hand
	length = 30
	angle = ( 360 * (int(hour.get()) % 24) / 12 ) + ( 360 * (int(mins.get()) / 60) * (1 / 12) )
	rads = radians(angle-90)
	hx, hy = length*cos(rads), length*sin(rads)
	canvas.create_line(center, center, center+hx, center+hy,width=4)

	#Minute Hand
	length = 40
	angle = 360 * int(mins.get()) / 60
	rads = radians(angle-90)
	mx, my = length*cos(rads), length*sin(rads)
	canvas.create_line(center, center, center+mx, center+my,width=2)

clock()

canvas.pack()
canvas.place(x=195,y=35)

frame.bind('<Escape>',sys.exit)
frame.mainloop()
