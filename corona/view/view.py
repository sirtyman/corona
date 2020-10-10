import matplotlib.pyplot as plt


class PlotStyle:
    BLUE_SOLID = 'b-'
    YELLOW_DASH = 'y--'
    RED_DOTTED = 'r.'


class Chart:
    def __init__(self, *data):
        self.data = data

    def plot_data(self):
        plt.figure()
        legend_handles = []
        for d in self.data:
            if d is None:
                continue
            plt.title(d.country)
            plt.plot(d.data_frame['Cases'], d.plot_style)
            plt.grid(True)
            legend_handles.append(d.name)
            # plt.plot(plot_data['recovered'], "y--")
            # plt.plot(plot_data['deaths'], "r.")
        plt.legend(legend_handles)
        plt.show()


def generate_chart(confirmed, recovered, deaths):
    chart = Chart(confirmed, recovered, deaths)
    chart.plot_data()
