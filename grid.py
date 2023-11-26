import customtkinter as ctk
import tkinter as tk
from PIL import Image 


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

#FUNCTIONS

def select_frame_by_name(name):
    home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")

    
    if name == "home":
        home_view_frame.grid(row=1, column=1, sticky="nsew",rowspan=2)
    else:
            home_view_frame.grid_forget()
        
            

def home_button_event():
        select_frame_by_name("home")
        



def add_button():
    pass
def add_button_on_click_entrie():
    pass


#IMAGES
user_png_image = ctk.CTkImage(light_image=Image.open("user_png.png"))
notification_png_image = ctk.CTkImage(light_image=Image.open("notification.png"))
home_button_image = ctk.CTkImage(light_image=Image.open("home.png"))

#FRAMES
scrollable_frame = ctk.CTkScrollableFrame(app,fg_color="white",corner_radius=0,
                                          scrollbar_button_color="white")
scrollable_frame.grid(row=1,column=0,sticky="ns",rowspan=2)

home_view_frame = ctk.CTkFrame(app,fg_color="black",corner_radius=0)
home_view_frame.columnconfigure(2, weight=1)
home_view_frame.rowconfigure(2, weight=1)


first_scrollable_frame_line = ctk.CTkFrame(scrollable_frame,height=2,fg_color="black",corner_radius=0)
first_scrollable_frame_line.grid(row=4,column=0,sticky="new")

#LABELS
label1 = ctk.CTkLabel(app,bg_color="white",corner_radius=0,font=("Arial Black",52),text="APP",text_color="black")
label1.grid(row=0,column=0,sticky="news")

user_png_image_label = ctk.CTkLabel(app, image=user_png_image,text="",fg_color="white")
user_png_image_label.grid(row=0,column=1,sticky="e",padx=110,ipadx=5,ipady=5)



#OPTION MENUS
user_drop_down = ctk.CTkOptionMenu(app,button_color="white",fg_color="white",dynamic_resizing=False,corner_radius=20,button_hover_color="white",
                                   text_color="black",values=["User","Options"],font=("Verdana",18),dropdown_font=("Verdana",18))
user_drop_down.grid(row=0,column=1,sticky="e",padx=80,ipadx=5,ipady=5)

#ENTRIES
search_entry = ctk.CTkEntry(app,width=400,height=50,corner_radius=50,fg_color="white",text_color="black",placeholder_text="Search",
                            placeholder_text_color="grey",border_color="black",font=("Verdana",24))
search_entry.grid(row=0,column=1)


#BUTTONS

plus_button = ctk.CTkButton(app,text="+",font=("Verdana",28),corner_radius=40,width=1,height=40)
plus_button.grid(row=0,column=1,sticky="w",padx=20,pady=20,ipadx=10,ipady=10)


notification_button = ctk.CTkButton(app,width=15,fg_color="white",hover_color='grey',
                                    image=notification_png_image,text="",corner_radius=50)
notification_button.grid(row=0,column=1,sticky="e",padx=300,ipadx=10,ipady=10)

home_button = ctk.CTkButton(scrollable_frame,image=home_button_image,fg_color="white",hover_color="#bab9b6",border_color="black",border_width=0,
                            text="Home",font=("Verdana",24),text_color="black",height=80,width=200,corner_radius=0,command=home_button_event)
home_button.grid(row=1,column=0,sticky="w")




app.mainloop()