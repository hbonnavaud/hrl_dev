
from hbrl.environments import PointEnv, MapsIndex
from hbrl.agents import SAC, TILO
import pickle


def simulation(environment, agent):

    nb_episodes = 1000
    nb_interactions_per_episodes = 200
    states_seen = []
    for episode_id in range(nb_episodes):
        state = environment.reset()
        states_seen.append(state)
        for interaction_id in range(nb_interactions_per_episodes):
            action = agent.action(state)
            state, _, _ = environment.step(action)
            states_seen.append(state)
    with open("states_seen.pkl", "wb") as f:
        pickle.dump(states_seen, f)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    environment = PointEnv(map_name=MapsIndex.MEDIUM.value)
    agent = SAC(state_space=environment.state_space, action_space=environment.action_space)

    simulation(environment, agent)
