''' A toy example of playing Uno with random agents
'''

import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed

# Make environment
env = rlcard.make('uno', config={'seed': 0})
episode_num = 2

# Set a global seed
set_global_seed(0)

# Set up agents
agent_0 = RandomAgent(action_num=env.action_num)
agent_1 = RandomAgent(action_num=env.action_num)
agent_2 = RandomAgent(action_num=env.action_num)
agent_3 = RandomAgent(action_num=env.action_num)
env.set_agents([agent_0, agent_1, agent_2, agent_3])

for episode in range(episode_num):

    # Generate data from the environment
    trajectories, _ = env.run(is_training=False)

    # Print out the trajectories
    print('\nEpisode {}'.format(episode))
    for ts in trajectories[0]:
        print('State: {}, Action: {}, Reward: {}, Next State: {}, Done: {}'.format(ts[0], ts[1], ts[2], ts[3], ts[4]))
