import pandas as pd

if __name__ == "__main__":
    us_cities = pd.read_csv("/home/kali/forensics/evidence/location_evidence/WifiLocation.csv", delimiter="|")

    import plotly.express as px

    fig = px.line_mapbox(us_cities, lat="Latitude", lon="Longitude", color="Timestamp", hover_data=[], zoom=3, height=900)

    fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat=41,
                      margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.show()
