import cds_hooks_work as cds
import os

app = cds.App()


@app.patient_view("hello-world", "The patient greeting service greets a patient!", title="Patient Greeter")
def greeting(r: cds.PatientViewRequest, response: cds.Response) -> cds.Response:
    response.cards = [cds.Card.info("hello world!", "demo_service")]
    response.httpStatusCode = 200


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', False)
    port = os.environ.get("PORT", 5000)
    app.serv(host="0.0.0.0", debug=debug, port=port)
