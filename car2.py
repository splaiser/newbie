def make_car_list(manufacturer,model,**car_info):
    car_info['manufacturer']= manufacturer
    car_info['model'] = model
    return car_info
car = make_car_list('subaru','outback',color='blue',tow_package=True)
print(car)