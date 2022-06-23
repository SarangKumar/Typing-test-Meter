from tkinter import *
import RandomWordsGenerator as r
from time import time, sleep
from tkinter import messagebox

root = Tk()
root.geometry('550x600')
root.title('Typing Test Meter')
root.resizable(False, False)
# root.iconbitmap("main_icon1.ico")

# ?--------------------------color--------------------------

color_dict = {1:['#A8DADB', '#457B9D', '#D99886'], 2:['#B98039', '#F3DA4C', '#5E5F71'], 3: ['#ff8c00', '#292826', '#fff'],
              4: ['#581845', '#900c3f', '#ffc30f'], 5:['#283350', '#ABD6DF', '#262626'], 6: ['#c72c41', '#292826', '#fff'],
              7: ['#ddb7ab', '#8faa8c', '#454545'], 8:['#283350', '#ABD6DF', '#262626'], 9: ['#c72c41', '#292826', '#fff'],}
primary_color = color_dict[6][0]
secondary_color = color_dict[6][1]
third_color = color_dict[6][2]

root.config(bg=primary_color)

# ?--------------------------functions--------------------------
user_name = '' 
f_name = ''
l_name = ''
syllabus = ''
words = ''
difficulty = ''
end = ''
start = ''
u_string = ''
accuracy = 0
net_speed = 0
typing_speed = 0

def frame_forget():
    frame1.forget()
    frame2.forget()
    frame3.forget()
    frame4.forget()
    frame5.forget()
    # frame6.forget()
  
def f1_close_f2_open():
  global user_name
  global f_name
  global l_name
  global email
  f_name = input1_f2_frame2.get()
  l_name = input2_f2_frame2.get()
  email = input3_f2_frame2.get()
  user_name = f_name+' '+l_name
  
  # validation
  if user_name==' ' and email=='':
    messagebox.showinfo('Notice', 'Input field is empty!!')
  elif user_name==' ' and '@' not in email:
    messagebox.showinfo('Notice', 'User Name field is empty and email not valid!')
  elif user_name==' ' and'@' in email:
    messagebox.showinfo('Notice', 'User Name field is empty!')
  elif  user_name!=' ' and email=='':
    messagebox.showinfo('Notice', 'Email field is empty!!')
  elif  user_name!=' ' and '@' not in email or '.' not in email:
    messagebox.showinfo('Notice', 'Email not valid!!')
  else:
    frame_forget()
    frame2.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

def f2_close_f3_open():
  if var_agree.get()==0:
    messagebox.showinfo('Notice', 'Please agree to the terms and conditions.')
  elif var_agree.get()==1:
    frame_forget()
    frame3.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=0, pady=20)

def f3_close_f4_open():
  global difficulty
  global words
  global syllabus
  difficulty = var_set_diff.get()
  words = var_set_words.get()
  syllabus = my_listbox.get(ANCHOR)
  if syllabus =='':
    messagebox.showinfo('Notice', 'Some fields are empty, please see to that!')
  else:
    frame_forget()
    frame4.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

