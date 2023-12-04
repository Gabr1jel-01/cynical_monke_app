import customtkinter as ctk
import tkinter as tk
from PIL import Image 
import os
import json


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

    
#endregion
def click():
    if add_collection_button.cget("state") == "normal":
        add_collection_button.configure(state="disabled")
        add_collection_button.configure(fg_color="#212121")


def automatic_loading_of_data():
    smth = ctk.CTkLabel(scrollable_frame,height=80,width=200).pack()
    # Open the JSON file
    with open("data_base.json", "r") as file_reader:
        # Load the JSON content into a Python object
        data = json.load(file_reader)

    # Access the "Collections" object
    collections = data.get("Collections", {})
    

    # Iterate through each group in the collections object
    for group_name in collections:
        
        # Example: You can use group_name in a string or any other way you need
        button = ctk.CTkButton(scrollable_frame,fg_color="#181818",hover_color="#3d3d3d",border_color="#181818",
                                      border_width=0,font=("Roboto",28),text_color="white",text=group_name,
                                      height=80,width=200,corner_radius=0,anchor="w")
        button.pack()
        
   
        


#region IMAGES

user_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/user.png"))
notification_png_image = ctk.CTkImage(light_image=Image.open("png_pictures/notification.png"))
delete_collection_button = ctk.CTkImage(light_image=Image.open("png_pictures/trashcan_image.png"))

#endregion



#region FRAMES

main_app_frame = ctk.CTkFrame(app,fg_color="#181818").grid(sticky="nsew",row=0,column=0,rowspan=3,columnspan=2)

frame_line = ctk.CTkFrame(main_app_frame,height=2,fg_color="#3d3d3d")
frame_line.grid(row=0,column=0,columnspan=2,sticky="sew")

scrollable_frame = ctk.CTkScrollableFrame(main_app_frame,fg_color="#181818",corner_radius=0,
                                          scrollbar_button_color="#181818")
scrollable_frame.grid(row=1,column=0,sticky="ns",rowspan=2)


home_view_frame = ctk.CTkFrame(main_app_frame,corner_radius=0,fg_color="#181818")
home_view_frame.columnconfigure(2, weight=1)
home_view_frame.rowconfigure(2, weight=1)

main_frame_for_loaded_pictures = ctk.CTkScrollableFrame(main_app_frame,fg_color="#181818",border_color="#181818",corner_radius=0)
main_frame_for_loaded_pictures.grid(row=1,column=1,rowspan=2,columnspan=2,sticky="nsew")
main_frame_for_loaded_pictures.grid_columnconfigure(0,weight=1)
main_frame_for_loaded_pictures.grid_columnconfigure(1,weight=1)
main_frame_for_loaded_pictures.grid_columnconfigure(2,weight=1)


main_frame_for_loaded_pictures.grid_rowconfigure(0,weight=1)
main_frame_for_loaded_pictures.grid_rowconfigure(1,weight=1)
main_frame_for_loaded_pictures.grid_rowconfigure(2,weight=1)
main_frame_for_loaded_pictures.grid_rowconfigure(3,weight=1)
main_frame_for_loaded_pictures.grid_rowconfigure(4,weight=1)
main_frame_for_loaded_pictures.grid_rowconfigure(5,weight=1)

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
a_project_label.grid(row=0,column=0,sticky="new",pady=20)

#endregion



#region ENTRIES
search_entry = ctk.CTkEntry(main_app_frame,width=400,height=50,corner_radius=50,fg_color="#181818",text_color="white",placeholder_text="Search",
                            placeholder_text_color="white",border_color="#3d3d3d",font=("Roboto",24),bg_color="#181818")
search_entry.grid(row=1,column=1,sticky="n")

#endregion



#region BUTTONS

notification_button = ctk.CTkButton(app,width=15,fg_color="#181818",hover_color="#3d3d3d",
                                    image=notification_png_image,text="",corner_radius=50,bg_color="#181818")
notification_button.grid(row=0,column=1,sticky="e",padx=220,ipady=10,pady=10)


add_collection_button = ctk.CTkButton(main_app_frame,fg_color="#181818",hover_color="#3d3d3d",border_color="#181818",
                                      border_width=0,text="+Collection",font=("Roboto",28),text_color="white",
                                      height=80,width=200,corner_radius=0,command=click,anchor="w")
add_collection_button.grid(row=1,column=0,sticky="nw")


delete_collection_button = ctk.CTkButton(main_app_frame,image=delete_collection_button,text="",height=80,width=30,
                                         fg_color="#181818",hover_color="#3d3d3d",bg_color="#181818")
delete_collection_button.grid(row=1,column=0,sticky="ne")


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

automatic_loading_of_data()

app.mainloop()