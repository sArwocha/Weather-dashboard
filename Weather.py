import requests
from datetime import datetime
from rich.console import Console
from rich.panel import Panel

console = Console()

api_key="e7909643d787aedd90a62c370de27d3d"
base_url="http://api.openweathermap.org/data/2.5/weather?"

while True:
    city_name=input("Enter the name of your City: ")

    complete_url= f"{base_url}q={city_name}&appid={api_key}&units=metric"

    try:
        response= requests.get(complete_url)      #here request.get act as a pathway to api that act as a id and response is the data that we get..
    except requests.exceptions.ConnectionError:
        console.print("connection error, Check your Internet....")
        exit() 



    data=response.json()

    if data["cod"]!="404":
        main = data["main"]
        weather = data["weather"][0]

        temp= main["temp"]
        humidity= main["humidity"]
        desc= weather["description"]
        wind=data["wind"]["speed"]
        wind_gust=data["wind"]["gust"]

        console.print(Panel(f"weather in {city_name}", style="bold cyan"))
        console.print(f"[yellow]Temperature[/yellow] : {temp}")
        console.print(f"[blue]Humidity[/blue]:    {humidity}%")
        console.print(f"[green]Description[/green]: {desc.capitalize()}")
        console.print(f"[purple]Wind Speed[/purple]: {wind} m/s")
        console.print(f"[red]Wind Gust[/red]: {wind_gust} m/s")
        console.print(f"[white]Time Pulled[/white]: {datetime.now().strftime('%H:%M:%S')}")

    else:
        console.print("City Not Found. Please check the spelling.")

    again=input("Do you want to check another city's weather ???(y/n) : ")
    if again.lower()!="y":
        break