def f4_close_f5_open():
  frame_forget()
  frame5.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

  wpm_100 = "You are in the top 1% of typist! Congratulations!"
  tip = { 0:  'There must be something wrong with inputs, consider retrying',
        10: 'Equivalent to one word every 6 seconds. Learn the proper typing technique and pratice to improve your speed.',
        20: 'Equivalent to one word every 3 seconds. Focus on your technique and keep practicing.',
        30: 'Better, but still below average. Keep practising to improve your speed and accuracy.',
        40: 'At this wpm now you are an average typist. You still have significant room for improvement',
        50: 'Congratulations! You\'re above average now.', 
        60: 'This is the speed required for most jobs. You can now be a professional typist.',
        70: 'You are way above average and would qualify for any typing job, assuming your accuracy is high enough.',
        80:  "You are catch! Any employer looking for a typist would love to have you.",
        90: "At this speed you are probably a gamer, coder or a genius. You're doing great!!",
        100: wpm_100, 110:wpm_100, 120:wpm_100, 130:wpm_100, 140:wpm_100, 150:wpm_100, 160:wpm_100, 170:wpm_100, 180:wpm_100, 190:wpm_100,
        200: wpm_100, 210:wpm_100, 220:wpm_100, 230:wpm_100, 240:wpm_100, 250:wpm_100, 260:wpm_100, 270:wpm_100, 280:wpm_100, 290:wpm_100,
        300: wpm_100, 310:wpm_100, 320:wpm_100, 330:wpm_100, 340:wpm_100, 350:wpm_100, 360:wpm_100, 370:wpm_100, 380:wpm_100, 390:wpm_100}

  rating = ''
  if 0 <= accuracy <= 25:
      rating = 'You need to work on your accuracy'
  elif 25 < accuracy <= 45:
      rating = 'More practice is required'
  elif 45 < accuracy <= 60:
      rating = 'Little practice is required'
  elif 60 < accuracy <= 80:
      rating = 'Average accuracy'
  elif 80< accuracy <=95:
      rating = 'Impressive accuracy'
  else:
      rating=" CONGRATULATIONS! You are  Absolutely accurate"

  # print("Your typing speed is "+ str(typing_speed) + 'wpm\n' + 'Your net speed is '+ str(net_speed) + 'wpm\n' +'Your accuracy is '+ str(accuracy) + '%\n')
  
  label1_f1_frame5 = Label(f1_frame5, text = "Your typing speed is "+ str(typing_speed) + 'wpm\n' + 'Your net speed is '+ str(net_speed) + 'wpm\n' +'Your accuracy is '+ str(accuracy) + '%\n', bg=secondary_color, fg = third_color)
  label1_f1_frame5.pack(fill='y', expand=1)
  
  label2_f1_frame5 = Label(f2_frame5, text = '\n' + 'Accuracy:', bg=secondary_color, fg = primary_color)
  label2_f1_frame5.pack(fill='y', expand=1)
  
  label2_f1_frame5 = Label(f2_frame5, text =rating +'\n', bg=secondary_color, fg = third_color)
  label2_f1_frame5.pack(fill='y', expand=1)
  
  label2_f1_frame5 = Label(f2_frame5, text ='Net Speed:', bg=secondary_color, fg = primary_color)
  label2_f1_frame5.pack(fill='y', expand=1)
  
  label2_f1_frame5 = Label(f2_frame5, text = tip[(net_speed-net_speed%10)] + '\n', bg=secondary_color, fg = third_color)
  label2_f1_frame5.pack(fill='y', expand=1)

def f2_close_f1_open():
  frame_forget()
  frame1.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)


def f3_close_f2_open():
  frame_forget()
  frame2.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

def f4_close_f3_open():
  frame_forget()
  frame3.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)
  btn_frame4.config(text='Click to get the text', command=generate_text, fg = primary_color, bg=secondary_color, font=('Helvetica', 10, 'bold'))

def f5_close_f4_open():
  frame_forget()
  frame4.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)
  
def generate_text():
  global start
  btn0_frame_f4_end.config(state='disabled')
  btn1_frame_f4_end.config(state='disabled')
  btn2_frame_f4_end.config(state='disabled')

  sleep(1.25)
  start = time()
  btn_frame4.config(text='Click to Submit', command=generate_submit)
  
  # labelbox1 = ['top row','home row','bottom row','top and home row','home and bottom row','top and bottom row','common english words']

  if syllabus==labelbox1[0]:
    global g_string
    global u_string
    g_string = r.randomiser_top_row(difficulty, words)
  elif syllabus==labelbox1[1]:
    g_string = r.randomiser_home_row(difficulty, words)
  elif syllabus==labelbox1[2]:
    g_string = r.randomiser_bottom_row(difficulty, words)
  elif syllabus==labelbox1[3]:
    g_string = r.randomiser_top_home_row(difficulty, words)
  elif syllabus==labelbox1[4]:
    g_string = r.randomiser_home_bottom_row(difficulty, words)
  elif syllabus==labelbox1[5]:
    g_string = r.randomiser_top_bottom_row(difficulty, words)
  elif syllabus==labelbox1[6]:
    g_string = r.randomiser_common_eng_words(difficulty, words)

  label_rules_f4.delete("1.0","end")
  label_rules_f4.insert(END, g_string)

