 # -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:08:53 2019

@author: gy19rf(Richard Frimpong) Student ID 201377095
"""
"""
Module name: Programming for Geographical Information Analysis (Core skills)
Module code: GEOG5990
"""

"""
This practical allows the use of a Graphic User Interface (Gui)to
create an Agent Based Model by importing some data from the website.
This gives way for moving, eating, sharing the agents to have interaction
 with the environment. This models allows easy plotting of agents on the 
environment, calculate the distance between agents and gets the agents animated as well
"""


"""Note: The import operator function is very useful in the building agents to interact  
with the environment because it allows useful data files to be imported to the model

"""
"""
 Import commframework, but call it agentframework
"""
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import commframework as agentframework
import random 
import matplotlib.pyplot
import csv
import matplotlib.animation
import requests
import bs4

# Set the seed of random so that the results is always the same
random.seed(1) 
"""
print first step
Assigning agents parameters
""" 
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []
environment = []




"""
Print the second step:
importing environment data from the website
"""
f = open('in.txt')
data = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in data:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()


"""
Print the third step:       
import x,y data from website
"""
 # Making the agents.
agents = []
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, agents, environment,y, x))




"""
Print the fourth step:
Reading the csv file in a 2D list 
"""
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on

    
    """
    Print the fifth step:         
     Moving the agents, allowing the agents to eat  and share the available resources 
    with neighbours within the environment
    """
         
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share(20)

    """
    Print the sixth step:
    Plotting the agents on the environment
    """     
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, 150)
    matplotlib.pyplot.ylim(0, 150)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
 
 
         
#    if random.random() < 0.1:
#        carry_on = False
#        print("stopping condition")
    
    #making an agent class
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
           

    """ Print the seventh step:  
    Calculating the distance between the agents
    """   
   
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

    """
  Print the eighth step:
  Getting the model animated
    """
   
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, frames=num_of_iterations, repeat=False)

"""
Print the nineth step:
creating a run function for tkinter Run model label
"""
def run():
   animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
   canvas.draw()

"""
Print the tenth step:
creating tkinter window, canvas, menu bar, Run model label, and link the Run model label with the run function
"""
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()

