import tkinter as tk
import math

window = tk.Tk()
window.title("Improved Calculator")
window.geometry("320x380")
window.resizable(False, False)

# ---------------- Functions ----------------

def press_num(num):
    text = entr_label.cget("text")

        if text == "0":
                entr_label.configure(text=str(num))
                    else:
                            entr_label.configure(text=text + str(num))


                            def press_op(op):
                                text = entr_label.cget("text")
                                    expr = expr_label.cget("text")

                                        expr_label.configure(text=expr + text + op)
                                            entr_label.configure(text="0")


                                            def press_C():
                                                expr_label.configure(text="")
                                                    entr_label.configure(text="0")


                                                    def press_eq():
                                                        text = entr_label.cget("text")
                                                            expr = expr_label.cget("text")

                                                                try:
                                                                        result = eval(expr + text)
                                                                                expr_label.configure(text=expr + text + " =")
                                                                                        entr_label.configure(text=str(result))

                                                                                            except ZeroDivisionError:
                                                                                                    entr_label.configure(text="Division by Zero")

                                                                                                        except SyntaxError:
                                                                                                                entr_label.configure(text="Syntax Error")

                                                                                                                    except Exception:
                                                                                                                            entr_label.configure(text="Error")


                                                                                                                            def negate():
                                                                                                                                text = entr_label.cget("text")

                                                                                                                                    if text.startswith("-"):
                                                                                                                                            entr_label.configure(text=text[1:])
                                                                                                                                                elif text != "0":
                                                                                                                                                        entr_label.configure(text="-"+text)


                                                                                                                                                        def square():
                                                                                                                                                            try:
                                                                                                                                                                    value = float(entr_label.cget("text"))
                                                                                                                                                                            entr_label.configure(text=str(value ** 2))
                                                                                                                                                                                except:
                                                                                                                                                                                        entr_label.configure(text="Error")


                                                                                                                                                                                        def square_root():
                                                                                                                                                                                            try:
                                                                                                                                                                                                    value = float(entr_label.cget("text"))

                                                                                                                                                                                                            if value < 0:
                                                                                                                                                                                                                        entr_label.configure(text="Invalid")
                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                            entr_label.configure(text=str(math.sqrt(value)))

                                                                                                                                                                                                                                                except:
                                                                                                                                                                                                                                                        entr_label.configure(text="Error")


                                                                                                                                                                                                                                                        # ---------------- Display ----------------

                                                                                                                                                                                                                                                        expr_label = tk.Label(
                                                                                                                                                                                                                                                            window,
                                                                                                                                                                                                                                                                text="",
                                                                                                                                                                                                                                                                    bg="lightgrey",
                                                                                                                                                                                                                                                                        width=35,
                                                                                                                                                                                                                                                                            height=2,
                                                                                                                                                                                                                                                                                anchor=tk.E,
                                                                                                                                                                                                                                                                                    relief="ridge"
                                                                                                                                                                                                                                                                                    )

                                                                                                                                                                                                                                                                                    expr_label.grid(row=0, column=0, columnspan=5)

                                                                                                                                                                                                                                                                                    entr_label = tk.Label(
                                                                                                                                                                                                                                                                                        window,
                                                                                                                                                                                                                                                                                            text="0",
                                                                                                                                                                                                                                                                                                bg="white",
                                                                                                                                                                                                                                                                                                    width=35,
                                                                                                                                                                                                                                                                                                        height=2,
                                                                                                                                                                                                                                                                                                            anchor=tk.E,
                                                                                                                                                                                                                                                                                                                font=("Arial", 15),
                                                                                                                                                                                                                                                                                                                    relief="ridge"
                                                                                                                                   )

                                                                                                                                                                                                                                                                                                                    entr_label.grid(row=1, column=0, columnspan=5)