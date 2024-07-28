import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import io

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def show_weather():
    city = city_combo.get()
    if city:
        api_key = 'YOUR_API_KEY'  # Replace with your actual API key
        weather_data = get_weather(api_key, city)
        if weather_data['cod'] == 200:
            main = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            icon_code = weather_data['weather'][0]['icon']

            weather_info = (
                f"Weather: {main}\n"
                f"Description: {description}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            
            # Display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo
            
            weather_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found!")
    else:
        messagebox.showwarning("Input Error", "Please select a city")

# List of sample cities
cities = ["New York", "London", "Paris", "Tokyo", "Mumbai", "Sydney"]

# Setting up the GUI
root = tk.Tk()
root.title("Real-Time Weather App")
root.geometry("400x400")
root.configure(bg="lightblue")

# Styling options
font_style = ("Helvetica", 12)
button_style = {"bg": "blue", "fg": "white", "font": ("Helvetica", 12, "bold")}

city_label = tk.Label(root, text="Select City:", font=font_style, bg="lightblue")
city_label.pack(pady=(20, 10))

city_combo = ttk.Combobox(root, values=cities, font=font_style)
city_combo.pack(pady=10, padx=20, fill=tk.X)

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather, **button_style)
get_weather_button.pack(pady=20)

icon_label = tk.Label(root, bg="lightblue")
icon_label.pack(pady=10)

weather_label = tk.Label(root, text="", font=font_style, bg="lightblue")
weather_label.pack(pady=10)

root.mainloop()
