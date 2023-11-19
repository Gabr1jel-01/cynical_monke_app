import customtkinter as ctk
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900")
        self.title("Basic app")
        
        #region SHORTER FRAME 
        self.shorter_title_frame = ctk.CTkFrame(self,width=200,height=200)
        self.shorter_title_frame.place(x=0,y=0)
        
        # MAIN LABEL NAME OF PROJECT
        self.shorter_title_frame_label = ctk.CTkLabel(self.shorter_title_frame,
                                                      text="AProject",
                                                      width=200,
                                                      height=100,
                                                      font=("Verdana",24),
                                                      corner_radius=0)
        self.shorter_title_frame_label.grid(row=0,column=0)
        
        
        
        # ADD BUTTON 
        self.add_collection_button = ctk.CTkButton(self.shorter_title_frame,
                                                   text="+Collection  ",
                                                   width=100,
                                                   height=100,
                                                   font=("Verdana",24),
                                                   corner_radius=0,
                                                   border_width=0)
        self.add_collection_button.grid(row=1,column=0,sticky="w")
        
        
        
        # TRASHCAN IMAGE
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
        
        
        #SCROLLABLE FRAME
        self.shorter_scrollable_frame = ctk.CTkScrollableFrame(self,
                                                               width=190,
                                                               height=700,
                                                               corner_radius=0)
        self.shorter_scrollable_frame.place(x=0,y=200)
        
        #BAGS BUTTON
        self.bags_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Bags",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.bags_button.pack(pady=5)
        
        #BIRD BUTTON
        self.bird_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Bird",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.bird_button.pack(pady=5)
        
        #BLANKETS BUTTON
        self.blankets_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Blankets",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.blankets_button.pack(pady=5)
        
        #CAPS BUTTON
        self.caps_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Caps",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.caps_button.pack(pady=5)
        
        #CARS BUTTON
        self.cars_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Cars",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.cars_button.pack(pady=5)
        
        #CATDOGS BUTTON
        self.catdogs_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="CatDogs",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.catdogs_button.pack(pady=5)
        
        #CATS BUTTON
        self.cat_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Cat",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.cat_button.pack(pady=5)
        
        #DOGS BUTTON
        self.dogs_button = ctk.CTkButton(self.shorter_scrollable_frame,
                                         text="Dogs",
                                         font=("Verdana",24),
                                         height=100,
                                         width=200,
                                         corner_radius=0)
        self.dogs_button.pack(pady=5)
        #endregion
               
        #region LONGER FRAME
        
        self.longer_title_frame = ctk.CTkFrame(self,width=1400,
                                               height=100,
                                               fg_color="#4a8fcd",
                                               corner_radius=0)
        self.longer_title_frame.place(x=200,y=0)
      
      
      
        # COLLECTION LABEL
        self.collections_label = ctk.CTkLabel(self.longer_title_frame,
                                              text="Collections",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.collections_label.place(x=0,y=0)
        
        #IMPORT LABEL
        self.import_label = ctk.CTkLabel(self.longer_title_frame,
                                              text="Import",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_label.place(x=400,y=0)
        
        #USB LABEL
        self.import_USB = ctk.CTkLabel(self.longer_title_frame,
                                              text="USB",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_USB.place(x=800,y=0)
        
        #SETTINGS LABEL
        self.import_settings = ctk.CTkLabel(self.longer_title_frame,
                                              text="Settings",
                                              height=100,
                                              width=200,
                                              font=("Verdana",24))
        self.import_settings.place(x=1200,y=0)
        #endregion
    
        #region PAGES
        self.main_frame = ctk.CTkScrollableFrame(self, fg_color="grey",
                                       height=800,
                                       width=1385,
                                       corner_radius=0)
        self.main_frame.place(x=200,y=100)
        
        
        
        #endregion
        
        
        
        
        
app = App()
app.mainloop()