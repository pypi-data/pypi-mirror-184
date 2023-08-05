from typing import Any, List, Union

import numpy as np
from matplotlib import pyplot as plt


def moving_average(x: List[float], window_length: Union[int, None] = None) -> np.ndarray[np.float32, Any]:
    if window_length is None:
        window_length = max(len(x) // 10, 1)
    return np.convolve(x, np.ones(window_length), "valid") / window_length


def plot_results(test_rewards: List[float], title: str = "Rewards", loss: List[float] = None) -> None:
    ma_rewards = moving_average(test_rewards)
    fig, ax = plt.subplots()
    plt.plot(ma_rewards, label="rewards")
    ax.set_xlabel("Game number")
    ax.set_ylabel("Moving Average Rewards")
    ax.set_title(title)

    if loss is not None:
        ax2 = ax.twinx()
        ax2.plot(moving_average(loss), label="loss", color="red")
        ax2.set_ylabel("Moving Average Loss")
        fig.legend()

    plt.show()


def plot_ac_results(test_rewards: List[float], actor_loss: List[float], critic_loss: List[float]) -> None:

    ma_rewards = moving_average(test_rewards)
    fig, (ax, ax1) = plt.subplots(2, 1)
    ax.plot(ma_rewards, label="rewards")
    ax.set_xlabel("Game number")
    ax.set_ylabel("Moving Average Rewards")
    ax.set_title("Rewards")

    ma_aloss = moving_average(actor_loss)
    ma_closs = moving_average(critic_loss)

    ax1.plot(ma_aloss, label="Actor Loss")
    ax1.set_xlabel("Game number")
    ax1.set_ylabel("ACtor Loss")
    ax2 = ax1.twinx()
    ax2.plot(ma_closs, label="Critic Loss", color="red")
    ax2.set_ylabel("Critic Loss")
    ax1.legend()
    ax2.legend()

    plt.show()
