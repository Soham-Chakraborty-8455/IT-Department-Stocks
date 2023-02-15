from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

####======================CONFIGURATIONS STARTS===============================================================####
app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DepartmentalStocks.db"
db.init_app(app)

####================================DATABASE MODEL STARTS=============================================================================================####
class LabDetails(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    SystemNumber = db.Column(db.Integer, nullable=False)
    datePurchased = db.Column(db.String, nullable=False)
    Brand = db.Column(db.String, nullable=False)
    suppliedby = db.Column(db.String, nullable=False)
    specifications= db.Column(db.String, nullable=False)
    IPaddress= db.Column(db.String, nullable=False)
    Warrenty= db.Column(db.String, nullable=False)
    OS= db.Column(db.String, nullable=False)

class FaultRegister(db.Model):
    slno= db.Column(db.Integer, primary_key=True)
    date= db.Column(db.String, nullable=False)
    ItemIssued= db.Column(db.String, nullable=False)
    ItemRecieved= db.Column(db.String, nullable=False)
    Quantity= db.Column(db.Integer, nullable=False)
    Lab= db.Column(db.String, nullable=False)
    Remarks= db.Column(db.String, nullable=False)
    Signature= db.Column(db.String, nullable=False)

class Materials(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    Material= db.Column(db.String, nullable=False)
    Brand= db.Column(db.String, nullable=False)
    Quantity= db.Column(db.Integer, nullable=False)

class Movement(db.Model):
    slno= db.Column(db.Integer, primary_key=True)
    Particulars= db.Column(db.String, nullable=False)
    To= db.Column(db.String, nullable=False)
    From= db.Column(db.String, nullable=False)
    Remarks= db.Column(db.String, nullable=False)

class IssueTable(db.Model):
    slno= db.Column(db.Integer, primary_key=True)
    ConcernedPerson= db.Column(db.String, nullable=False)
    Problem= db.Column(db.String, nullable=False)
    Remarks= db.Column(db.String, nullable=False)
    Signature= db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/facultyregisterinput", methods=["POST", "GET"])
def facultyregisterinputs():
    if request.methods=="POST":
        date= request.json["date"]
        ItemIssued= request.json['ItemIssued']
        ItemRecieved= request.json['ItemRecieved']
        Quantity= request.json['Quantity']
        Lab= request.json['Lab']
        Remarks= request.json['Remarks']
        Signature= request.json['Signature']
        entry= FaultRegister(date=date, ItemIssued=ItemIssued, ItemRecieved=ItemRecieved, Quantity=Quantity, Lab=Lab, Remarks=Remarks, Signature= Signature)
        with app.app_context():
            db.session.add(entry)
            db.session.commit()
    return jsonify({"status": "uploaded"})


@app.route("/Labdetailsinput", methods=["POST", "GET"])
def labdetailsinput():
    if request.methods=="POST":
        SystemNumber= request.json['SystemNumber']
        datePurchased= request.json['datePurchased']
        Brand= request.json['Brand']
        suppliedby= request.json['suppliedby']
        specifications= request.json['specifications']
        IPaddress= request.json['IPaddress']
        Warrenty= request.json['Warrenty']
        OS= request.json['OS']
        entry= LabDetails(SystemNumber= SystemNumber, datePurchased=datePurchased, Brand=Brand, suppliedby=suppliedby, specifications=specifications, IPaddress=IPaddress, Warrenty=Warrenty, OS=OS )
        with app.app_context():
            db.session.add(entry)
            db.session.execute()
    return jsonify({"status": "uploaded"})


@app.route("/Materialsinput", methods=["POST", "GET"])
def Materialsinput():
    if request.method=="POST":
        Material= request.json['Material']
        Brand= request.json['Brand']
        Quantity= request.json['Quantity']
        entry= Materials(Material=Material, Brand=Brand, Quantity=Quantity)
        with app.app_context():
            db.session.add(entry)
            db.session.commit()
    return jsonify({"status": "uploaded"})

@app.route("/Movementsinput", methods=["POST", "GET"])
def Movementsinput():
    if request.method=="POST":
        Particulars= request.json['Particulars']
        To= request.json['To']
        From= request.json['From']
        Remarks= request.json['Remarks']
        entry= Movement(Particulars=Particulars, To=To, From=From, Remarks=Remarks)
        with app.app_context():
            db.session.add(entry)
            db.session.commit()
    return  jsonify({"Status":"Uploaded"})

@app.route("IssueTableinput", methods=["POST", "GET"])
def IssueTableInput():
    if request.method=="POST":
        ConcernedPerson= request.json['ConcernedPerson']
        Problem= request.json['Problem']
        Remarks= request.json['Remarks']
        Signature= request.json['Signature']
        entry= IssueTable(ConcernedPerson=ConcernedPerson, Problem=Problem, Remarks=Remarks, Signature=Signature)
        with app.app_context():
            db.session.add(entry)
            db.session.commit()
    return jsonify({"Status":"Uploaded"})

@app.route("/facultyregisterdisp", methods=["POST", "GET"])
def facultyregisterdisp():
    with app.app_context():
        totalList= FaultRegister.query.all()
    return jsonify({"FacultyRegister": totalList})

@app.route("/labdetailsdisp", methods=["POST", "GET"])
def labdetailsdisp():
    with app.app_context():
        totalList= LabDetails.query.all()
    return jsonify({"labDetails": totalList})

@app.route("/Materialsdisp", methods=["POST", "GET"])
def materialsdisp():
    with app.app_context():
        totalList= Materials.query.all()
    return jsonify({"Materials": totalList})

@app.route("/movementsdisp", methods=["POST", "GET"])
def movementsdisp():
    with app.app_context():
        totalList= Movement.query.all()
    return jsonify({"Movement": totalList})

@app.route("/issuetabledisp", methods=["POST", "GET"])
def issuetabledisp():
    with app.app_context():
        totalList= IssueTable.query.all()
    return jsonify({"IssueTable": totalList})

if __name__ == "__main__":
    app.run(debug=True)