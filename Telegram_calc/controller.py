import operations as op
import user_interface as ui
import log



def button_click():
    '''
    Ввода данных, расчет и вывод результат
    '''

    while True:
        choice = ui.choice_calc('')
        sign = ui.operation(' ')
        if choice == 1:
            a= ui.rational_number(1)
            b = ui.rational_number(2)
            op.init_ratio(a, b)
        elif choice == 2:
            a, ai = ui.complex_number(1)
            b, bi = ui.complex_number(2)
            op.init_compl(a, ai, b, bi)
        elif choice==3:
            break
        if sign == '+':
            result = op.sum()
        if sign == '-':
            result = op.sub()
        if sign == '*':
            result = op.mult()
        if sign == '/':
            result = op.div()
        if sign=='**':
            result=op.exp()
        if result == False:
            result = ui.error_result()


        data = f'{op.x} {sign} {op.y}'
        ui.output_result(data, result)
        log.logger(data, result)
