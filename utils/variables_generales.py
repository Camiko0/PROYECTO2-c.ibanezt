ventas_del_dia = 0

def reset_ventas_del_dia() -> None:
    global ventas_del_dia
    ventas_del_dia = 0

def set_variable_ventas_del_dia(ventas: int) -> None:
    global ventas_del_dia
    ventas_del_dia += ventas

def get_variable_ventas_del_dia() -> int:
    return ventas_del_dia