def generate_submit():
  global end
  global accuracy
  global net_speed
  global typing_speed

  u_string = entry_rules_f4.get(1.0, "end-1c") 
  end = time()
  k = list(zip(g_string.split(), u_string.split()))

  btn0_frame_f4_end.config(state='normal')
  btn1_frame_f4_end.config(state='normal')
  btn2_frame_f4_end.config(state='normal')
  time_taken = end-start

  # calculations
  score = sum([1 for i in k if k[0]==k[1]])
  typing_speed = round(60*len(u_string.split())/(end-start))
  score = sum([1 for i in range(len(k)) if k[i][0]==k[i][1]])
  accuracy = round(score/len(g_string.split())*100,2)
  net_speed = round(typing_speed*accuracy*(1/100))

  lbl_frame4.config(text="Your typing speed is "+ str(typing_speed) + 'wpm\n' + 'Your net speed is '+ str(net_speed) + 'wpm\n' +'Your accuracy is '+ str(accuracy) + '%\n')

def close():
  root.destroy()

# ###############################CODE STARTS###############################

# ?--------------------------frame1 starts--------------------------
frame1 = Frame(root, width=500, bg=secondary_color)
frame1.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

label_f1_01 = Label(frame1, text='Typing meter', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f1_01.pack(pady=10)

label_f1_02 = Label(frame1, text = 'Enter your Particulars', fg = primary_color, bg=secondary_color, font=('Helvetica', 16, 'bold'))
label_f1_02.pack(pady=2)

f2_frame1 = Frame(frame1, bd=10, bg=secondary_color)
f2_frame1.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

f1_frame2 = Frame(f2_frame1, width=5, bd=10, bg=secondary_color)
f1_frame2.grid(row=0, column=0, padx=50)

f2_frame2 = Frame(f2_frame1, width=5, bd=10, bg=secondary_color)
f2_frame2.grid(row=0, column=1, columnspan=2 , padx=0)

label1_f1_frame2 = Label(f1_frame2, text='Enter your first name: ',bg=secondary_color, fg = third_color)
label1_f1_frame2.pack(anchor='e', pady=2)

label2_f1_frame2 = Label(f1_frame2, text='Enter your last name: ', fg = third_color,bg=secondary_color)
label2_f1_frame2.pack(anchor='e', pady=2)

label3_f1_frame2 = Label(f1_frame2, text='Enter your email address: ', fg = third_color,bg=secondary_color)
label3_f1_frame2.pack(anchor='e', pady=2)

input1_f2_frame2 = Entry(f2_frame2, width=30)
input1_f2_frame2.pack(anchor='w', ipadx=1, ipady=1, pady=1)

input2_f2_frame2 = Entry(f2_frame2, width=30)
input2_f2_frame2.pack(anchor='w', ipadx=1, ipady=1, pady=1)

input3_f2_frame2 = Entry(f2_frame2, width=30)
input3_f2_frame2.pack(anchor='w', ipadx=1, ipady=1, pady=1)

frame_f1_end = Frame(frame1, relief='sunken', bd=2)
frame_f1_end.pack(side = BOTTOM, fill='x')

lbl1_frame_f1_end = Label(frame_f1_end, text='Page 1 of 5', width=10)
lbl1_frame_f1_end.pack(side=LEFT, pady=2)

btn1_frame_f1_end = Button(frame_f1_end, text='NEXT', width=10, fg = 'white', bg = secondary_color, command=f1_close_f2_open, activebackground=primary_color, activeforeground=secondary_color)
btn1_frame_f1_end.pack(side=RIGHT, pady=2, padx=2)

btn2_frame_f1_end = Button(frame_f1_end, text='CLOSE', width=10, fg = 'white', bg = secondary_color, command=close, activebackground=primary_color, activeforeground=secondary_color)
btn2_frame_f1_end.pack(side=RIGHT, pady=2, padx=2)
# ?--------------------------frame1 ends--------------------------


# ?--------------------------frame2 starts--------------------------
frame2 = Frame(root, bg=secondary_color)

label_f2_01 = Label(frame2, text='Typing meter', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f2_01.pack(pady=10)

label_f2_02 = Label(frame2, text = 'Rules of the game', fg = primary_color, bg=secondary_color, font=('Helvetica', 16, 'bold'))
label_f2_02.pack(pady=2)

labelframe_f2 = LabelFrame(frame2, text='Rules', fg = primary_color, bg=secondary_color)
labelframe_f2.pack(fill='y',ipadx=10, ipady=5, expand = 'yes', padx=5, pady=2)

label_rules = Text(labelframe_f2, height=10, width=200, fg = third_color, bg=secondary_color, relief='flat')
label_rules.pack(padx=10, pady=10)

rules = "**RULES : \n1. After you agree to the rules mentioned below, click next then Choose the type of test you want to attempt, the level of difficulty and the nature of sample generated.\nNOTE: you can choose only one option from each\n2:  Press the button \"click to get the text\" Type the given test sample carefully as soon as possible and click on submit.\n3:  Your net speed along with accuracy and remarks will be shown below.\nALL THE VERY BEST"
label_rules.insert(END, rules)

f3_frame2 = Frame(frame2, bg=secondary_color)
f3_frame2.pack(anchor='w')

var_agree = IntVar()
var_agree.set(0)

radio1_agree = Radiobutton(f3_frame2, text="I don't agree to the rules", var = var_agree, value=0, fg = primary_color, bg=secondary_color, activebackground=secondary_color, activeforeground=primary_color)
radio2_agree = Radiobutton(f3_frame2, text='I agree to the rules', var = var_agree, value=1, fg = primary_color, bg=secondary_color, activebackground=secondary_color, activeforeground=primary_color)

radio1_agree.grid(row=1, column=0,sticky='w', padx=10)
radio2_agree.grid(row=0, column=0,sticky='w', padx=10)

frame_f2_end = Frame(frame2, relief='sunken', bd=2)
frame_f2_end.pack(side = BOTTOM, fill='x')

lbl1_frame_f2_end = Label(frame_f2_end, text='Page 2 of 5', width=15)
lbl1_frame_f2_end.pack(side=LEFT, pady=2)

btn0_frame_f2_end = Button(frame_f2_end, text='NEXT', width=10, fg = third_color, bg = secondary_color, command=f2_close_f3_open)
btn0_frame_f2_end.pack(side=RIGHT, pady=2, padx=2)

btn1_frame_f2_end = Button(frame_f2_end, text='BACK', width=10, fg = 'white', bg = secondary_color, command=f2_close_f1_open)
btn1_frame_f2_end.pack(side=RIGHT, pady=2, padx=2)

btn2_frame_f2_end = Button(frame_f2_end, text='CLOSE', width=10, fg = third_color, bg = secondary_color, command=close )
btn2_frame_f2_end.pack(side=RIGHT, pady=2, padx=2)
# ?--------------------------frame2 ends--------------------------

# ?--------------------------frame3 starts--------------------------
frame3 = Frame(root, bg=secondary_color)
# frame3.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=20)

label_f3_01 = Label(frame3, text='Typing meter', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f3_01.pack(pady=10)

label_f3_02 = Label(frame3, text = 'Choose the difficulty', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f3_02.pack(pady=2)

f1_frame3 = Frame(frame3, bg=secondary_color)
f1_frame3.pack(fill='both',ipadx=50, ipady=5, expand = 'yes', padx=20, pady=2)

label_frame1_f1_frame3 = LabelFrame(f1_frame3, text='Set_Syllabus', fg = primary_color, bg=secondary_color, height = 3)
label_frame1_f1_frame3.pack(fill='both',ipadx=5, ipady=5, expand = 'yes', padx=5, pady=2)

label_frame2_f1_frame3 = LabelFrame(f1_frame3, text='Set_Difficulty', fg = primary_color, bg=secondary_color)
label_frame2_f1_frame3.pack(fill='both',ipadx=5, ipady=5, expand = 'yes', padx=5, pady=2)

label_frame3_f1_frame3 = LabelFrame(f1_frame3, text='Set_Words', fg = primary_color, bg=secondary_color)
label_frame3_f1_frame3.pack(fill='both',ipadx=5, ipady=5, expand = 'yes', padx=5, pady=2)

labelbox1 = ['top row','home row','bottom row','top and home row','home and bottom row','top and bottom row','common english words']

my_listbox = Listbox(label_frame1_f1_frame3, width=100, fg = third_color, bg=secondary_color, relief='flat')

for i in labelbox1:
  my_listbox.insert(END, i)

my_listbox.pack()

frame_radio_diff = Frame(label_frame2_f1_frame3,bg=secondary_color)
frame_radio_diff.pack()

frame_radio_words = Frame(label_frame3_f1_frame3,bg=secondary_color)
frame_radio_words.pack()

var_set_diff = StringVar()
var_set_words = StringVar()
var_set_diff.set('intermediate')
var_set_words.set('medium')

radio1_diff = Radiobutton(frame_radio_diff, text = 'Easy', var = var_set_diff, value='easy',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio2_diff = Radiobutton(frame_radio_diff, text = 'Intemediate', var = var_set_diff, value='intermediate',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio3_diff = Radiobutton(frame_radio_diff, text = 'Hard', var = var_set_diff, value='hard',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio1_words = Radiobutton(frame_radio_words, text = 'Quick', var = var_set_words, value='quick',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio2_words = Radiobutton(frame_radio_words, text = 'Short', var = var_set_words, value='short',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio3_words = Radiobutton(frame_radio_words, text = 'Medium', var = var_set_words, value='medium',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
radio4_words = Radiobutton(frame_radio_words, text = 'Hard', var = var_set_words, value='hard',bg=secondary_color, fg = primary_color, activebackground=secondary_color, activeforeground=primary_color)
# radio5_words = Radiobutton(frame_radio_words, text = 'Hectic', var = var_set_words, value='hectic')

radio1_diff.grid(row=0, column=0, padx=30)
radio2_diff.grid(row=0, column=1, padx=30)
radio3_diff.grid(row=0, column=2, padx=30)

radio1_words.grid(row=0, column=0, padx=20)
radio2_words.grid(row=0, column=1, padx=20)
radio3_words.grid(row=0, column=2, padx=20)
radio4_words.grid(row=0, column=3, padx=20)
# radio5_words.grid(row=0, column=4, padx=20)

frame_f3_end = Frame(frame3, relief='sunken', bd=2)
frame_f3_end.pack(side = BOTTOM, fill='x')

lbl1_frame_f3_end = Label(frame_f3_end, text='Page 3 of 5', width=15)
lbl1_frame_f3_end.pack(side=LEFT, pady=2)

btn1_frame_f3_end = Button(frame_f3_end, text='NEXT', width=10, fg = third_color, bg = secondary_color, command=f3_close_f4_open )
btn1_frame_f3_end.pack(side=RIGHT, pady=2, padx=2)

btn1_frame_f3_end = Button(frame_f3_end, text='BACK', width=10, fg = third_color, bg = secondary_color, command=f3_close_f2_open)
btn1_frame_f3_end.pack(side=RIGHT, pady=2, padx=2)

btn2_frame_f3_end = Button(frame_f3_end, text='CLOSE', width=10, fg = third_color, bg = secondary_color, command=close )
btn2_frame_f3_end.pack(side=RIGHT, pady=2, padx=2)
# ?--------------------------frame 3 ends--------------------------

# ?--------------------------frame 4 starts--------------------------
frame4 = Frame(root, width=500, bg=secondary_color)

label_f4_01 = Label(frame4, text='Typing meter', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f4_01.pack(pady=10)

label_f4_02 = Label(frame4, text = 'Typing area', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f4_02.pack(pady=2)

f1_frame4 = Frame(frame4, bg=secondary_color)
f1_frame4.pack(fill='both', expand=True, ipadx=10, ipady=10, padx=20, pady=10)

labelframe1_frame4 = LabelFrame(f1_frame4, text='Generated String', fg = primary_color, bg=secondary_color)
labelframe1_frame4.pack(fill='x', padx=5, pady=2.5)

label_rules_f4 = Text(labelframe1_frame4, height=5, width=80, fg = third_color, bg=secondary_color)
label_rules_f4.pack(pady=2.5, padx=5, ipady=5, ipadx=5)

label_rules_f4.insert(END, 'Text to type will appear here after clicking the button..')

labelframe2_frame4 = LabelFrame(f1_frame4, text='Typing Area', fg = primary_color, bg=secondary_color)
labelframe2_frame4.pack(fill='x', padx=5, pady=2.5)

entry_rules_f4 = Text(labelframe2_frame4, width=100, height=5)
entry_rules_f4.pack(pady=5, padx=5, ipady=5, ipadx=2.5)

btn_frame4 = Button(f1_frame4, text='Click to get the text', command=generate_text, fg = primary_color, bg=secondary_color, font=('Helvetica', 10, 'bold'))
btn_frame4.pack(pady=10, ipadx=15)

lbl_frame4 = Label(f1_frame4,text='', fg = third_color, bg=secondary_color)
lbl_frame4.pack(pady=5)

frame_f4_end = Frame(frame4, relief='sunken', bd=2)
frame_f4_end.pack(side = BOTTOM, fill='x')

lbl1_frame_f4_end = Label(frame_f4_end, text='Page 4 of 5')
lbl1_frame_f4_end.pack(side=LEFT, pady=2)

btn0_frame_f4_end = Button(frame_f4_end, text='NEXT', width=10, fg = third_color, bg = secondary_color, command=f4_close_f5_open)
btn0_frame_f4_end.pack(side=RIGHT, pady=2, padx=2)

btn1_frame_f4_end = Button(frame_f4_end, text='BACK', width=10, fg = third_color, bg = secondary_color, command=f4_close_f3_open)
btn1_frame_f4_end.pack(side=RIGHT, pady=2, padx=2)

btn2_frame_f4_end = Button(frame_f4_end, text='CLOSE', width=10, fg =third_color, bg = secondary_color, command=close)
btn2_frame_f4_end.pack(side=RIGHT, pady=2, padx=2)
# ?--------------------------frame4 ends--------------------------

# ?--------------------------frame 5 starts--------------------------
frame5 = Frame(root, width=500, bg=secondary_color)

label_f5_01 = Label(frame5, text='Typing meter', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f5_01.pack(pady=10)

label_f5_02 = Label(frame5, text = 'Remarks', fg = primary_color, bg=secondary_color, font=('Helvetica', 18, 'bold'))
label_f5_02.pack(pady=2)

f1_frame5 = LabelFrame(frame5, text = 'Results', fg = primary_color, bg=secondary_color)
f1_frame5.pack(fill='both', expand=True, padx=10, pady=10, ipadx=5, ipady=5)

f2_frame5 = LabelFrame(frame5, text = 'Remarks', fg = primary_color, bg=secondary_color)
f2_frame5.pack(fill='both', expand=True, padx=10, pady=10, ipadx=5, ipady=50)

frame_f5_end = Frame(frame5, relief='sunken', bd=2)
frame_f5_end.pack(side = BOTTOM, fill='x')

lbl1_frame_f4_end = Label(frame_f5_end, text='Page 5 of 5')
lbl1_frame_f4_end.pack(side=LEFT, pady=2)

btn1_frame_f5_end = Button(frame_f5_end, text='BACK', width=10, fg = third_color, bg = secondary_color, command=f5_close_f4_open)
btn1_frame_f5_end.pack(side=RIGHT, pady=2, padx=2)

btn2_frame_f5_end = Button(frame_f5_end, text='CLOSE', width=10, fg = third_color, bg = secondary_color, command=close)
btn2_frame_f5_end.pack(side=RIGHT, pady=2, padx=2)
# ?--------------------------frame 5 ends--------------------------

# ############################CODE ENDS############################
root.mainloop()