from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract


class MyWrapper(EWrapper):
    def __init__(self):
        super().__init__()

    def error(self, reqId, errorCode, errorString):
        print(f"Error {errorCode}: {errorString}")

    def contractDetails(self, reqId, contractDetails):
        print(f"Contract Details: {contractDetails.contract}")


class MyClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)


def request_option_data(client):
    contract = Contract()
    contract.symbol = "AAPL"  # Símbolo del subyacente (por ejemplo, Apple)
    contract.secType = "OPT"  # Tipo de seguridad: "OPT" para opciones
    contract.exchange = "SMART"  # Intercambio (puede ajustarse según tus necesidades)
    contract.currency = "USD"  # Moneda
    contract.lastTradeDateOrContractMonth = (
        "202412"  # Fecha de vencimiento en formato yyyymm
    )

    # Puedes ajustar los parámetros del contrato según tus necesidades

    # Solicitar detalles del contrato de opciones
    client.reqContractDetails(1, contract)


def main():
    wrapper = MyWrapper()
    client = MyClient(wrapper)

    client.connect(
        "127.0.0.1", 7497, clientId=1
    )  # Ajusta la IP y el puerto según tu configuración

    # Solicitar datos de opciones
    request_option_data(client)

    client.run()


if __name__ == "__main__":
    main()
