from gym.envs.registration import register

register(
        id='minimize-1d-np-v0',
        entry_point='phygym_minimize.envs:Minimize1DNP',
        )