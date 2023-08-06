from rl_coach.agents.dfp_agent import DFPAgentParameters
from rl_coach.base_parameters import VisualizationParameters, EmbedderScheme, MiddlewareScheme, \
    PresetValidationParameters
from rl_coach.core_types import EnvironmentSteps, RunPhase
from rl_coach.environments.doom_environment import DoomEnvironmentParameters
from rl_coach.environments.environment import SelectedPhaseOnlyDumpMethod, MaxDumpMethod
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.schedules import LinearSchedule

####################
# Graph Scheduling #
####################

schedule_params = ScheduleParameters()
schedule_params.improve_steps = EnvironmentSteps(6250000)
schedule_params.steps_between_evaluation_periods = EnvironmentSteps(62500)
schedule_params.evaluation_steps = EnvironmentSteps(6250)

# There is no heatup for DFP. heatup length is determined according to batch size. See below.

#########
# Agent #
#########
agent_params = DFPAgentParameters()
schedule_params.heatup_steps = EnvironmentSteps(agent_params.network_wrappers['main'].batch_size)

agent_params.network_wrappers['main'].learning_rate = 0.0001
agent_params.exploration.epsilon_schedule = LinearSchedule(0.5, 0, 10000)
agent_params.exploration.evaluation_epsilon = 0
agent_params.algorithm.goal_vector = [1]  # health


# scale observation and measurements to be -0.5 <-> 0.5
agent_params.network_wrappers['main'].input_embedders_parameters['measurements'].input_rescaling['vector'] = 100.
agent_params.network_wrappers['main'].input_embedders_parameters['measurements'].input_offset['vector'] = 0.5
agent_params.network_wrappers['main'].input_embedders_parameters['observation'].input_offset['vector'] = 0.5

# changing the network scheme to match Coach's default network, as it performs better on this preset
agent_params.network_wrappers['main'].input_embedders_parameters['observation'].scheme = EmbedderScheme.Medium
agent_params.network_wrappers['main'].input_embedders_parameters['measurements'].scheme = EmbedderScheme.Medium
agent_params.network_wrappers['main'].input_embedders_parameters['goal'].scheme = EmbedderScheme.Medium
agent_params.network_wrappers['main'].middleware_parameters.scheme = MiddlewareScheme.Medium

# scale the target measurements according to the paper (dividing by standard deviation)
agent_params.algorithm.scale_measurements_targets['GameVariable.HEALTH'] = 30.0

###############
# Environment #
###############
env_params = DoomEnvironmentParameters()
env_params.level = 'HEALTH_GATHERING'
vis_params = VisualizationParameters()
vis_params.video_dump_methods = [SelectedPhaseOnlyDumpMethod(RunPhase.TEST), MaxDumpMethod()]
vis_params.dump_mp4 = False

########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.test = True
preset_validation_params.min_reward_threshold = 1600
preset_validation_params.max_episodes_to_achieve_reward = 70

graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=vis_params,
                                    preset_validation_params=preset_validation_params)
