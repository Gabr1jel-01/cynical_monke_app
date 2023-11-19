import customtkinter as ctk
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.title("Basic app")
        
        self.shorter_title_frame = ctk.CTkFrame(self,width=200,height=200)
        self.shorter_title_frame.place(x=0,y=0)
        
        
        self.shorter_title_frame_label = ctk.CTkLabel(self.shorter_title_frame,
                                                      text="AProject",
                                                      width=200,
                                                      height=100,
                                                      font=("Verdana",24),
                                                      corner_radius=0)
        self.shorter_title_frame_label.grid(row=0,column=0)
        
        
        
    
        self.add_collection_button = ctk.CTkButton(self.shorter_title_frame,
                                                   text="+Collection  ",
                                                   width=100,
                                                   height=100,
                                                   font=("Verdana",24),
                                                   corner_radius=0,
                                                   border_width=0)
        self.add_collection_button.grid(row=1,column=0,sticky="w")
        
        
        
        
        self.img = tk.PhotoImage(file="trashcan_image_png.png")
        self.shorter_title_frame_delete_button = ctk.CTkButton(self.shorter_title_frame,
                                                               image=self.img,
                                                               text="",
                                                               width=50,
                                                               height=102,
                                                               fg_color="red",
                                                               corner_radius=0,
                                                               border_width=0,
                                                               hover_color="#cd4848")
        self.shorter_title_frame_delete_button.grid(row=1,column=0,sticky="e")
        
        self.shorter_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                               width=190,
                                                               height=700,
                                                               corner_radius=0)
        self.shorter_scrollable_frame.place(x=0,y=200)
        
        
        
        
        
        
        
        self.longer_title_frame = ctk.CTkFrame(self,width=1400,
                                               height=100,
                                               fg_color="#4a8fcd",
                                               corner_radius=0)
        self.longer_title_frame.place(x=200,y=0)
      
      
      
      
        self.collections_label = ctk.CTkLabel(self.longer_title_frame,
                                              text="Collections",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.collections_label.place(x=0,y=0)
        
        self.import_label = ctk.CTkLabel(self.longer_title_frame,
                                              text="Import",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_label.place(x=400,y=0)
        
        self.import_USB = ctk.CTkLabel(self.longer_title_frame,
                                              text="USB",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_USB.place(x=800,y=0)
        
        self.import_settings = ctk.CTkLabel(self.longer_title_frame,
                                              text="Settings",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_settings.place(x=1200,y=0)
        
    
        
        
        
        
        
app = App()
app.mainloop()