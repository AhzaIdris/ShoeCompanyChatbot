from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_shoe", methods=["POST"])
def get_shoe():
    data = request.get_json()
    category = data.get("category")
    material = data.get("material")
    size = data.get("size")

    # Simulated product info response
    product_info = {
        "category": category,
        "material": material,
        "size": size,
        "description": f"{material.capitalize()} {category} in size EU {size}."
    }

    return jsonify(product_info)

if __name__ == "__main__":
    app.run(debug=True)
