from rl_coach.agents.bc_agent import BCAgentParameters
from rl_coach.base_parameters import VisualizationParameters
from rl_coach.core_types import TrainingSteps, EnvironmentEpisodes, EnvironmentSteps, RunPhase
from rl_coach.environments.environment import MaxDumpMethod, SelectedPhaseOnlyDumpMethod
from rl_coach.environments.gym_environment import Atari
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.memories.memory import MemoryGranularity

####################
# Graph Scheduling #
####################

schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(10000000000)
schedule_params.steps_between_evaluation_periods = TrainingSteps(500)
schedule_params.evaluation_steps = EnvironmentEpisodes(5)
schedule_params.heatup_steps = EnvironmentSteps(0)

#########
# Agent #
#########
agent_params = BCAgentParameters()
agent_params.network_wrappers['main'].learning_rate = 0.00025
agent_params.memory.max_size = (MemoryGranularity.Transitions, 1000000)
# agent_params.memory.discount = 0.99
agent_params.algorithm.discount = 0.99
agent_params.algorithm.num_consecutive_playing_steps = EnvironmentSteps(0)
agent_params.memory.load_memory_from_file_path = 'datasets/montezuma_revenge.p'

###############
# Environment #
###############
env_params = Atari()
env_params.level = 'MontezumaRevenge-v0'
env_params.random_initialization_steps = 30

vis_params = VisualizationParameters()
vis_params.video_dump_methods = [SelectedPhaseOnlyDumpMethod(RunPhase.TEST), MaxDumpMethod()]
vis_params.dump_mp4 = False

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=vis_params)
