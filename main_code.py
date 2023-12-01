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

#212121 dark grey
#3d3d3d middle grey
#aaaaaa light grey


#181818 dark black


#ffffff white

#region FUNCTIONS

def select_frame_by_name(name):
    add_collection_button.configure(fg_color=("#01767b", "gray25") if name == "home" else "transparent")

    
    if name == "":
        home_view_frame.grid(row=1, column=1, sticky="nsew",rowspan=2)
    else:
            home_view_frame.grid_forget()
        
            

def home_button_event():
        select_frame_by_name("home")
        

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
                                            font=("Roboto",24))
        new_collection_label.place(x=20,y=10)
        
        new_collection_entrie = ctk.CTkEntry(pop_up_window,width=300,height=40,corner_radius=0,placeholder_text="New collection name",
                                             placeholder_text_color="grey")
        new_collection_entrie.place(x=100,y=110)
        
        create_button = ctk.CTkButton(pop_up_window,text="Create ✓",fg_color="#85CC18",height=50,width=200,font=("Roboto",20),
                                      hover_color="#56A600",command=pop_up_create_action)
        create_button.place(x=30,y=200)
        
        create_button = ctk.CTkButton(pop_up_window,text="Cancle X",fg_color="#B51F03",height=50,width=200,font=("Roboto",20),
                                      hover_color="#812100")
        create_button.place(x=270,y=200)
        
        
    else:
        pass


def pop_up_create_action():
    a = new_collection_entrie.get()
    global row_counter
    
    button = ctk.CTkButton(scrollable_frame,text=a,font=("Roboto",24),height=80,width=200,corner_radius=0,border_width=0,
                           fg_color="#53bbaf",hover_color="#01767b",text_color="black")
    button.grid(row=1+row_counter, column=0,sticky="w")
    row_counter = row_counter + 1
    pop_up_window.destroy()
    
#endregion



#region IMAGES

user_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/user.png"))
notification_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/notification.png"))
delete_collection_button = ctk.CTkImage(light_image=Image.open("png_pictures/trashcan_image.png"))

#endregion



#region FRAMES
main_app_frame = ctk.CTkFrame(app,fg_color="#181818").grid(sticky="nsew",row=0,column=0,rowspan=3,columnspan=2)


scrollable_frame = ctk.CTkScrollableFrame(main_app_frame,fg_color="#181818",corner_radius=0,
                                          scrollbar_button_color="#181818")
scrollable_frame.grid(row=2,column=0,sticky="ns",rowspan=2)

home_view_frame = ctk.CTkFrame(main_app_frame,corner_radius=0,fg_color="#181818")
home_view_frame.columnconfigure(2, weight=1)
home_view_frame.rowconfigure(2, weight=1)

main_frame_for_loaded_pictures = ctk.CTkFrame(main_app_frame,fg_color="#181818",border_color="#181818",corner_radius=0)
main_frame_for_loaded_pictures.grid(row=1,column=1,rowspan=2,columnspan=2,sticky="nsew")

#endregion



#region OPTION MENUS
user_drop_down = ctk.CTkOptionMenu(main_app_frame,button_color="#181818",fg_color="#181818",bg_color="#181818",
                                   dynamic_resizing=False,corner_radius=20,button_hover_color="#3d3d3d",
                                   text_color="white",values=["User","Options"],font=("Roboto",18),dropdown_font=("Roboto",18))
user_drop_down.grid(row=0,column=1,sticky="e",padx=80,pady=10)
#endregion



#region LABELS
user_png_image_label = ctk.CTkLabel(main_app_frame, image=user_png_image,text="",fg_color="#181818")
user_png_image_label.grid(row=0,column=1,sticky="e",padx=110)

a_project_label = ctk.CTkLabel(main_app_frame,text="AProject",font=("Roboto",32),text_color="white",fg_color="#181818")
a_project_label.grid(row=0,column=0,sticky="nsew")

#endregion



#region ENTRIES
search_entry = ctk.CTkEntry(main_app_frame,width=400,height=50,corner_radius=50,fg_color="#181818",text_color="white",placeholder_text="Search",
                            placeholder_text_color="white",border_color="#3d3d3d",font=("Roboto",24),bg_color="#181818")
search_entry.grid(row=1,column=1,pady=30,sticky="n")

#endregion



#region BUTTONS

notification_button = ctk.CTkButton(app,width=15,fg_color="#181818",hover_color="#3d3d3d",
                                    image=notification_png_image,text="",corner_radius=50,bg_color="#181818")
notification_button.grid(row=0,column=1,sticky="e",padx=220,ipady=10,pady=10)


add_collection_button = ctk.CTkButton(main_app_frame,fg_color="#181818",hover_color="#3d3d3d",border_color="#181818",
                                      border_width=0,text="+Collection",font=("Roboto",28),text_color="white",
                                      height=80,width=200,corner_radius=0,command=home_button_event,anchor="w")
add_collection_button.grid(row=1,column=0,sticky="w")


delete_collection_button = ctk.CTkButton(main_app_frame,image=delete_collection_button,text="",height=80,width=30,
                                         fg_color="#181818",hover_color="#3d3d3d",bg_color="#181818")
delete_collection_button.grid(row=1,column=0,sticky="e")


collections_button = ctk.CTkButton(main_app_frame,font=("Roboto",32),text="Collections",fg_color="#181818",
                                   hover_color="#3d3d3d",corner_radius=50,bg_color="#181818")
collections_button.grid(row=0,column=1,padx=150,sticky="w")


import_button = ctk.CTkButton(main_app_frame,font=("Roboto",32),text="Import",fg_color="#181818",
                              hover_color="#3d3d3d",corner_radius=50,bg_color="#181818")
import_button.grid(row=0,column=1,sticky="w",padx=480)


usb_button = ctk.CTkButton(main_app_frame,font=("Roboto",32),text="USB",fg_color="#181818",
                           hover_color="#3d3d3d",corner_radius=50,bg_color="#181818")
usb_button.grid(row=0,column=1,sticky="e",padx=690)


settings_button = ctk.CTkButton(main_app_frame,font=("Roboto",32),text="Settings",fg_color="#181818",
                                hover_color="#3d3d3d",corner_radius=50,bg_color="#181818")
settings_button.grid(row=0,column=1,sticky="e",padx=400)


#endregion



app.mainloop()