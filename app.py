from shiny import App, reactive, render, ui

# Taxas de conversão em relação ao Real Brasileiro
RATES = {
    "BRL": 1.0,        # Real Brasileiro
    "USD": 0.20,       # Dólar
    "EUR": 0.18,       # Euro
    "JPY": 29.5,       # Iene
    "BTC": 0.000003    # Bitcoin
}

app_ui = ui.page_fluid(
    ui.h2("Currency Converter"),

    # Entrada de valor numérico
    ui.input_numeric("amount", "Amount to convert:", None),
    ui.input_select("from_currency", "From currency:", list(RATES.keys()), selected="BRL"),
    ui.input_select("to_currency", "To currency:", list(RATES.keys()), selected="USD"),

    ui.hr(),
    ui.output_text("result")
)

def server(input, output, session):

    @output
    @render.text
    def result():
        amount = input.amount()
        from_currency = input.from_currency()
        to_currency = input.to_currency()

        # Verifica se o valor é válido
        if amount is None or amount <= 0:
            return "Please enter a valid amount greater than zero."

        # Verifica se as moedas são iguais
        if from_currency == to_currency:
            return f"The source and target currencies are the same. Result: {amount:.2f} {to_currency}"

        # Conversão intermediária para BRL e depois para moeda de destino
        amount_in_brl = amount / RATES[from_currency]
        converted_amount = amount_in_brl * RATES[to_currency]

        return f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"

app = App(app_ui, server)
