import time, random, tkinter, colorsys, queue, _thread

from creative import sound
from tkinter import *
from tkinter import Tk, messagebox
from math import floor
import winsound

#SOUND VISUALISER==========================================================================================
"""IT WORK AS A SIDE PART OF THIS CODE """

#VISUALISER WINDOW=========================================================================================
def DrawList(data, current_selection_1 = -1, current_selection_2 = -1):
    width = w / len(data)
    height = 0
    x, y = 0, h
    
    selection_colour1 = "orange"
    selection_colour2 = "lime"
        
    for e in range(0, len(data)):
        if not COLOUR_MODE: colour = "yellow"
        else:
            depth = 256 - floor((256 / h) * data[e])
            (r, g, b) = colorsys.hsv_to_rgb(float(depth) / 256, 1.0, 1.0)
            R, G, B = int(255 * r), int(255 * g), int(255 * b)
            colour = '#%02x%02x%02x' % (R, G, B)
        if e == current_selection_1 or e == current_selection_2: colour = selection_colour1
        if e == current_selection_2 :colour = selection_colour2
        if not DISPLAY_MODE_DOTS:
            canvas.create_rectangle(x, y , x + width, y - data[e], fill=colour)
        else:
            canvas.create_oval(x, y - data[e], x + width, y - data[e] + width, fill=colour)
        x += width

def ToggleSoundMode():
    global sounds
    sorting=True
    if (sounds == True):
        sounds = False
    else:
        sounds = True


def ToggleColourMode():
    global COLOUR_MODE
    sorting=True
    if (COLOUR_MODE == True):
        COLOUR_MODE = False
    else:
        COLOUR_MODE = True

def ToggleDotMode():
    global DISPLAY_MODE_DOTS
    sorting=True
    if (DISPLAY_MODE_DOTS == True):
        DISPLAY_MODE_DOTS = False
    else:
        DISPLAY_MODE_DOTS = True


def EndSort():
    global sorting, queue
    with queue.mutex: queue.queue.clear()
    sorting = False
    SoundMode=False
    ResetList(ElementSlider.get())
    print("Ending sort...")
    messagebox.showinfo(title="Greetings", message="Sort ended!")

def ResetList(value):
    global lst
    if (not sorting):
        lst = random.sample(range(0,h), int(value))


def UpdateDelay(value):
    global ANIMATION_DELAY
    ANIMATION_DELAY = int(value)

def partition(arr,l,h):
    global queue
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l , h): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            if not sounds:
                queue.put(lambda: DrawList(arr, i, j), sound(arr[i]))
            else:
                queue.put(lambda: DrawList(arr, i, j))
            
    arr[i+1],arr[h] = arr[h],arr[i+1]
    
    queue.put(lambda: DrawList(arr, i, j))
    time.sleep(ANIMATION_DELAY/1000)
    
    return (i+1) 

#SORTING ALGORITHMS========================================================================================
def quickSort(arr):
    global queue
    last = time.perf_counter()

    h = len(arr) - 1
    l = 0

    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # Keep popping from stack while is not empty 
    while top >= 0:

        if not sorting:  print("Ending sort..."); return
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p+1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 
         
    print("Sorted with Quick Sort in", time.perf_counter() - last, "seconds.")

    with queue.mutex: queue.queue.clear()
    queue.put(lambda: EndSort())
    return

def mergeSort(data):
    global queue
    last = time.perf_counter()
    n = len(data)
    step = 1
    while (step < n):
        i = 0
        while (i < n - step):
            a = data[i:i + step]
            b = data[i + step:min(i + 2 * step, n)]
            for k in range(i, min(i + 2 * step, n)):
                if (len(a) > 0 and len(b) > 0):
                    if (a[0] > b[0]):
                        data[k] = b[0]
                        b.remove(b[0])
                        #sound()
                    else:
                        data[k] = a[0]
                        a.remove(a[0])
                else:
                    for p in range(k, min(i + 2 * step, n)):
                        if (len(b) > 0):
                            data[p] = b[0]
                            b.remove(b[0])
                    for j in range(k, min(i + 2 * step, n)):
                        if (len(a) > 0):
                            data[j] = a[0]
                            a.remove(a[0])

                if not sounds:
                    queue.put(lambda: DrawList(data, i, k), sound(data[k]))
                else:
                    queue.put(lambda: DrawList(data, i, k))
                time.sleep(ANIMATION_DELAY/1000)
                if not sorting:  print("Ending sort..."); return
            i = i + 2 * step
        step = step * 2
    print("Sorted with Merge Sort in ", time.perf_counter() - last, "seconds.")
    with queue.mutex: queue.queue.clear()
    queue.put(lambda: EndSort())
    return
def bubbleSort(data):
    global queue
    last = time.perf_counter()
    for e in range(len(data) - 1, 0, -1):
        for i in range(1, len(data)):
            if data[i - 1] > data[i]:
                data[i], data[i - 1] = data[i - 1], data[i]
                if not sounds:
                    queue.put(lambda: DrawList(data, e, i), sound(data[i-1]))
                else:
                    queue.put(lambda: DrawList(data, e, i))
                time.sleep(ANIMATION_DELAY / 1000)
                if not sorting:  print("Ending sort..."); return
    	
    print("Sorted with Bubble Sort in", time.perf_counter() - last, "seconds.")

    with queue.mutex: queue.queue.clear()
    queue.put(lambda: EndSort())
    return 

