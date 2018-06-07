name = "OpenAIBot"

from gym.envs.registration import register

register(
    id='OpenAIBot-v0',
    entry_point='OpenAIBot.envs:OpenAIBotEnv',
)