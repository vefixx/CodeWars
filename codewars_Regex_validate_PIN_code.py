#мое решение
def validate_pin(pin):
    pin_numbers = []
    if pin.isdigit():
        for i in pin:
            pin_numbers.append(i)
        
        if len(pin_numbers) == 4 or len(pin_numbers) == 6:
            return True 
        else:
            return False
    else:
        return False

    


#второй способ решения
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()