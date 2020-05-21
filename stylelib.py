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


def pastel(title, x_title=None, y_title=None, legends=None):
    rcparams()
    # rcParams["legend.facecolor"]

    bkcolor = (0.9176470588235294, 0.9176470588235294, 0.9490196078431372, 1.0)
    sns.set_palette("Set2", 8, 1)
    fig, ax = plt.subplots(1, 1)    
    ax.set_facecolor(bkcolor)
    # print(ax.get_facecolor())
    plt.title(title, fontdict = {'fontsize' : 16})
    ax.legend(['$x(t)$', '$y(t)$']) 
    plt.tight_layout(pad=2)
    ax.grid(True, color='w')
    return plt, fig, ax

def darkplot(title, x_title=None, y_title=None, ax_grid='y'):
    rcparams()

    # Palette
    bkcolor = "#121212"
    linecolor = "#3f3f3f"
    numberscolor = "#FFFFFFA0"
    title_color = "#FFFFFFE0"
    
    # Original
    # bkcolor = "#0D0D0D"
    # linecolor = "#83818C"
    
    palette = sns.diverging_palette(10, 220, sep=80, n=2)
    palette.reverse()
    sns.set_palette(palette, desat=0.95)

    # More rc params
    matplotlib.rcParams["legend.facecolor"] = bkcolor
    matplotlib.rcParams["legend.loc"] = "upper left"
    matplotlib.rcParams["legend.frameon"] = False
    matplotlib.rcParams['text.color'] = numberscolor
   
    # Creates one graph plot
    fig, ax = plt.subplots(1, 1)

    # Background color configs
    ax.set_facecolor(bkcolor)
    fig.set_facecolor(bkcolor)

    # Title and layout
    plt.title(title, loc='left', pad=50, fontdict = {'fontsize' : 18, 'color': title_color})
    plt.tight_layout(pad=2) 
    
    # Axes params (line colors, number colors, etc)
    ax.spines["bottom"].set_color(linecolor) 
    ax.spines["left"].set_color(bkcolor)
    ax.tick_params(axis='x', colors=numberscolor, color=linecolor)
    ax.tick_params(axis='y', colors=numberscolor, color=bkcolor)
    ax.spines["top"].set_color(bkcolor) 
    ax.spines["right"].set_color(bkcolor)

    ax.grid(True, axis=ax_grid, linewidth=0.5, color=linecolor)
    
    return plt, fig, ax

def dark_legend(ax, legend):
    ncol = 2
    bbox = [-0.01, 1.14]
    ax.legend(legend, ncol=ncol, bbox_to_anchor=bbox)