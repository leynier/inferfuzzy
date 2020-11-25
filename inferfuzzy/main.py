import typer

from .defuzzifications import centroid_defuzzification
from .memberships import (
    GammaMembership,
    GaussianMembership,
    LambdaMembership,
    LMembership,
    SMembership,
    ZMembership,
)
from .systems import LarsenSystem, MamdaniSystem
from .var import Var

app = typer.Typer()


@app.command()
def run():
    variety_var = Var("variety")
    variety_var += "low", ZMembership(1, 2)
    variety_var += "normal", GaussianMembership(3, 2)
    variety_var += "high", SMembership(4, 6)

    diversity_percent_var = Var("diversity")
    diversity_percent_var += "low", GammaMembership(70, 100)
    diversity_percent_var += "normal", LambdaMembership(40, 60, 80)
    diversity_percent_var += "high", LMembership(30, 50)

    clients_percent_var = Var("clients")
    clients_percent_var += "low", LMembership(20, 40)
    clients_percent_var += "normal", LambdaMembership(30, 60, 90)
    clients_percent_var += "high", GammaMembership(80, 100)

    sales_percent_var = Var("sales")
    sales_percent_var += "low", LMembership(20, 60)
    sales_percent_var += "normal", LambdaMembership(30, 60, 90)
    sales_percent_var += "high", GammaMembership(90, 100)

    variety_var.graph()
    diversity_percent_var.graph()
    clients_percent_var.graph()
    sales_percent_var.graph()

    mamdani = MamdaniSystem(defuzz_func=centroid_defuzzification)
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    mamdani += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")

    larsen = LarsenSystem(defuzz_func=centroid_defuzzification)
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    mamdani += (
        variety_var.into("low")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("low")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("normal")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("normal")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("low")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("normal")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("high")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("low")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("normal")
    ), sales_percent_var.into("low")
    larsen += (
        variety_var.into("high")
        & diversity_percent_var.into("high")
        & clients_percent_var.into("high")
    ), sales_percent_var.into("normal")

    variety_val = typer.prompt("Input variety value", type=int)
    diversity_val = typer.prompt("Input diversity percent", type=float)
    clients_val = typer.prompt("Input clients percent", type=float)

    mamdani_result: float = mamdani.infer(
        variety=variety_val,
        diversity=diversity_val,
        clients=clients_val,
    )["sales"]

    larsen_result: float = larsen.infer(
        variety=variety_val,
        diversity=diversity_val,
        clients=clients_val,
    )["sales"]

    typer.echo(f"Mamdani: {'{:.2f}'.format(mamdani_result)}%")
    typer.echo(f"Larsen {'{:.2f}'.format(larsen_result)}%")
