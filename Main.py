from Geno import *
import textwrap


def main():
    # ask how many genes the user would like to generate
    number_to_analyse = int(input("How many genotypes would you like to analise?: "))
    # all possible parameters for yes
    yes = ["yes", "ya", "y",
           "yeah", "ye", "affirmative",
           "positive", "true", "ye"]
    # ask user if they would like to print the dna in full
    print_dna = input("Would you like to print the genotype in full for manual analysis?")

    # for every time the user would like to repeat, repeat
    for i in range(number_to_analyse):
        print("*******************************************************************************************************")
        print(f"Genotype Data {i}")  # print the dna id number
        man = Geno(1000)  # set the length of the dna
        man.get_genotype()  # generate dna string
        man.find_disease()  # search the dna for diseases
        if print_dna.lower().strip() in yes:  # check if the user wants to print the dna
            # print the dna
            print(f"genetic code:\n{textwrap.fill(man.dna, 101)}")
        if i != number_to_analyse - 1:  # pause the printing of the report until the user presses enter
            press_enter = input("Press enter to continue")


# if the program is run call main function
if __name__ == '__main__':
    main()  # activate main function
