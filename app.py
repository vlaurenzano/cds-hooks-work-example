import cds_hooks_work as cds
import os

app = cds.App()


@app.patient_view("hello-world", "The patient greeting service greets a patient!", title="Patient Greeter")
def greeting(r: cds.PatientViewRequest, response: cds.Response):
    card = cds.Card.info("hello world!", cds.Source("demo_service"))
    card.add_link(cds.Link.absolute("cds-hooks-work", "https://github.com/vlaurenzano/cds-hooks-work"))
    response.add_card(card)
    response.httpStatusCode = 200


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', False)
    port = os.environ.get("PORT", 5000)
    app.serve(host="0.0.0.0", debug=debug, port=port)
