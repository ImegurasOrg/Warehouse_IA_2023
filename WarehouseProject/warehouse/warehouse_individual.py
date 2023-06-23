from ga.individual_int_vector import IntVectorIndividual

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # self.cost = 0
        # RETODO

    def compute_fitness(self) -> float:
        # TODO implement a fitness function for warehouse individual

        return 0
    # Calcula os caminhos completos percorridos pelos forklifts. Devolve uma lista de listas de células(as células percorridas por cada forklift);
    # e o numero máximo de passos necessário para percorrer todos os caminhos(i.e, o numero de células do caminho mais longo percorrido por um forklift)
    def obtain_all_path(self):
        # TODO implement a method to obtain all paths from the genome
        
        pass

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
        # RETODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # RETODO
        return new_instance