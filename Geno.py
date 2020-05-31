import random


# setup the geno object, where a single persons dna will be generated
class Geno:
    def __init__(self, genotype_size,):  # initialize the object
        """setup the possible diseases"""
        self.disease_pos_or_neg = {"cancer": False,
                                   "heart_disease": False,
                                   "alzheimer": False,
                                   "cystic_fibrosis": False,
                                   "crohns_disease": False}
        self.size = genotype_size  # setup the size of the dna
        self.dna = ""
        self.full_genotype = ""
        self.probability = {"cancer": 0,
                            "heart_disease": 0,
                            "alzheimer": 0,
                            "cystic_fibrosis": 0,
                            "crohns_disease": 0}

    def get_genotype(self):
        """generate the dna"""
        base_pairs = ["G", "A",
                      "C", "T"]  # all possible base values
        number_of_base_pairs = len(base_pairs)
        for i in range(self.size):  # randomly generate dna the length required made of base values
            base_pairs_chance = random.randint(0, number_of_base_pairs - 1)
            self.dna += base_pairs[base_pairs_chance]

    def find_disease(self):
        """Analyse the dna for diseases"""
        # all disease base patterns
        cancer = "GATTA"
        heart_disease = "CCTGA"
        alzheimer = "GAATT"
        cystic_fibrosis = "CCCAC"
        crohns_disease = "TTACG"
        # every possible disease
        list_of_diseases = [cancer, heart_disease,
                            alzheimer, cystic_fibrosis,
                            crohns_disease]
        list_of_diseases_names = ["cancer", "heart_disease", "alzheimer",
                                  "cystic_fibrosis", "crohns_disease"]

        # look for every disease type in the dna
        for i in range(len(list_of_diseases)):
            if list_of_diseases[i] in self.dna:
                self.disease_pos_or_neg[str(list_of_diseases_names[i])] = True  # if disease found return true
                self.probability[list_of_diseases_names[i]] = self.dna.count(list_of_diseases[i])

        print("*******************************************************************************************************")
        for x in range(len(list_of_diseases)):
            # determine the risk factor based on how many instances of a disease there is in the dna
            risk: str
            risk_for_particular_disease = self.probability[list_of_diseases_names[x]]

            if risk_for_particular_disease == 0:
                risk = "None"
            elif risk_for_particular_disease == 1:
                risk = "Low"
            elif risk_for_particular_disease == 2:
                risk = "Medium"
            elif risk_for_particular_disease == 3:
                risk = "High"
            else:
                risk = "Very High"
            replica_dna_sample = []  # duplicate the dna
            previous_values = 0
            location_of_disease = []
            if risk_for_particular_disease > 0:
                replica_dna_sample = self.dna.split(list_of_diseases[x])  # split the dna where the dna is
                for i in range(len(replica_dna_sample)-1):  # check the length of the list items to find dna locations
                    location_of_disease.append((len(replica_dna_sample[i])+1)+previous_values)
                    previous_values += (len(replica_dna_sample[i])+1)

            # print out the report
            print(f" disease: {list_of_diseases_names[x]}, \n increased probability: "
                  f"{self.disease_pos_or_neg[list_of_diseases_names[x]]} \n "
                  f"genetic preposition: {self.disease_pos_or_neg[list_of_diseases_names[x]]}  \n"
                  f" number of {list_of_diseases_names[x]} prepositions: {self.probability[list_of_diseases_names[x]]}"
                  f"\n risk factor: {risk}")
            if len(replica_dna_sample) > 0:
                if len(replica_dna_sample) == 1:
                    print(f" {list_of_diseases_names[x]} genetic preposition is located at base index"
                          f"{location_of_disease[0]}")
                else:
                    print(f" {list_of_diseases_names[x]} genetic prepositions are located at base indexes "
                          f"{location_of_disease}")

            print("----------------------------------------------------------------------------------------------------"
                  "--")
