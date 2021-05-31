import pygame
import sys



bgcolor='#001219'
barcolor="#ee9b00"

def main():

    pygame.init()
    display=pygame.display.set_mode((1500,800))
    menu_state="sorting algo"
    sub_menu_state = None
    msx=50
    msy=150
    algo="Bubble Sort"
    size=50
    speed=1

    def display_text(text,x,y,size):
        font = pygame.font.SysFont("Times",size)
        rendered_text = font.render(text,True,barcolor,bgcolor)
        text_rect = rendered_text.get_rect()
        text_rect.topleft=(x,y)
        return (rendered_text,text_rect)


    while True:
        display.fill(bgcolor)
        pygame.display.set_caption(f"Press \"SPACE\" to select        Press \"ENTER\" to start      Press \" ARROW KEY\" to navigate")
        rt,tr=display_text("ALGORITHM VISUALIZER",400,30,60)
        display.blit(rt,tr)
        rt, tr = display_text("SORTING ALGORITHM", 150, 150, 40)
        display.blit(rt, tr)
        rt, tr = display_text("ARRAY SIZE", 150, 250, 40)
        display.blit(rt, tr)
        rt, tr = display_text("SPEED", 150, 350, 40)
        display.blit(rt, tr)
        rt, tr = display_text(f"Algorithm:  {algo}", 50, 600, 40)
        display.blit(rt, tr)
        rt, tr = display_text(f"Size:  {size} elements", 550, 600, 40)
        display.blit(rt, tr)
        rt, tr = display_text(f"Speed:  {speed}X", 1000, 600, 40)
        display.blit(rt, tr)

        if menu_state=="sorting algo":
            msy=150

            rt, tr = display_text(">>>",msx,msy,40)
            display.blit(rt, tr)

            smsx=800
            smsy=150
            rt, tr = display_text("BUBBLE SORT", 850, 150, 30)
            display.blit(rt, tr)
            rt, tr = display_text("SELECTION SORT", 850, 200, 30)
            display.blit(rt, tr)
            rt, tr = display_text("INSERTION SORT", 850, 250, 30)
            display.blit(rt, tr)
            rt, tr = display_text("MERGE SORT", 850, 300, 30)
            display.blit(rt, tr)
            rt, tr = display_text("QUICK SORT", 850, 350, 30)
            display.blit(rt, tr)
            rt, tr = display_text("HEAP SORT", 850, 400, 30)
            display.blit(rt, tr)
            if sub_menu_state=="bubble sort":
                smsy=150
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="selection sort":
                smsy=200
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="insertion sort":
                smsy=250
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="merge sort":
                smsy=300
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="quick sort":
                smsy=350
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="heap sort":
                smsy=400
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)



        elif menu_state=="array size":
            msy=250
            rt, tr = display_text(">>>", msx, msy, 40)
            display.blit(rt, tr)
            smsx = 800
            smsy = 150
            rt, tr = display_text("50 ELEMENTS", 850, 150, 30)
            display.blit(rt, tr)
            rt, tr = display_text("100 ELEMENTS", 850, 200, 30)
            display.blit(rt, tr)
            rt, tr = display_text("200 ELEMENTS", 850, 250, 30)
            display.blit(rt, tr)
            rt, tr = display_text("250 ELEMENTS", 850, 300, 30)
            display.blit(rt, tr)
            rt, tr = display_text("400 ELEMENTS", 850, 350, 30)
            display.blit(rt, tr)
            if sub_menu_state=="50":
                smsy=150
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="100":
                smsy=200
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="200":
                smsy=250
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="250":
                smsy=300
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="400":
                smsy=350
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)


        elif menu_state=="speed":
            msy=350
            rt, tr = display_text(">>>", msx, msy, 40)
            display.blit(rt, tr)
            smsx = 800
            smsy = 150
            rt, tr = display_text("1X", 850, 150, 30)
            display.blit(rt, tr)
            rt, tr = display_text("2X", 850, 200, 30)
            display.blit(rt, tr)
            rt, tr = display_text("3X", 850, 250, 30)
            display.blit(rt, tr)
            rt, tr = display_text("4X", 850, 300, 30)
            display.blit(rt, tr)
            rt, tr = display_text("5X", 850, 350, 30)
            display.blit(rt, tr)
            if sub_menu_state=="1":
                smsy=150
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="2":
                smsy=200
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="3":
                smsy=250
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="4":
                smsy=300
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)
            elif sub_menu_state=="5":
                smsy=350
                rt, tr = display_text(">>>", smsx, smsy, 30)
                display.blit(rt, tr)



        # *********   Event handling   ***********



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit();sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    if menu_state == "sorting algo":
                        if  sub_menu_state==None:
                            menu_state="array size"
                        elif sub_menu_state=="bubble sort":
                            sub_menu_state="selection sort"
                        elif sub_menu_state == "selection sort":
                            sub_menu_state = "insertion sort"
                        elif sub_menu_state == "insertion sort":
                            sub_menu_state = "merge sort"
                        elif sub_menu_state == "merge sort":
                            sub_menu_state = "quick sort"
                        elif sub_menu_state == "quick sort":
                            sub_menu_state = "heap sort"
                        elif sub_menu_state == "heap sort":
                            sub_menu_state = "bubble sort"

                    elif menu_state == "array size":
                        if sub_menu_state == None:
                            menu_state="speed"
                        elif sub_menu_state == "50":
                            sub_menu_state = "100"
                        elif sub_menu_state == "100":
                            sub_menu_state = "200"
                        elif sub_menu_state == "200":
                            sub_menu_state = "250"
                        elif sub_menu_state == "250":
                            sub_menu_state = "400"
                        elif sub_menu_state == "400":
                            sub_menu_state = "50"


                    elif menu_state == "speed":
                        if sub_menu_state == None:
                            menu_state="sorting algo"
                        elif sub_menu_state == "1":
                            sub_menu_state = "2"
                        elif sub_menu_state == "2":
                            sub_menu_state = "3"
                        elif sub_menu_state == "3":
                            sub_menu_state = "4"
                        elif sub_menu_state == "4":
                            sub_menu_state = "5"
                        elif sub_menu_state == "5":
                            sub_menu_state = "1"

                if event.key==pygame.K_UP:
                    if menu_state == "sorting algo":
                        if sub_menu_state == None:
                            menu_state="speed"
                        elif sub_menu_state=="bubble sort":
                            sub_menu_state="heap sort"
                        elif sub_menu_state == "selection sort":
                            sub_menu_state = "bubble sort"
                        elif sub_menu_state == "insertion sort":
                            sub_menu_state = "selection sort"
                        elif sub_menu_state == "merge sort":
                            sub_menu_state = "insertion sort"
                        elif sub_menu_state == "quick sort":
                            sub_menu_state = "merge sort"
                        elif sub_menu_state == "heap sort":
                            sub_menu_state = "quick sort"

                    elif menu_state == "array size":
                        if sub_menu_state == None:
                            menu_state="sorting algo"
                        elif sub_menu_state == "50":
                            sub_menu_state = "400"
                        elif sub_menu_state == "100":
                            sub_menu_state = "50"
                        elif sub_menu_state == "200":
                            sub_menu_state = "100"
                        elif sub_menu_state == "250":
                            sub_menu_state = "200"
                        elif sub_menu_state == "400":
                            sub_menu_state = "250"

                    elif menu_state == "speed":
                        if sub_menu_state == None:
                            menu_state="array size"
                        elif sub_menu_state == "1":
                            sub_menu_state = "5"
                        elif sub_menu_state == "2":
                            sub_menu_state = "1"
                        elif sub_menu_state == "3":
                            sub_menu_state = "2"
                        elif sub_menu_state == "4":
                            sub_menu_state = "3"
                        elif sub_menu_state == "5":
                            sub_menu_state = "4"

                if event.key==pygame.K_SPACE:
                    if menu_state=="sorting algo" and sub_menu_state==None:
                        sub_menu_state="bubble sort"
                    elif menu_state=="sorting algo" and sub_menu_state=="bubble sort":
                        algo = "Bubble Sort"
                        sub_menu_state=None
                    elif menu_state == "sorting algo" and sub_menu_state == "selection sort":
                        algo = "Selection Sort"
                        sub_menu_state = None
                    elif menu_state == "sorting algo" and sub_menu_state == "insertion sort":
                        algo = "Insertion Sort"
                        sub_menu_state=None
                    elif menu_state == "sorting algo" and sub_menu_state == "merge sort":
                        algo = "Merge Sort"
                        sub_menu_state=None
                    elif menu_state == "sorting algo" and sub_menu_state == "quick sort":
                        algo = "Quick Sort"
                        sub_menu_state=None
                    elif menu_state == "sorting algo" and sub_menu_state == "heap sort":
                        algo = "Heap Sort"
                        sub_menu_state=None

                    elif menu_state == "array size" and sub_menu_state == None:
                        sub_menu_state="50"
                    elif menu_state == "array size" and sub_menu_state == "50":
                        size = 50
                        sub_menu_state=None
                    elif menu_state == "array size" and sub_menu_state == "100":
                        size = 100
                        sub_menu_state=None
                    elif menu_state == "array size" and sub_menu_state == "200":
                        size = 200
                        sub_menu_state=None
                    elif menu_state == "array size" and sub_menu_state == "250":
                        size = 250
                        sub_menu_state=None
                    elif menu_state == "array size" and sub_menu_state == "400":
                        size = 400
                        sub_menu_state=None

                    elif menu_state == "speed" and sub_menu_state == None:
                        sub_menu_state="1"
                    elif menu_state == "speed" and sub_menu_state == "1":
                        speed=1
                        sub_menu_state=None
                    elif menu_state == "speed" and sub_menu_state == "2":
                        speed = 2
                        sub_menu_state=None
                    elif menu_state == "speed" and sub_menu_state == "3":
                        speed = 3
                        sub_menu_state=None
                    elif menu_state == "speed" and sub_menu_state == "4":
                        speed = 4
                        sub_menu_state=None
                    elif menu_state == "speed" and sub_menu_state == "5":
                        speed = 5
                        sub_menu_state=None

                if event.key==pygame.K_RETURN:
                    import sorting_visualizer
                    sorting_visualizer.main(algo,size,speed)


        pygame.display.update()


if __name__ == "__main__":
    main()