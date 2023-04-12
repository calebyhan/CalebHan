import airlabs
from decouple import config
import plotly.express as px
import pandas as pd


api = airlabs.API(config("KEY"))


def view_current():
    data = api.flights(_view="array", _fields="hex,reg_number,lat,lng,dir,speed,dep_iata,arr_iata")
    df = pd.DataFrame(data)
    df.rename(columns={0: "Hex", 1: "Reg Number", 2: "Latitude", 3: "Longitude", 4: "Direction", 5: "Speed", 6: "Arrival", 7: "Departure"}, inplace=True)
    print(df)

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Reg Number", hover_data=["Hex", "Arrival", "Departure", "Speed", "Direction"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=800)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()


view_current()
