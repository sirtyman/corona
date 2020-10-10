import argparse

from corona.view.view import PlotStyle

from corona.model.data import ChartData
from corona.client.client import HttpClient
from corona.view.view import generate_chart


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--countries', type=str, nargs='*', default=[],
                        help='List of countries to display stats for.')
    parser.add_argument('--total', nargs='?', const=True, type=bool, default=False,
                        help='If True the total numbers will be displayed. Otherwise - daily cases.')
    args = parser.parse_args()

    return args


def generate_per_country(data_by_country, country, total):
    confirmed = ChartData(data_response=data_by_country[country]['confirmed'], data_description="Confirmed",
                          plot_style=PlotStyle.BLUE_SOLID, country=country, total=total)
    recovered = ChartData(data_response=data_by_country[country]['recovered'], data_description="Recovered",
                          plot_style=PlotStyle.YELLOW_DASH, country=country, total=total)
    deaths = ChartData(data_response=data_by_country[country]['deaths'], data_description="Deaths",
                       plot_style=PlotStyle.RED_DOTTED, country=country, total=total)
    generate_chart(confirmed, recovered, deaths)


def main(opts):
    client = HttpClient(opts.countries)
    results_per_country = client.get()

    for country in results_per_country.keys():
        generate_per_country(results_per_country, country, opts.total)


if __name__ == "__main__":
    options = parse_arguments()
    main(options)


