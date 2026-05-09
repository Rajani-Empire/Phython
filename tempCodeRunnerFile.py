def calculate_total(exp) :
    total = 0
    for item in exp:
        total = total +item
    return total




tom_exp_list = [2100,3400,3500]
jon_expence_list = [200,500,700]


toms_total = calculate_total(tom_exp_list)

jon_total =calculate_total(jon_exp_list)

print(toms_total)
print(jon_total)