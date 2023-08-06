from rl_coach.agents.dfp_agent import DFPAgentParameters, HandlingTargetsAfterEpisodeEnd
from rl_coach.base_parameters import VisualizationParameters
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps, RunPhase
from rl_coach.environments.doom_environment import DoomEnvironmentParameters
from rl_coach.environments.environment import SelectedPhaseOnlyDumpMethod, MaxDumpMethod
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.schedules import LinearSchedule

####################
# Graph Scheduling #
####################

schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(10000000000)
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(50)
schedule_params.evaluation_steps = EnvironmentEpisodes(3)

# There is no heatup for DFP. heatup length is determined according to batch size. See below.

#########
# Agent #
#########
agent_params = DFPAgentParameters()
schedule_params.heatup_steps = EnvironmentSteps(agent_params.network_wrappers['main'].batch_size)

agent_params.network_wrappers['main'].learning_rate = 0.0001
agent_params.exploration.epsilon_schedule = LinearSchedule(0.5, 0, 10000)
agent_params.exploration.evaluation_epsilon = 0

# this works better than the default which is 64
agent_params.algorithm.num_consecutive_playing_steps = EnvironmentSteps(1)

agent_params.algorithm.use_accumulated_reward_as_measurement = True
agent_params.algorithm.goal_vector = [0, 1]  # ammo, accumulated_reward
agent_params.algorithm.handling_targets_after_episode_end = HandlingTargetsAfterEpisodeEnd.LastStep


###############
# Environment #
###############
env_params = DoomEnvironmentParameters()
env_params.level = 'basic'

vis_params = VisualizationParameters()
vis_params.video_dump_methods = [SelectedPhaseOnlyDumpMethod(RunPhase.TEST), MaxDumpMethod()]
vis_params.dump_mp4 = False

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=vis_params)
