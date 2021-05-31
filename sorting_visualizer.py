import pygame
import sorting_algorithm
import sys
import time
import bubbleSort
import heapSort
import insertionSort
import mergeSort
import quickSort
import selectionSort


pygame.init()
dimensions = (1500, 800)
margin=50
margin2=200
pause=True
display=pygame.display.set_mode((dimensions[0],dimensions[1]))
pivot_list=[]
run=False
bgcolor='#001219'
barcolor="#ee9b00"
color1="#ae2012"
color2="#0a9396"
color3="#d3d3d3"
color4="#e5383b"

def display_text(text, x, y, size, fcolor=(13, 238, 193), bcolor=(3, 22, 44)):
    font = pygame.font.Font("freesansbold.ttf", size)
    rendered_text = font.render(text, True, fcolor, bcolor)
    text_rect = rendered_text.get_rect()
    text_rect.topleft = (x, y)
    return (rendered_text, text_rect)


def check_event():
        global pause
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    run=True
                    return run

                if event.key==pygame.K_RETURN:
                    import menu
                    menu.main()

                if event.key==pygame.K_s:

                    pause=True
                    keep_open()

                if event.key==pygame.K_p:
                    pause=False





def display_array(algorithm,display=display):
    display.fill(bgcolor)
    if(algorithm.name!="Insertion Sort" and algorithm.name!="Merge Sort" ):
        margin3=margin2
    else:
        margin3=margin
    k =dimensions[0] / len(algorithm.array)
    for i in range(len(algorithm.array)):
        display.fill(barcolor, rect=(i * k,(max(algorithm.array)/2)+margin3-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))
        # display.fill(barcolor,rect=(100,600,20,20))
    pygame.display.update()

    while True:
        run=check_event()
        if(run==True):
            algorithm.run()
            break










def update_bubblesort(algorithm,swap1=None,swap2=None,parse=None,display=display):
    display.fill(bgcolor)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time()-algorithm.start_time}")
    k=dimensions[0]/len(algorithm.array)
    for i in range(len(algorithm.array)):

        colour=barcolor
        if algorithm.array[i]==swap1:
            colour = color1
        elif algorithm.array[i]==swap2:
            colour=color2

        if i>=(len(algorithm.array)-parse):
            colour=color3


        display.fill(colour,rect=(i*k,(max(algorithm.array)/2)+margin2-algorithm.array[i]/2,int(k/2),algorithm.array[i]/2))

    check_event()
    pygame.display.update()

def update_selectionsort(algorithm,smallest=None,cmp=None,parse=None,display=display):
    display.fill(bgcolor)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time() - algorithm.start_time}")
    k=dimensions[0]/len(algorithm.array)

    for i in range(len(algorithm.array)):
        colour = barcolor
        if algorithm.array[i]==smallest:
            colour=color1
        elif algorithm.array[i]==cmp:
            colour=color2
        if i<parse:
            colour=color3
        display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin2-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))
    check_event()
    pygame.display.update()

def update_insertionsort(algorithm,pos=None,j=None,temp=None,display=display):
    display.fill(bgcolor)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time() - algorithm.start_time}")
    k=dimensions[0]/len(algorithm.array)

    for i in range(len(algorithm.array)):
        colour=barcolor
        if i <= pos:
            colour=color3
        if i == j:
            colour=color2
        if j != None:
            if i==(j+1):
                colour=bgcolor
                display.fill(color1, rect=(i * k,(max(algorithm.array)/2)+margin+20, int(k / 2), temp/2))


        display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))
    check_event()
    pygame.display.update()

def update_mergesort(algorithm,cmp1,cmp2,start,mid,end,temp,display=display):
    display.fill(bgcolor)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time() - algorithm.start_time}")
    k=dimensions[0]/len(algorithm.array)
    if start!=None and end!=None and mid!=None:
        for i in range(len(algorithm.array)):
            colour=barcolor
            if start<= i <=mid:
                colour=color1
            if (mid+1)<= i <= end:
                colour=color2
            if i == cmp1 or i == cmp2:
                colour=color4
            if algorithm.array[i] in temp:
                continue

            display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))

        for i in range(len(temp)):
            colour=(0,255,0)
            display.fill(colour, rect=((start*k)+(i * k),((max(algorithm.array)/2)+margin)+((max(algorithm.array)/2)+20-temp[i]/2) , int(k / 2), temp[i]/2))
    else:
        for i in range(len(algorithm.array)):
            colour=color3
            display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))


    check_event()
    pygame.display.update()


def update_quicksort(algorithm,pos=None,j=None,start=None,end=None,pivot=None,display=display):

    display.fill(bgcolor)
    k = dimensions[0]/len(algorithm.array)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time() - algorithm.start_time}")
    global pivot_list
    if(start==0 and end==len(algorithm.array)-1):
        pivot_list=[]

    pivot_list.append(pivot)

    for i in range(len(algorithm.array)):
        colour=barcolor
        if i in range(start,end+1):
            colour=color4
        if i==pos:
            colour=color1
        if i==j:
            colour=color2
        if i == start:
            colour=(255,255,0)
        if algorithm.array[i] in pivot_list:
            colour=color3

        display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin2-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))
    check_event()
    pygame.display.update()



def update_heapsort(algorithm,parent,r_child,l_child,parse,display=display):
    display.fill(bgcolor)
    pygame.display.set_caption(f"Algorithm: {algorithm.name}      Time: {time.time() - algorithm.start_time}")
    k = dimensions[0] / len(algorithm.array)
    for i in range(len(algorithm.array)):
        colour=barcolor
        if i==parent:
            colour=color1
        if i==r_child:
            colour=color2
        if i==l_child:
            colour=(255,165,0)
        if i>(len(algorithm.array)-1)-parse:
            colour=color3

        display.fill(colour, rect=(i * k, (max(algorithm.array)/2)+margin2-algorithm.array[i]/2, int(k / 2), algorithm.array[i]/2))
    check_event()
    pygame.display.update()





def keep_open():
    while True:
        check_event()
        if pause == False:
            break
        pygame.display.update()


def main(algo,size,speed):
    global display

    algorithm=None
    if algo == "Bubble Sort":
        bubbleSort.main()
        algorithm=sorting_algorithm.BubbleSort(size,speed)
    elif algo== "Selection Sort":
        selectionSort.main()
        algorithm=sorting_algorithm.SelectionSort(size,speed)
    elif algo== "Insertion Sort":
        insertionSort.main()
        algorithm=sorting_algorithm.InsertionSort(size,speed)
    elif algo== "Merge Sort":
        mergeSort.main()
        algorithm=sorting_algorithm.MergeSort(size,speed)
    elif algo== "Quick Sort":
        quickSort.main()
        algorithm=sorting_algorithm.QuickSort(size,speed)
    elif algo== "Heap Sort":
        heapSort.main()
        algorithm=sorting_algorithm.HeapSort(size,speed)

    print(algorithm.array)
    display_array(algorithm)
    print(algorithm.array)
    keep_open()

if __name__ == "__main__":
    main()