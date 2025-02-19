import customtkinter as ctk
import tkinter as tk

# Set the appearance and theme for CustomTkinter
ctk.set_appearance_mode("dark")         # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")     # Themes: "blue", "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter Complex Example")
        self.geometry("1000x600")

        # ============= Left Frame (Sidebar) =============
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        self.sidebar_label = ctk.CTkLabel(self.sidebar_frame, text="CustomTkinter", 
                                          font=ctk.CTkFont(size=18, weight="bold"))
        self.sidebar_label.pack(pady=20, padx=20)

        self.button_1 = ctk.CTkButton(self.sidebar_frame, text="CTkButton 1")
        self.button_1.pack(pady=10, padx=20)

        self.button_2 = ctk.CTkButton(self.sidebar_frame, text="CTkButton 2")
        self.button_2.pack(pady=10, padx=20)

        self.button_3 = ctk.CTkButton(self.sidebar_frame, text="Disabled CTkButton", state="disabled")
        self.button_3.pack(pady=10, padx=20)

        # Appearance Mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:")
        self.appearance_mode_label.pack(pady=(30, 0), padx=20)

        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_mode_optionmenu.set("Dark")
        self.appearance_mode_optionmenu.pack(pady=(0, 20), padx=20)

        # ============= Main Content Frame =============
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Top Text Area
        self.top_label = ctk.CTkLabel(self.main_frame,
                                      text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
                                           "Sed diam nonummy nibh euismod tincidunt ut laoreet.\n"
                                           "Duis autem vel eum iriure dolor in hendrerit in vulputate.\n",
                                      wraplength=400,
                                      justify="left")
        self.top_label.pack(pady=10, padx=10)

        # A Tab View
        self.tab_view = ctk.CTkTabview(self.main_frame, width=400, height=150)
        self.tab_view.pack(pady=10, padx=10, fill="x")
        self.tab_view.add("Tab 1")
        self.tab_view.add("Tab 2")

        self.tab1_label = ctk.CTkLabel(self.tab_view.tab("Tab 1"), text="CTkLabel in Tab 1")
        self.tab1_label.pack(pady=10, padx=10)

        self.tab2_label = ctk.CTkLabel(self.tab_view.tab("Tab 2"), text="CTkLabel in Tab 2")
        self.tab2_label.pack(pady=10, padx=10)

        # Sliders & Progress
        self.slider_1 = ctk.CTkSlider(self.main_frame, from_=0, to=100, number_of_steps=5, command=self.slider_callback)
        self.slider_1.set(25)
        self.slider_1.pack(pady=10, padx=10, fill="x")

        self.slider_label = ctk.CTkLabel(self.main_frame, text="Slider Value: 25")
        self.slider_label.pack(pady=5, padx=10)

        self.progressbar_1 = ctk.CTkProgressBar(self.main_frame)
        self.progressbar_1.set(0.25)
        self.progressbar_1.pack(pady=10, padx=10, fill="x")

        # Radio Buttons
        self.radio_group_frame = ctk.CTkFrame(self.main_frame)
        self.radio_group_frame.pack(pady=10, padx=10, fill="x")

        self.radio_label = ctk.CTkLabel(self.radio_group_frame, text="CTkRadioButton Group:")
        self.radio_label.pack(anchor="w")

        self.radio_var = tk.StringVar(value="Option 1")
        self.radio_1 = ctk.CTkRadioButton(self.radio_group_frame, text="Option 1", variable=self.radio_var, value="Option 1")
        self.radio_2 = ctk.CTkRadioButton(self.radio_group_frame, text="Option 2", variable=self.radio_var, value="Option 2")
        self.radio_3 = ctk.CTkRadioButton(self.radio_group_frame, text="Option 3", variable=self.radio_var, value="Option 3")
        self.radio_1.pack(anchor="w")
        self.radio_2.pack(anchor="w")
        self.radio_3.pack(anchor="w")

        # Checkboxes
        self.checkbox_1 = ctk.CTkCheckBox(self.main_frame, text="CTkCheckBox")
        self.checkbox_1.pack(pady=10, padx=10, anchor="w")

        self.checkbox_2 = ctk.CTkCheckBox(self.main_frame, text="Disabled CheckBox", state="disabled")
        self.checkbox_2.pack(pady=5, padx=10, anchor="w")

        # Entry and Button
        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Type something...")
        self.entry.pack(pady=10, padx=10, fill="x")

        self.ctk_button = ctk.CTkButton(self.main_frame, text="CTkButton")
        self.ctk_button.pack(pady=10, padx=10)

    def slider_callback(self, value):
        self.slider_label.configure(text=f"Slider Value: {int(value)}")
        self.progressbar_1.set(value / 100)

    def change_appearance_mode(self, new_mode):
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
