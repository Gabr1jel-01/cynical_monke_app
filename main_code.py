import customtkinter as ctk
import tkinter as tk
from PIL import Image 
import os

ctk.set_appearance_mode("light")

# main app init
app = ctk.CTk()
app.geometry("1800x900+100+20")
app.columnconfigure(0,weight=0)
app.columnconfigure(1,weight=1)
app.columnconfigure(2,weight=0)
app.rowconfigure(0,weight=0)
app.rowconfigure(1,weight=1)
app.rowconfigure(2,weight=2)


#VARIABLES

row_counter = 1



#FUNCTIONS

def select_frame_by_name(name):
    home_button.configure(fg_color=("#01767b", "gray25") if name == "home" else "transparent")

    
    if name == "home":
        home_view_frame.grid(row=1, column=1, sticky="nsew",rowspan=2)
    else:
            home_view_frame.grid_forget()
        
            

def home_button_event():
        select_frame_by_name("home")
        
def change_appearance_mode_event(new_appearance_mode):
    ctk.set_appearance_mode(new_appearance_mode)

def add_button():
    global pop_up_window 
    pop_up_window = None
    global new_collection_entrie

    if pop_up_window is None or not pop_up_window.winfo_exists():
        pop_up_window = ctk.CTkToplevel(app,fg_color="white")
        pop_up_window.geometry("500x300")
        pop_up_window.resizable(0,0)
        pop_up_window.title("")
        pop_up_window.wm_attributes("-topmost", True)
        
        
        new_collection_frame_purple = ctk.CTkFrame(pop_up_window,fg_color="white",corner_radius=0,width=500,height=70)
        new_collection_frame_purple.place(x=0,y=0)  
        
        new_collection_label = ctk.CTkLabel(pop_up_window,text="Please enter new collection name:",
                                            font=("Times New Roman",24))
        new_collection_label.place(x=20,y=10)
        
        new_collection_entrie = ctk.CTkEntry(pop_up_window,width=300,height=40,corner_radius=0,placeholder_text="New collection name",
                                             placeholder_text_color="grey")
        new_collection_entrie.place(x=100,y=110)
        
        create_button = ctk.CTkButton(pop_up_window,text="Create ✓",fg_color="#85CC18",height=50,width=200,font=("Times New Roman",20),
                                      hover_color="#56A600",command=pop_up_create_action)
        create_button.place(x=30,y=200)
        
        create_button = ctk.CTkButton(pop_up_window,text="Cancle X",fg_color="#B51F03",height=50,width=200,font=("Times New Roman",20),
                                      hover_color="#812100")
        create_button.place(x=270,y=200)
        
        
    else:
        pass


def pop_up_create_action():
    a = new_collection_entrie.get()
    global row_counter
    
    button = ctk.CTkButton(scrollable_frame,text=a,font=("Times New Roman",24),height=80,width=200,corner_radius=0,border_width=0,
                           fg_color="#53bbaf",hover_color="#01767b",text_color="black")
    button.grid(row=1+row_counter, column=0,sticky="w")
    row_counter = row_counter + 1
    pop_up_window.destroy()
    
    

#IMAGES
app_main_picture = ctk.CTkImage(light_image=Image.open("png_pictures/colours.png"))
user_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/user.png"))
notification_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/notification.png"))
home_button_image = ctk.CTkImage(light_image=Image.open("png_pictures/home.png"))


#FRAMES
scrollable_frame = ctk.CTkScrollableFrame(app,fg_color="white",corner_radius=0,
                                          scrollbar_button_color="white")
scrollable_frame.grid(row=1,column=0,sticky="ns",rowspan=2)

home_view_frame = ctk.CTkFrame(app,corner_radius=0)
home_view_frame.columnconfigure(2, weight=1)
home_view_frame.rowconfigure(2, weight=1)

line_under_search_bar_frame = ctk.CTkFrame(app,fg_color="#4f2d71",height=5)
line_under_search_bar_frame.grid(row=1,column=1,sticky="new")

#LABELS
label1 = ctk.CTkLabel(app,corner_radius=0,image=app_main_picture,text="")
label1.grid(row=0,column=0,sticky="")


user_png_image_label = ctk.CTkLabel(app, image=user_png_image,text="",fg_color="white")
user_png_image_label.grid(row=0,column=1,sticky="e",padx=110,ipadx=5,ipady=5)

#OPTION MENUS
user_drop_down = ctk.CTkOptionMenu(app,button_color="white",fg_color="white",dynamic_resizing=False,corner_radius=20,button_hover_color="white",
                                   text_color="black",values=["User","Options"],font=("Times New Roman",18),dropdown_font=("Times New Roman",18))
user_drop_down.grid(row=0,column=1,sticky="e",padx=80,ipadx=5,ipady=5)

#appearance_mode_menu = ctk.CTkOptionMenu(scrollable_frame,values=["Light", "Dark", "System"],command=change_appearance_mode_event)
#appearance_mode_menu.grid(row=0,column=0,sticky="s")

#ENTRIES
search_entry = ctk.CTkEntry(app,width=400,height=50,corner_radius=50,fg_color="white",text_color="black",placeholder_text="Search",
                            placeholder_text_color="grey",border_color="#905d9e",font=("Times New Roman",24))
search_entry.grid(row=0,column=1)


#BUTTONS

plus_button = ctk.CTkButton(app,text="+",font=("Times New Roman",36),corner_radius=40,width=1,height=40,command=add_button,
                            fg_color="#905d9e",hover_color="#4f2d71")
plus_button.grid(row=0,column=1,sticky="w",padx=20,pady=20,ipadx=10,ipady=10)


notification_button = ctk.CTkButton(app,width=15,fg_color="#905d9e",hover_color="#4f2d71",
                                    image=notification_png_image,text="",corner_radius=50)
notification_button.grid(row=0,column=1,sticky="e",padx=300,ipadx=10,ipady=10)

home_button = ctk.CTkButton(scrollable_frame,image=home_button_image,fg_color="#53bbaf",hover_color="#01767b",border_color="black",border_width=0,
                            text="Home",font=("Times New Roman",24),text_color="black",height=80,width=200,corner_radius=0,command=home_button_event)
home_button.grid(row=1,column=0,sticky="w")




app.mainloop()