import settings


class Environment:
    def __init__(self, observers=None):
        self.observers = []
        self.reports = []
        self.population = None

    def create_new_generation(self):
        if self.observers:
            self.show_scores()
            self.compute()

    def show_scores(self):
        print(">    Final Round Score")
        for obs in self.observers:
            print("%s > %s -> Score: %d %d" % (obs.core.tag, obs.ai, obs.get_score(), obs.core.obs.score))
        print("-------------------------")

    def add_observer(self, observer):
        self.observers.append(observer)

    def compute(self):
        if self.population:
            # Set the score to the individuals from the population
            for index, obs in enumerate(self.observers):
                self.population.pool[index].set_score(obs.get_score())

            self.population.create_offsprings()
        else:
            self.population.reset_pool()

        for index, obs in enumerate(self.observers):
            obs.core.set_threshold(self.population.get_individual(index).get_threshold())
            obs.set_ai(self.population.get_individual(index))
            obs.reset()




