from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def trap_rain_water(heights):
    n = len(heights)
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = [0] * n

    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water[left] = left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water[right] = right_max - heights[right]
            right -= 1

    return {
        "heights": heights,
        "water": water,
        "total_water": sum(water)
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compute", methods=["POST"])
def compute():
    data = request.json
    heights = data["heights"]

    result = trap_rain_water(heights)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)