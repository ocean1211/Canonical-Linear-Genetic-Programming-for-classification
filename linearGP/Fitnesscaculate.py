import Preprocess
import Initialize
import numpy

#0: register 1: input
#instruction_list  [target, operater, source, mode]


def implement_operation(instruction_list,input_list):
    #print(instruction_list,input_list)
    # print('input ',len(input_list))
    fitness = 0
    for n in range(len(input_list[0])):
        Register = [0.00, 0.00, 0.00, 0.00]
        for i in range(len(instruction_list)):
            if instruction_list[i][3] == 0: #mode : register
                if instruction_list[i][1] == 0: #operater : '+'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] + Register[instruction_list[i][2]]),2)
                elif instruction_list[i][1] == 1: #operator : '-'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] - Register[instruction_list[i][2]]),2)
                elif instruction_list[i][1] == 2: #operator : '*'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] * Register[instruction_list[i][2]]),2)
                    # print("then:",Register)
                elif instruction_list[i][1] == 3:#operator : '/'
                    if Register[instruction_list[i][2]]/10.0 == 0.0 or -0.0:
                        continue
                    else:
                        Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] / Register[instruction_list[i][2]]),2)
                        # print("then:",Register)

            if instruction_list[i][3] == 1:#mode input
                # print(instruction_list[i])
                if instruction_list[i][1] == 0: #operater : '+'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] + input_list[instruction_list[i][2]][n]),2)

                elif instruction_list[i][1] == 1: #operator : '-'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] - input_list[instruction_list[i][2]][n]),2)
                elif instruction_list[i][1] == 2: #operator : '-'
                    Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] * input_list[instruction_list[i][2]][n]),2)
                elif instruction_list[i][1] == 3:#operator : '/'
                    if round(input_list[instruction_list[i][2]][n], 2)/10.0 == 0.0 or -0.0:
                        continue
                    else:
                        Register[instruction_list[i][0]] = round((Register[instruction_list[i][0]] / input_list[instruction_list[i][2]][n]), 2)

        max = numpy.argmax(Register[0:Preprocess.classnumber])
        if Preprocess.classlist[max] == input_list[len(input_list)-1][n] :
            fitness += 1
    return fitness