def selectionSort(data):
    global queue
    last = time.perf_counter()
    for e in range(len(data)):
        smallest = e
        for j in range(e + 1, len(data)):
            if data[j] < data[smallest]: smallest = j;

            if not sounds:
                queue.put(lambda: DrawList(data, e, j), sound(data[j]))
            else:
                queue.put(lambda: DrawList(data, e, j))
            time.sleep(ANIMATION_DELAY / 1000)
            if not sorting:  print("Ending sort..."); return
        temp = data[e]
        data[e] = data[smallest]
        data[smallest] = temp
    print("Sorted with Selection Sort in ", time.perf_counter() - last, "seconds.")

    with queue.mutex: queue.queue.clear()
    queue.put(lambda: EndSort())
    return

def insertionSort(data):
    global queue
    last = time.perf_counter()
    for e in range(1, len(data)):
        index = data[e]
        j = e
        while j > 0 and data[j-1] > index:
            data[j] = data[j-1]
            j -= 1
            if not sounds:
                queue.put(lambda: DrawList(data, e, j), sound(data[j]))
            else:
                queue.put(lambda: DrawList(data, e, j))
            time.sleep(ANIMATION_DELAY / 1000)
            if not sorting:  print("Ending sort..."); return
        data[j] = index
    print("Sorted with Insertion Sort in ", time.perf_counter() - last, "seconds.")
    
    with queue.mutex: queue.queue.clear()
    queue.put(lambda: EndSort())
    return



#MAIN WINDOW===============================================================================================
root = Tk()
root.title("SORTING SIMPLIFIER")
#root.attributes('-fullscreen',True)
root.geometry("1531x900-1+0")
root.config(background = 'black')

#CONSTANTS=================================================================================================
w=1520
h=800
minElements = 10
maxElements = h
lst = random.sample(range(0, h - 10), minElements)
DISPLAY_MODE_DOTS = False
COLOUR_MODE = False
sounds = True
queue = queue.Queue()
ANIMATION_DELAY = 1
sorting = False

#COPONENTS OF THE WINDOW===================================================================================

#TOOLBAR========================================

toolbar = tkinter.Frame(root)

ElementSlider = tkinter.Scale(toolbar, from_=minElements, to=maxElements, orient="horizontal", length=250, command = ResetList)
ElementSlider.set(100)
ElementSlider.pack(side="right")

Label1 = tkinter.Label(toolbar, text="Element Count:")
Label1.pack(side="right")

DelaySlider = tkinter.Scale(toolbar, from_=1, to=1000, orient="horizontal", length=250, command = UpdateDelay)
DelaySlider.pack(side="right")

Label2 = tkinter.Label(toolbar, text="Animation Delay (ms):")
Label2.pack(side="right")

ColourMode = tkinter.Button(toolbar, text="End Sort", command = EndSort)
ColourMode.pack(side="left")

ColourMode = tkinter.Button(toolbar, text="Toggle Colour Mode", command = ToggleColourMode)
ColourMode.pack(side="right")

SoundMode = tkinter.Button(toolbar, text="Toggle Sound Mode", command = ToggleSoundMode)
SoundMode.pack(side="right")

DotMode = tkinter.Button(toolbar, text="Toggle Dot Mode", command = ToggleDotMode)
DotMode.pack(side="right")

toolbar.pack(side="bottom", fill="x")


menu_bar=Menu(root)
fileMenu=Menu(menu_bar,tearoff=0)
fileMenu.add_command(label="BUBBLE SORT",command=lambda: BeginSort("BUBBLE"))
fileMenu.add_command(label="MERGE SORT",command=lambda: BeginSort("MERGE"))
fileMenu.add_command(label="SELECTION SORT",command=lambda: BeginSort("SELECTION"))
fileMenu.add_command(label="INSERTION SORT",command=lambda: BeginSort("INSERTION"))
fileMenu.add_command(label="QUICK SORT",command=lambda: BeginSort("QUICK"))
menu_bar.add_cascade(label="SORTING TECHNIQUES",menu=fileMenu)
menu_bar.add_cascade(label="QUIT",command = lambda: root.destroy())
root.config(menu=menu_bar)



#ALGO VISUALISER AREA
canvas = tkinter.Canvas(root, bg="lime", height=h, width=w,border = 0)
canvas.pack(fill = "both",)



#SOMETHING UNUSUAL==============================
def BeginSort(sort):
    global sorting, lst, queue
    with queue.mutex: queue.queue.clear()
    if (not sorting):
        if (sort == "BUBBLE"):
            _thread.start_new_thread(bubbleSort, (lst, ))
        if (sort == "MERGE"):
            _thread.start_new_thread(mergeSort, (lst, ))
        if (sort == "SELECTION"):
            _thread.start_new_thread(selectionSort, (lst, ))
        if (sort == "INSERTION"):
            _thread.start_new_thread(insertionSort, (lst, ))
        if (sort == "QUICK"):
            _thread.start_new_thread(quickSort, (lst, ))
        if (sort == "BOGO"):
            _thread.start_new_thread(bogoSort, (lst, ))
        sorting = True

while True:
    root.update()
    root.update_idletasks()
    canvas.delete("all")
    if (sorting):
        function = queue.get()
        function()
    else:
        DrawList(lst)
