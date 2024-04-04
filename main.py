def calculate_energy_momentum():
    velocityOneInitial = float(input("Enter velocity of object one (initial): "))
    velocityTwoInitial = float(input("Enter velocity of object two (initial): "))
    velocityOneFinal = float(input("Enter velocity of object one (final): "))
    velocityTwoFinal = float(input("Enter velocity of object two (final): "))

    print(f'\n')


    # not ours
    massOne = .587
    massTwo = 1.292

    #ours
    #massOne = 0.5898
    #massOne = 1.283


    #massTwo = 0.5902
    #massTwo = 1.283

    kmassOne = massOne * 0.5
    kmassTwo = massTwo * 0.5

    kineticEnergyInitial = (kmassOne * velocityOneInitial ** 2) + (kmassTwo * velocityTwoInitial ** 2)
    kineticEnergyFinal = (kmassOne * velocityOneFinal ** 2) + (kmassTwo * velocityTwoFinal ** 2)
    kpercentDifference = ((kineticEnergyFinal - kineticEnergyInitial) / kineticEnergyFinal) * 100
    kapercentDifference = ((kineticEnergyInitial-kineticEnergyFinal)/kineticEnergyInitial)*100

    print(f'Initial Kinetic Energy = {kineticEnergyInitial}')
    print(f'Final Kinetic Energy = {kineticEnergyFinal}')
    print(f'Percent error for kinetic energy = {abs(kpercentDifference)} %')
    print(f'Alternate percent error for kinetic energy = {abs(kapercentDifference)} %')

    print(f'\n')


    momentumInitial = (massOne * velocityOneInitial) + (massTwo * velocityTwoInitial)
    momentumFinal = (massOne * velocityOneFinal) + (massTwo * velocityTwoFinal)
    mpercentDifference = ((momentumFinal - momentumInitial) / momentumFinal) * 100
    mapercentDifference = ((momentumInitial-momentumFinal)/momentumInitial)*100

    print(f'Initial Momentum = {momentumInitial}')
    print(f'Final Momentum = {momentumFinal}')
    print(f'Percent error for momentum = {abs(mpercentDifference)} %')
    print(f'Alternate percent error for momentum = {abs(mapercentDifference)} %')

    print(f'\n')

    velocityCalcOneFinal = (((massOne-massTwo)/(massOne+massTwo))*velocityOneInitial)+((2*massTwo)/(massOne+massTwo)*velocityTwoInitial)
    velocityCalcTwoFinal = ((2*massOne)/(massOne+massTwo)*velocityOneInitial)-((massOne-massTwo)/(massOne+massTwo)*velocityTwoInitial)

    print(f'First final velocity calculation = {velocityCalcOneFinal}')
    print(f'Second final velocity calculation = {velocityCalcTwoFinal}')

    print(f'\n')

    calcPercentErrorVelocityOneFinal = ((velocityOneFinal-velocityCalcOneFinal)/(velocityCalcOneFinal))*100
    calcpercentErrorVelocityTwoFinal = ((velocityTwoFinal-velocityCalcTwoFinal)/(velocityCalcTwoFinal))*100

    print(f'velocity 1 error calc vs experimental = {abs(calcPercentErrorVelocityOneFinal)} %')
    print(f'velocity 2 error calc vs experimental = {abs(calcpercentErrorVelocityTwoFinal)} %')



def main():
    print("lab 5 pain bypass")
    calculate_energy_momentum()


if __name__ == "__main__":
    main()
