import matplotlib.pyplot as plt
import matplotlib.style as stl
import seaborn as sns
import matplotlib

def rcparams():
    matplotlib.rcParams['font.sans-serif'] = "Open Sans"



def my_style(title, x_title=None, y_title=None):
    stl.use('seaborn-dark')
    # sns.set_palette("pastel")
    fig, ax = plt.subplots(1, 1)
    # print(ax.get_facecolor())
    plt.title(title)
    plt.tight_layout(pad=2)
    ax.grid(True)
    return plt, fig, ax


def pastel(title, x_title=None, y_title=None):
    rcparams()

    bkcolor = (0.9176470588235294, 0.9176470588235294, 0.9490196078431372, 1.0)
    sns.set_palette("Set2", 8, 1)
    fig, ax = plt.subplots(1, 1)    
    ax.set_facecolor(bkcolor)
    # print(ax.get_facecolor())
    plt.title(title, fontdict = {'fontsize' : 16})
    plt.tight_layout(pad=2)
    ax.grid(True, color='w')
    return plt, fig, ax