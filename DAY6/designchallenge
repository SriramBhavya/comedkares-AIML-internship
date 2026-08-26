# AI - Reasoning Under Uncertainty

# Probabilities of weather conditions
weather_probability = {
    "Sunny": 0.70,
    "Rainy": 0.20,
    "Cloudy": 0.10
}

print("Weather Prediction Using Uncertainty\n")

for weather, probability in weather_probability.items():
    print(f"{weather}: {probability * 100:.0f}%")

# Find the most probable weather
most_likely = max(weather_probability, key=weather_probability.get)

print("\nMost likely weather:", most_likely)
print("Confidence:", weather_probability[most_likely] * 100, "%")
