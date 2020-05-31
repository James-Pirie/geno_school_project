from Geno import *
import textwrap


def main():
    number_to_analyse = int(input("How many genotypes would you like to analise?: "))

    yes = ["yes", "ya", "y",
           "yeah", "ye", "affirmative",
           "positive", "true", "ye"]
    print_dna = input("Would you like to print the genotype in full for manual analysis?")

    for i in range(number_to_analyse):
        print("*******************************************************************************************************")
        print(f"Genotype Data {i}")
        man = Geno(1000)
        man.get_genotype()
        man.find_disease()
        if print_dna.lower().strip() in yes:

            print(f"genetic code:\n{textwrap.fill(man.dna, 101)}")
        if i != number_to_analyse - 1:
            press_enter = input("Press enter to continue")


if __name__ == '__main__':

    main()

