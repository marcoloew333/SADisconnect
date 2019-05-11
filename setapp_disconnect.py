try:
    from selenium import webdriver
    import time
    import os
    import tkinter as tk
    from tkinter import ttk
    from tkinter import Menu
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


def site_login():
    try:
        driver.get("https://my.setapp.com/login")
        time.sleep(4)
        driver.find_element_by_id("email").send_keys("marco.loew@haw-hamburg.de")
        time.sleep(0.1)
        driver.find_element_by_id("password").send_keys("je88kk312E\x23set")
        time.sleep(0.1)
        driver.find_element_by_css_selector("button.btn.btn-block.btn-primary").click()
        time.sleep(3)
        driver.find_element_by_css_selector("a[href*='/devices']").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button[data-qa*='disconnect-device-button']").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button[data-qa*='disconnect-device-confirm-btn']").click()
        time.sleep(0.3)
        driver.quit()
    except ConnectionError:
        notify("Error", "Disconnect failed")


# exit code
def _exit():
    driver.quit()
    win.quit()
    win.destroy()
    exit()


# UI initialisation
win = tk.Tk()
win.title("Linked In Downloader")

# UI design
AccountDetailsFrame = ttk.LabelFrame(win, text="Login")
AccountDetailsFrame.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(AccountDetailsFrame, text="Mail Address").grid(column=0, row=0)
login_mail = tk.StringVar()
entered_login_mail = tk.Entry(AccountDetailsFrame, width=25, textvariable=login_mail)
entered_login_mail.grid(column=1, row=0)

ttk.Label(AccountDetailsFrame, text="Password").grid(column=0, row=1)
login_pw = tk.StringVar()
entered_login_pw = tk.Entry(AccountDetailsFrame, width=25, textvariable=login_pw)
entered_login_pw.grid(column=1, row=1)

# button
login_button = ttk.Button(win, text="Connect", command=site_login)
login_button.grid(column=0, row=2, sticky="WE", padx=10, pady=5)
quit_button = ttk.Button(win, text="Quit Instance", command=_exit)
quit_button.grid(column=0, row=3, sticky="WE", padx=10, pady=5)

# site_login()
# notify("Completed", "This Mac is now ready for login to Setapp.")

# menubar
menubar = Menu(win)
win.config(menu=menubar)
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Exit", command=_exit)

for child in AccountDetailsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10)

# UI execution
win.mainloop()

# driver.quit()

