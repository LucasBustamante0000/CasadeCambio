from shiny import App, reactive, render, ui

TAXAS = {
    "BRL": 1.0,        # Real brasileiro
    "USD": 0.20,       # Dólar
    "EUR": 0.18,       # Euro
    "JPY": 29.5,       # Iene
    "BTC": 0.000003    # Bitcoin 
}

app_ui = ui.page_fluid(
    ui.h2("Conversor de Moedas"),

    ui.input_numeric("valor", "Valor a converter:", None),
    ui.input_select("origem", "Moeda de origem:", list(TAXAS.keys()), selected="BRL"),
    ui.input_select("destino", "Moeda de destino:", list(TAXAS.keys()), selected="USD"),

    ui.hr(),
    ui.output_text("resultado")
)

def server(input, output, session):

    @output
    @render.text
    def resultado():
        valor = input.valor()
        origem = input.origem()
        destino = input.destino()

        if valor is None or valor <= 0:
            return "Por favor, insira um valor válido maior que zero."

        if origem == destino:
            return f"Moeda de origem e destino são iguais. Resultado: {valor:.2f} {destino}"

        valor_em_brl = valor / TAXAS[origem]
        valor_convertido = valor_em_brl * TAXAS[destino]

        return f"{valor:.2f} {origem} = {valor_convertido:.2f} {destino}"

app = App(app_ui, server)
