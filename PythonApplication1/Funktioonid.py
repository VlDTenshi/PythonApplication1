
def arithmetic(a1:float,symbol:str,a2:float):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korrutamine, / jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str symbol: Tehing
    :rtype: var Määramata tüüp
    """
    if symbol in ["+","-","/","*"]:
        if symbol=="/" and a2==0:
            vas="Div/0"
        else:
            vas=eval(str(a1)+symbol+str(a2))
    else:
        vas="Tundmatu tehing!"
    return vas