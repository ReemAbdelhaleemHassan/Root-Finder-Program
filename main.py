import tkinter
from tkinter import messagebox, filedialog
from tkinter import *
from tkinter import ttk
import time
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from methods import *
from variables import *
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from math import sin, cos, tan, e


def plotting_window(expression):
    x = np.linspace(PLOTTING_RANGE[0], PLOTTING_RANGE[1], 100)
    fx = lambda x: eval(expression)
    exact_root = fsolve(fx, 1)
    fig = plt.figure(figsize=(5, 5))
    # adding the subplot
    ax = fig.add_subplot(111)
    # plotting the graph
    ax.plot(x, fx(x))
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid()
    ax.set_title(f"Function: {expression}\nExact Root is {exact_root[0]}")
    # placing the canvas on the Tkinter window
    window = Tk()
    canvas = FigureCanvasTkAgg(fig, window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    # setting the title
    window.title('Plotting The function')
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    plt.scatter(exact_root[0], 0)


# Reading From Text File
def open_file(function):
    if file := filedialog.askopenfile(
        mode='r', filetypes=[('Text Files', '*.txt')]
    ):
        content = file.readline().replace('\n', '')
        file.close()
        function.set(str(content))


def call_Bisection(f, a, b, n, e, tab, button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = MAX_ITR
    if len(e) == 0:
        e = EPSILON

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab, column=("c1", "c2", "c3", "c4", "c5"), show='headings', yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER, width=75)
    tree.heading("# 2", text="Xl")
    tree.column("# 3", anchor=CENTER, width=75)
    tree.heading("# 3", text="Xu")
    tree.column("# 4", anchor=CENTER, width=75)
    tree.heading("# 4", text="Xr")
    tree.column("# 5", anchor=CENTER, width=125)
    tree.heading("# 5", text="f(Xr)")

    start_time = time.time()
    root, k = bisection(f, float(a), float(b), tree, float(e), n)
    end_time = time.time()

    er_label = ttk.Label(tab, text='Bisection Failed', font=("Courier", 15))
    root_label = ttk.Label(
        tab, text=f'Approx. Root = {str(root)}', font=("Courier", 10)
    )

    time_label = ttk.Label(
        tab,
        text=f'Execution Time = {str(end_time - start_time)}',
        font=("Courier", 10),
    )

    iter_label = ttk.Label(
        tab,
        text=f'# of Iterations = {len(tree.get_children())}',
        font=("Courier", 10),
    )

    k_label = ttk.Label(
        tab, text=f'Expected # of iterations = {str(k)}', font=("Courier", 10)
    )


    if root is None:
        er_label.pack()
        er_label.place(x=500, y=250)
    else:
        root_label.pack()
        root_label.place(x=475, y=150)
        time_label.pack()
        time_label.place(x=475, y=250)
        iter_label.pack()
        iter_label.place(x=475, y=350)
        k_label.pack()
        k_label.place(x=475, y=400)

    tree.pack(fill=BOTH)
    tree.place(x=50, y=100, height=300, width=400)
    iterations.place(x=450, y=100, height=300)
    iterations.config(command=tree.yview)


def call_False_Position(f, a, b, n, e, tab, button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = MAX_ITR
    if len(e) == 0:
        e = EPSILON

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab, column=("c1", "c2", "c3", "c4", "c5"), show='headings', yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER, width=75)
    tree.heading("# 2", text="Xl")
    tree.column("# 3", anchor=CENTER, width=75)
    tree.heading("# 3", text="Xu")
    tree.column("# 4", anchor=CENTER, width=75)
    tree.heading("# 4", text="Xr")
    tree.column("# 5", anchor=CENTER, width=125)
    tree.heading("# 5", text="f(Xr)")

    start_time = time.time()
    root = false_position(f, float(a), float(b), tree, float(e), n)
    end_time = time.time()

    er_label = ttk.Label(tab, text='False Position Method Failed', font=("Courier", 15))
    root_label = ttk.Label(
        tab, text=f'Approx. Root = {str(root)}', font=("Courier", 10)
    )

    time_label = ttk.Label(
        tab,
        text=f'Execution Time = {str(end_time - start_time)}',
        font=("Courier", 10),
    )

    iter_label = ttk.Label(
        tab,
        text=f'# of Iterations = {len(tree.get_children())}',
        font=("Courier", 10),
    )


    if root is None:
        er_label.pack()
        er_label.place(x=500, y=250)
    else:
        root_label.pack()
        root_label.place(x=475, y=150)
        time_label.pack()
        time_label.place(x=475, y=250)
        iter_label.pack()
        iter_label.place(x=475, y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50, y=100, height=300, width=400)
    iterations.place(x=450, y=100, height=300)
    iterations.config(command=tree.yview)


def call_Fixed_Point(f, a, n, e, tab, button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = MAX_ITR
    if len(e) == 0:
        e = EPSILON

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab, column=("c1", "c2", "c3", "c4", "c5"), show='headings', yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER, width=75)
    tree.heading("# 2", text="Xi")
    tree.column("# 3", anchor=CENTER, width=75)
    tree.heading("# 3", text="f(x)")

    start_time = time.time()
    root, convergence = fixed_point(f, float(a), tree, float(e), n)
    end_time = time.time()

    er_label = ttk.Label(tab, text='Fixed Point Method Failed', font=("Courier", 15))
    root_label = ttk.Label(
        tab, text=f'Approx. Root = {str(root)}', font=("Courier", 10)
    )

    time_label = ttk.Label(
        tab,
        text=f'Execution Time = {str(end_time - start_time)}',
        font=("Courier", 10),
    )

    iter_label = ttk.Label(
        tab,
        text=f'# of Iterations = {len(tree.get_children())}',
        font=("Courier", 10),
    )

    conv_label = ttk.Label(tab, text=f'G(X) {convergence}', font=("Courier", 10))

    if root is None:
        er_label.pack()
        er_label.place(x=500, y=250)
    else:
        root_label.pack()
        root_label.place(x=475, y=150)
        time_label.pack()
        time_label.place(x=475, y=250)
        iter_label.pack()
        iter_label.place(x=475, y=350)
    conv_label.pack()
    conv_label.place(x=475, y=400)
    tree.pack(fill=BOTH)
    tree.place(x=50, y=100, height=300, width=400)
    iterations.place(x=450, y=100, height=300)
    iterations.config(command=tree.yview)


def call_Newton_Raphson(f, a, n, e, tab, button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = MAX_ITR
    if len(e) == 0:
        e = EPSILON

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab, column=("c1", "c2", "c3", "c4", "c5"), show='headings', yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER, width=75)
    tree.heading("# 2", text="Xi")
    tree.column("# 3", anchor=CENTER, width=75)
    tree.heading("# 3", text="f(x)")

    start_time = time.time()
    root = newton_raphson(f, float(a), tree, float(e), n)
    end_time = time.time()

    er_label = ttk.Label(tab, text='Fixed Point Method Failed', font=("Courier", 15))
    root_label = ttk.Label(
        tab, text=f'Approx. Root = {str(root)}', font=("Courier", 10)
    )

    time_label = ttk.Label(
        tab,
        text=f'Execution Time = {str(end_time - start_time)}',
        font=("Courier", 10),
    )

    iter_label = ttk.Label(
        tab,
        text=f'# of Iterations = {len(tree.get_children())}',
        font=("Courier", 10),
    )


    if root is None:
        er_label.pack()
        er_label.place(x=500, y=250)
    else:
        root_label.pack()
        root_label.place(x=475, y=150)
        time_label.pack()
        time_label.place(x=475, y=250)
        iter_label.pack()
        iter_label.place(x=475, y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50, y=100, height=300, width=400)
    iterations.place(x=450, y=100, height=300)
    iterations.config(command=tree.yview)


def call_Secant(f, a, b, n, e, tab, button):
    button['state'] = DISABLED
    if len(n) == 0:
        n = MAX_ITR
    if len(e) == 0:
        e = EPSILON

    iterations = ttk.Scrollbar(tab)
    iterations.pack()
    tree = ttk.Treeview(tab, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings',
                        yscrollcommand=iterations.set)
    tree.column("# 1", anchor=CENTER, width=50)
    tree.heading("# 1", text="i")
    tree.column("# 2", anchor=CENTER, width=70)
    tree.heading("# 2", text="Xi-1")
    tree.column("# 3", anchor=CENTER, width=70)
    tree.heading("# 3", text="Xi")
    tree.column("# 4", anchor=CENTER, width=70)
    tree.heading("# 4", text="f(Xi-1)")
    tree.column("# 5", anchor=CENTER, width=70)
    tree.heading("# 5", text="f(Xi)")
    tree.column("# 6", anchor=CENTER, width=70)
    tree.heading("# 6", text="Xi+1")

    start_time = time.time()
    root = secant(f, float(a), float(b), tree, float(e), n)
    end_time = time.time()

    er_label = ttk.Label(tab, text='Secant Failed', font=("Courier", 15))
    root_label = ttk.Label(
        tab, text=f'Approx. Root = {str(root)}', font=("Courier", 10)
    )

    time_label = ttk.Label(
        tab,
        text=f'Execution Time = {str(end_time - start_time)}',
        font=("Courier", 10),
    )

    iter_label = ttk.Label(
        tab,
        text=f'# of Iterations = {len(tree.get_children())}',
        font=("Courier", 10),
    )


    if root is None:
        er_label.pack()
        er_label.place(x=500, y=250)
    else:
        root_label.pack()
        root_label.place(x=475, y=150)
        time_label.pack()
        time_label.place(x=475, y=250)
        iter_label.pack()
        iter_label.place(x=475, y=350)

    tree.pack(fill=BOTH)
    tree.place(x=50, y=100, height=300, width=400)
    iterations.place(x=450, y=100, height=300)
    iterations.config(command=tree.yview)


def MethodSelection(expression):
    newWindow = Toplevel(main)
    newWindow.title("Methods")
    newWindow.geometry("800x500")
    newWindow.resizable(False, False)
    if 'cos' in expression or 'sin' in expression:
        print('cannot plot')
        fx = lambda x: eval(expression)
        exact_root = fsolve(fx, 1)
        print('Exact Root')
        print(exact_root)
    else:
        plotting_window(expression)

    tabControl = ttk.Notebook(newWindow)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Bisection')
    tabControl.add(tab2, text='False Postion')
    tabControl.add(tab3, text='Fixed Point')
    tabControl.add(tab4, text='Newton Raphson')
    tabControl.add(tab5, text='Secant')
    tabControl.pack(expand=1, fill="both")

    # --------------Bisection--------------
    f_label = ttk.Label(tab1, text='Function = ' + expression, font=("Arial", 18)).pack()
    m_i_label = ttk.Label(tab1, text='Enter Max Iterations:')
    e_label = ttk.Label(tab1, text='Enter Epsilon:')
    a_label = ttk.Label(tab1, text='Enter Interval From:')
    b_label = ttk.Label(tab1, text='To')
    max_iteration = ttk.Entry(tab1)
    epsilon = ttk.Entry(tab1)
    a_bis = ttk.Entry(tab1)
    b_bis = ttk.Entry(tab1)

    cal_button = ttk.Button(tab1, text='Calculate',
                            command=lambda: call_Bisection(expression, a_bis.get(), b_bis.get(), max_iteration.get(),
                                                           epsilon.get(), tab1, cal_button))
    m_i_label.pack()
    m_i_label.place(x=40, y=50)
    max_iteration.pack()
    max_iteration.place(x=155, y=50, height=20, width=50)
    e_label.pack()
    e_label.place(x=220, y=50)
    epsilon.pack()
    epsilon.place(x=295, y=50, height=20, width=50)
    a_label.pack()
    a_label.place(x=370, y=50)
    a_bis.pack()
    a_bis.place(x=490, y=50, height=20, width=50)
    b_label.pack()
    b_label.place(x=545, y=50)
    b_bis.pack()
    b_bis.place(x=570, y=50, height=20, width=50)
    cal_button.pack()
    cal_button.place(x=675, y=50)

    # --------------False Position--------------
    f_label = ttk.Label(tab2, text='Function = ' + expression, font=("Arial", 18)).pack()
    m_i_label = ttk.Label(tab2, text='Enter Max Iterations:')
    e_label = ttk.Label(tab2, text='Enter Epsilon:')
    a_label = ttk.Label(tab2, text='Enter Interval From:')
    b_label = ttk.Label(tab2, text='To')
    max_iteration = ttk.Entry(tab2)
    epsilon = ttk.Entry(tab2)
    a_fal = ttk.Entry(tab2)
    b_fal = ttk.Entry(tab2)

    cal_button_2 = ttk.Button(tab2, text='Calculate',
                            command=lambda: call_False_Position(expression, a_fal.get(), b_fal.get(),
                                                                max_iteration.get(),
                                                                epsilon.get(), tab2, cal_button_2))
    m_i_label.pack()
    m_i_label.place(x=40, y=50)
    max_iteration.pack()
    max_iteration.place(x=155, y=50, height=20, width=50)
    e_label.pack()
    e_label.place(x=220, y=50)
    epsilon.pack()
    epsilon.place(x=295, y=50, height=20, width=50)
    a_label.pack()
    a_label.place(x=370, y=50)
    a_fal.pack()
    a_fal.place(x=490, y=50, height=20, width=50)
    b_label.pack()
    b_label.place(x=545, y=50)
    b_fal.pack()
    b_fal.place(x=570, y=50, height=20, width=50)
    cal_button_2.pack()
    cal_button_2.place(x=675, y=50)

    # --------------Fixed Point--------------
    f_label = ttk.Label(tab3, text='Function = ' + expression, font=("Arial", 18)).pack()
    m_i_label = ttk.Label(tab3, text='Enter Max Iterations:')
    e_label = ttk.Label(tab3, text='Enter Epsilon:')
    a_label = ttk.Label(tab3, text='Enter G(X):')
    b_label = ttk.Label(tab3, text='Enter Initial Guess')
    max_iteration = ttk.Entry(tab3)
    epsilon = ttk.Entry(tab3)
    gx = ttk.Entry(tab3)
    xi = ttk.Entry(tab3)

    cal_button_3 = ttk.Button(tab3, text='Calculate',
                            command=lambda: call_Fixed_Point(gx.get(), xi.get(), max_iteration.get(),
                                                             epsilon.get(), tab3, cal_button_3))
    m_i_label.pack()
    m_i_label.place(x=40, y=50)
    max_iteration.pack()
    max_iteration.place(x=155, y=50, height=20, width=50)
    e_label.pack()
    e_label.place(x=220, y=50)
    epsilon.pack()
    epsilon.place(x=295, y=50, height=20, width=50)
    a_label.pack()
    a_label.place(x=370, y=50)
    gx.pack()
    gx.place(x=430, y=50, height=20, width=50)
    b_label.pack()
    b_label.place(x=500, y=50)
    xi.pack()
    xi.place(x=600, y=50, height=20, width=50)
    cal_button_3.pack()
    cal_button_3.place(x=675, y=50)

    # --------------Newton Raphson--------------
    f_label = ttk.Label(tab4, text='Function = ' + expression, font=("Arial", 18)).pack()
    m_i_label = ttk.Label(tab4, text='Enter Max Iterations:')
    e_label = ttk.Label(tab4, text='Enter Epsilon:')
    a_label = ttk.Label(tab4, text='Enter Intial Guess:')
    # b_label = ttk.Label(tab4, text='To')
    max_iteration = ttk.Entry(tab4)
    epsilon = ttk.Entry(tab4)
    a_new = ttk.Entry(tab4)
    # b_fal = ttk.Entry(tab4)

    cal_button_4 = ttk.Button(tab4, text='Calculate',
                            command=lambda: call_Newton_Raphson(expression, a_new.get(), max_iteration.get(),
                                                                epsilon.get(), tab4, cal_button_4))
    m_i_label.pack()
    m_i_label.place(x=40, y=50)
    max_iteration.pack()
    max_iteration.place(x=155, y=50, height=20, width=50)
    e_label.pack()
    e_label.place(x=220, y=50)
    epsilon.pack()
    epsilon.place(x=295, y=50, height=20, width=50)
    a_label.pack()
    a_label.place(x=370, y=50)
    a_new.pack()
    a_new.place(x=490, y=50, height=20, width=50)
    cal_button_4.pack()
    cal_button_4.place(x=675, y=50)

    # --------------Secant--------------
    f_label = ttk.Label(tab5, text='Function = ' + expression, font=("Arial", 18)).pack()
    m_i_label = ttk.Label(tab5, text='Enter Max Iterations:')
    e_label = ttk.Label(tab5, text='Enter Epsilon:')
    a_label = ttk.Label(tab5, text='X0:')
    b_label = ttk.Label(tab5, text='X1')
    max_iteration = ttk.Entry(tab5)
    epsilon = ttk.Entry(tab5)
    a_sec = ttk.Entry(tab5)
    b_sec = ttk.Entry(tab5)

    cal_button_5 = ttk.Button(tab5, text='Calculate',
                            command=lambda: call_Secant(expression, a_sec.get(), b_sec.get(), max_iteration.get(),
                                                        epsilon.get(), tab5, cal_button_5))
    m_i_label.pack()
    m_i_label.place(x=40, y=50)
    max_iteration.pack()
    max_iteration.place(x=155, y=50, height=20, width=50)
    e_label.pack()
    e_label.place(x=220, y=50)
    epsilon.pack()
    epsilon.place(x=295, y=50, height=20, width=50)
    a_label.pack()
    a_label.place(x=370, y=50)
    a_sec.pack()
    a_sec.place(x=400, y=50, height=20, width=50)
    b_label.pack()
    b_label.place(x=455, y=50)
    b_sec.pack()
    b_sec.place(x=480, y=50, height=20, width=50)
    cal_button_5.pack()
    cal_button_5.place(x=675, y=50)


def check_expr(expression):
    try:
        x = 0
        eval(expression)
    except:
        messagebox.showinfo('Error', 'Invalid Function Expression')
        pass
    else:
        MethodSelection(expression)


main = Tk()
main.title('Root Finder Program')
main.geometry("500x150")
main.resizable(False, False)

title = Label(main, text='Enter Function', font=("Arial", 18))
error_message = Label(main, text='Error: Invalid Function', fg='#f00', font=("Arial", 13))
expr = tkinter.StringVar()
function_entry = Entry(main, textvariable=expr, font=("Arial", 15))
next_button = Button(main, text='Proceed', command=lambda: check_expr(function_entry.get()))
browse_button = Button(main, text='Browse File', command=lambda: open_file(expr))

title.pack()
function_entry.pack()
function_entry.place(x=100, y=50, height=30, width=300)
next_button.pack()
next_button.place(x=225, y=100)
browse_button.pack()
browse_button.place(x=415, y=52)
main.mainloop()
