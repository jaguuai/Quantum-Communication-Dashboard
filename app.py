from flask import Flask, render_template
from quantum.bell_states import create_bell, run_circuit
from quantum.entanglement import create_entanglement, run_entanglement
from quantum.teleportation import create_teleportation, run_teleportation  # YENİ

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bell")
def bell():
    qc = create_bell()
    counts = run_circuit(qc)
    return render_template("bell.html", counts=counts)

@app.route("/entanglement")
def entanglement():
    qc = create_entanglement()
    counts = run_entanglement(qc)
    return render_template("entanglement.html", counts=counts)

# Teleportation Route - YENİ
@app.route("/teleportation")
def teleportation():
    qc = create_teleportation()
    counts = run_teleportation(qc)
    return render_template("teleportation.html", counts=counts)

if __name__ == "__main__":
    app.run(debug=True)