try:
    from selenium import webdriver
    import time
    import os
    import tkinter as tk
    from tkinter import ttk
    from tkinter import Menu
    from tkinter import messagebox as mBox
except ImportError:
    print("Necessary module could not be loaded")

# Object to configure Chrome
options = webdriver.ChromeOptions()

# Start Chrome in headless mode
options.add_argument('headless')

# Set window size
options.add_argument('window-size=1200x600')

# Define variable 'driver' and apply the predefined options
driver = webdriver.Chrome('/Applications/chromedriver', options=options)


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


def _msgBox():
    mBox.showwarning("Warning", "Disconnect interrupted")


def site_login(event):
    try:
        driver.get("https://my.setapp.com/login")
        time.sleep(4)
        driver.find_element_by_id("email").send_keys(entered_login_mail.get())
        time.sleep(0.1)
        driver.find_element_by_id("password").send_keys(entered_login_pw.get())
        time.sleep(0.1)
        driver.find_element_by_css_selector("button.btn.btn-block.btn-primary").click()
        time.sleep(5)
        driver.find_element_by_xpath('//a[@href="/devices"]').click()
        time.sleep(3)
        driver.find_element_by_css_selector("button[data-qa*='disconnect-device-button']").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button[data-qa*='disconnect-device-confirm-btn']").click()
        time.sleep(0.3)
        driver.quit()
        notify("Completed", "This Mac is now ready for login to Setapp.")
    except ConnectionError:
        notify("Error", "Disconnect failed")


# exit code
def _exit():
    driver.quit()
    win.quit()
    win.destroy()


# UI initialisation
win = tk.Tk()
win.title("Linked In Downloader")

# Icon
win.iconbitmap("SetappDisconnectIcon.icns")

# UI design
AccountDetailsFrame = ttk.LabelFrame(win, text="Login")
AccountDetailsFrame.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(AccountDetailsFrame, text="Mail Address").grid(column=0, row=0)
login_mail = tk.StringVar(value="marco.loew@haw-hamburg.de")  # initializing string variable
entered_login_mail = tk.Entry(AccountDetailsFrame, width=25, textvariable=login_mail)
entered_login_mail.grid(column=1, row=0)

ttk.Label(AccountDetailsFrame, text="Password").grid(column=0, row=1)
login_pw = tk.StringVar()
entered_login_pw = tk.Entry(AccountDetailsFrame, width=25, textvariable=login_pw, show="*")
entered_login_pw.grid(column=1, row=1)
entered_login_pw.focus()

# button
login_button = ttk.Button(win, text="Connect", command=site_login)
login_button.grid(column=0, row=2, sticky="WE", padx=10, pady=5)
quit_button = ttk.Button(win, text="Quit Instance", command=_exit)
quit_button.grid(column=0, row=3, sticky="WE", padx=10, pady=5)

# key bindings
entered_login_pw.bind("<Return>", site_login)

# site_login()
# notify("Completed", "This Mac is now ready for login to Setapp.")

# menubar
menubar = Menu(win)
win.config(menu=menubar)
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=_exit)
fileMenu.add_command(label="About", command=_msgBox)

for child in AccountDetailsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# UI execution


if __name__ == "__main__":
    win.mainloop()
