import random
from individual import Individual
import settings


class Population:
    def __init__(self, size, mutation):
        self.pool = []
        self.mutation = mutation
        self.size = size
        self.reset_pool()

        self.max_score = 0
        self.count_max = 0

        self.all_fit = False

    def get_fittest(self):
        if not self.pool:
            return 0, 0
        max_fittest_score = max([indv.score for indv in self.pool])
        fittest = [indv for indv in self.pool if indv.score == max_fittest_score]

        fittest_trait = fittest[0].threshold  # get the threshold value
        self.pool.remove(fittest[0])

        return fittest_trait, max_fittest_score

    def create_offsprings(self):
        if not self.pool:
            self.reset_pool()

        # If the minimum score is equal with the max score possible then there is no need to create offsprings
        if min([indv.score for indv in self.pool]) == settings.MAX_SCORE_SESSION:
            print("They smart!")
            return

        print("> Apply the law of jungle\n# Begin")
        # ----------------------------------- Selection ----------------------------------------------
        first_max_score, first_max_fit = self.get_fittest()
        second_max_score, second_max_fit = self.get_fittest()

        self.check_evolution(first_max_score)

        # Check if the individuals are stuck and there no sign of evolution for "EXTINCTION_COUNTER" rounds
        if self.count_max > settings.EXTINCTION_COUNTER and self.max_score != settings.MAX_SCORE_SESSION:
            print("BEGIN the extinction")
            self.reset_pool()
        else:
            # ----------------------------------- Crossover ---------------------------------------------
            threshold1 = first_max_score
            threshold2 = second_max_score
            # The final weight ratio: 75% from the first and 25% from the second
            offspring_threshold = (threshold1 * 3 + threshold2) / 4
            print("Offspring: %d" % offspring_threshold)

            # Kill the old population
            self.pool.clear()

            # ------------------------------------ Mutation ----------------------------------------------
            # Create the offsprings and apply mutation
            for i in range(self.size):
                self.pool.append(Individual(offspring_threshold + self.get_mutation(i)))
            print("# End")

    def get_mutation(self, index):
        if random.uniform(0, 1) <= self.mutation:
            value = random.randint(-15, 15)
            print("Mutation with %d on the %d-th AI" % (value, index))
            return value
        return 0

    def check_evolution(self, max_score_session):
        if self.max_score < max_score_session:
            # They have evolved
            self.max_score = max_score_session
            self.count_max = 1
        elif self.max_score == max_score_session:
            # No sign of evolution
            self.count_max += 1

    def reset_pool(self):
        # Make new individuals
        print("Reset Pool")
        self.pool = []
        for i in range(self.size):
            self.pool.append(Individual(random.randrange(40, 150, 5)))

    def add_individuals(self, indv):
        self.pool.append(indv)

    def get_individual(self, index):
        return self.pool[index]

    def get_pool(self):
        return self.pool


