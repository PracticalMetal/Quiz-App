THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
import time
from quiz_brain import QuizBrain

class UserInterface:
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20)
        self.window.config(background=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,background="white")
        self.qtext=self.canvas.create_text(150,125,text="elf.get_next_question",fill="black",font=("Arial",20,"italic"),width=250)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.get_next_question()

        # creating the text
        self.score=Label(text=f"Score: {self.quiz.score}",background=THEME_COLOR,fg="white",padx=20,pady=20)
        self.score.grid(row=0,column=1)

        # Creating buttons
        true_btn=PhotoImage(file="images/true.png")
        false_btn=PhotoImage(file="images/false.png")
        self.true=Button(image=true_btn,highlightthickness=0,command=self.true_bn)
        # self.true.config(padx=20,pady=20)
        self.false=Button(image=false_btn,highlightthickness=0,command=self.false_bn)
        self.true.grid(row=2,column=0,padx=20,pady=20)
        self.false.grid(row=2,column=1,padx=20,pady=20)
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.qtext,text=q_text)

    def true_bn(self)->str:
        self.give_feedback(self.quiz.check_answer("true"))
        self.score.config(text=f"Score: {self.quiz.score}")
        
        self.get_next_question()

    def false_bn(self)->str:
        self.give_feedback(self.quiz.check_answer("false"))
        self.score.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def give_feedback(self,if_true:bool):
        if if_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,self.get_next_question)
        

