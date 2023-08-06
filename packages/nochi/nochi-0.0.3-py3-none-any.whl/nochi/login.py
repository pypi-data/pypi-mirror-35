from tkinter import *
import tkinter.messagebox as messagebox
import time, sys, os

FONT = 'none 18'
folder = __file__.rstrip('login.py')
assert os.path.exists(folder+'password.txt'), 'Password.txt is not in the same folder as login.py'


class ChangePassword():

    def displayChange(self, window, exit=True):
        if exit:
            window.destroy()
        window = Tk()
        window.title('Change Password')
        window.iconbitmap(folder+'logo.ico')

        # Create widgets
        self.currentPasswordLabel = Label(window, text='Current Password', font=FONT)
        self.newPasswordLabel = Label(window, text='New Password', font=FONT)
        self.confirmPasswordLabel = Label(window, text='Confirm Password', font=FONT)

        self.currentPasswordEntry = Entry(window, font=FONT, show='•'); self.currentPasswordEntry.focus()
        self.newPasswordEntry = Entry(window, font=FONT, show='•')
        self.confirmPasswordEntry = Entry(window, font=FONT, show='•')

        self.passwordStatusLabel = Label(window, text='Fill out boxes',  font=FONT, fg='green')
        changePassword = Button(window, text='Change Password', font=FONT, command=lambda: self.newPasswordFunction(window))


        # Display widgets
        self.passwordStatusLabel.grid(column=0, row=0, columnspan=2, padx=3, pady=3)
        
        self.currentPasswordLabel.grid(column=0, row=1, sticky=W)
        self.newPasswordLabel.grid(column=0, row=2, sticky=W, padx=3, pady=3)
        self.confirmPasswordLabel.grid(column=0, row=3, sticky=W, padx=3, pady=3)

        self.currentPasswordEntry.grid(column=1, row=1, sticky=W, padx=3, pady=3)
        self.newPasswordEntry.grid(column=1, row=2, sticky=W, padx=3, pady=3)
        self.confirmPasswordEntry.grid(column=1, row=3, sticky=W, padx=3, pady=3)

        changePassword.grid(column=0, row=5, padx=3, pady=3)

        window.bind('<Return>', lambda x: self.newPasswordFunction(window))
        window.wm_protocol('WM_DELETE_WINDOW', lambda: exit(window))
        window.mainloop()
        

    def newPasswordFunction(self, window):
        # Retrive password from password.txt
        file = open(folder+'password.txt', 'r')
        validPassword = file.read()
        file.close()

        
        if self.currentPasswordEntry.get() != '':
            # Check if newPassword and validPassword match
            if self.currentPasswordEntry.get() == validPassword:
                
                if self.newPasswordEntry.get() != '' and self.confirmPasswordEntry.get() != '':
                    
                    if self.newPasswordEntry.get() == self.confirmPasswordEntry.get():
                        
                        newPassword = self.newPasswordEntry.get()
                        
                        # Change password
                        file = open(folder+'password.txt', 'w')
                        file.write(newPassword)
                        file.close()
                        
                        self.passwordStatusLabel.configure(text='Changing Password...', fg='green')
                        window.after(2000, messagebox.showinfo, 'Change Password', 'Succesfully Changed Password!')
                        window.destroy()
                    
                    else: # self.newPasswordEntry.get() != self.confirmPasswordEntry.get()
                        self.passwordStatusLabel.configure(text='Passwords do not match', fg='red')
                        self.newPasswordEntry.delete(0, END); self.confirmPasswordEntry.delete(0, END)
                        
                else: # self.newPasswordEntry.get == '' and self.confirmPasswordEntry.get() == ''
                    self.passwordStatusLabel.configure(text='Enter new password', fg='red')

            else: # self.currentPasswordEntry.get() != validPassword
                self.passwordStatusLabel.configure(text='Current password is incorrect', fg='red')
                self.currentPasswordEntry.delete(0, END)


class Login(ChangePassword):

    def startup(self):
        # Set up window
        window = Tk()
        window.title('Login')
        window.iconbitmap(folder+'logo.ico')
        
        # Retrive password from password.txt
        file = open(folder+'password.txt', 'r')
        self.validPassword = file.read()
        file.close()

        # Create widgets
        self.statusLabel = Label(window, text='Waiting for Password...', font=FONT, fg='green')
        self.passwordLabel = Label(window, text='Password', font=FONT, width=7)
        self.passwordEntry = Entry(window, font=FONT, show='•', width=17)
        self.passwordEntry.focus()
        self.login = Button(window, text='Login', font=FONT, command=lambda: self.checkPassword(window), width=7)
        self.changePassword = Button(window, text='Change Password', font=FONT, command=lambda: self.displayChange(window))

        # Display widgets
        self.statusLabel.grid(column=0, row=0, columnspan=2, padx=3, pady=3)
        self.passwordLabel.grid(column=0, row=1, sticky=W, padx=3, pady=3)
        self.passwordEntry.grid(column=1, row=1, padx=3, pady=3)
        self.login.grid(column=0, row=2, sticky=W, padx=3, pady=3)
        self.changePassword.grid(column=1, row=2, sticky=W, padx=3, pady=3)

        window.bind('<Return>', lambda x: self.checkPassword(window))
        window.wm_protocol('WM_DELETE_WINDOW', lambda: exit(window))
        window.mainloop()


    def checkPassword(self, window):
        # Check for equality beween entered password and validPassword
        password = self.passwordEntry.get()
        if password != '':
            if password == self.validPassword:
                self.statusLabel.configure(text='Loging In...', fg='green')
                window.after(2000, messagebox.showinfo, 'Login', 'Succesfully Logged in!')
                window.destroy()
                return
            else:
                self.statusLabel.configure(text='Incorrect Password', fg='red')
                self.passwordEntry.delete(0, END)

        else:
            self.statusLabel.configure(text='Please Enter Password', fg='red')

def exit(window):
    window.destroy()
    sys.exit()

if __name__ == '__main__':
    login = Login()
    login.startup()
